from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Expense, User
import csv
from django.views import View
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer, ExpenseSerializer

class UserCreate(generics.CreateAPIView):
    """
    API view for creating a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    """
    API view for retrieving user details.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ExpenseCreate(generics.CreateAPIView):
    """
    API view for creating a new expense.
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def create(self, request, *args, **kwargs):
        """
        Handles the creation of a new expense and associates users with it.

        Args:
            request (Request): The request containing the expense data.

        Returns:
            Response: The created expense data and HTTP status.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        expense = serializer.save()
        expense.users.set(serializer.validated_data['users'])
        expense.details = serializer.validated_data.get('details', {})
        expense.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ExpenseList(generics.ListAPIView):
    """
    API view for listing all expenses.
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseDetail(generics.RetrieveAPIView):
    """
    API view for retrieving details of a specific expense.
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class BalanceSheetView(View):
    """
    View for rendering the balance sheet template with expenses.
    """
    def get(self, request):
        """
        Handles GET requests to display the balance sheet.

        Args:
            request (Request): The request object.

        Returns:
            HttpResponse: Rendered balance sheet template with expenses.
        """
        expenses = Expense.objects.all()
        context = {
            'expenses': expenses,
        }
        return render(request, 'balance_sheet.html', context)

class DownloadBalanceSheetView(View):
    """
    View for downloading the balance sheet as a CSV file.
    """
    def get(self, request):
        """
        Handles GET requests to download the balance sheet in CSV format.

        Args:
            request (Request): The request object.

        Returns:
            HttpResponse: CSV file response containing the balance sheet data.
        """
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="balance_sheet.csv"'
        writer = csv.writer(response)

        writer.writerow(['Title', 'Amount', 'Users', 'Split Method', 'Details'])

        for expense in Expense.objects.all():
            users = ', '.join([user.name for user in expense.users.all()])
            writer.writerow([expense.title, expense.amount, users, expense.split_method, expense.details])

        return response
