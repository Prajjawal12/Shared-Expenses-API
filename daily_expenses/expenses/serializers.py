from rest_framework import serializers
from .models import User, Expense
from rest_framework import generics

class UserSerializer(serializers.ModelSerializer):
    contributions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_contributions(self, user):
        """
        Retrieves a list of contributions made by the user towards various expenses.

        Args:
            user (User): The user instance for which contributions are to be fetched.

        Returns:
            list: A list of dictionaries containing expense details and the user's share.
        """
        expenses = user.expenses.all()
        return [
            {
                'expense_id': expense.id,
                'title': expense.title,
                'amount': expense.amount,
                'user_share': user.id in expense.details and float(expense.details[str(user.id)]) or 0.0
            }
            for expense in expenses
        ]

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'title', 'amount', 'users', 'split_method', 'details']

    def validate(self, data):
        """
        Validates the expense data to ensure proper allocation based on split method.

        Args:
            data (dict): The input data for the expense.

        Returns:
            dict: The validated data after applying necessary transformations.

        Raises:
            serializers.ValidationError: If the data does not conform to validation rules.
        """
        split_method = data.get('split_method')
        amount = data.get('amount')
        users = data.get('users')
        details = data.get('details')

        if not users:
            raise serializers.ValidationError("At least one user must be associated with the expense.")

        if split_method == 'equal':
            if amount <= 0:
                raise serializers.ValidationError("Total amount must be greater than 0.")
            equal_share = float(amount) / len(users)
            data['details'] = {str(user.id): equal_share for user in users}

        elif split_method == 'exact':
            if not details or sum(details.values()) != amount:
                raise serializers.ValidationError("Details must sum up to the total amount.")
            data['details'] = {str(k): float(v) for k, v in details.items()}

        elif split_method == 'percentage':
            if not details or sum(details.values()) != 100:
                raise serializers.ValidationError("Percentages must sum up to 100%.")
            data['details'] = {
                str(user.id): float(amount) * (percent / 100)
                for user, percent in zip(users, details.values())
            }

        else:
            raise serializers.ValidationError("Invalid split method. Choose 'equal', 'exact', or 'percentage'.")

        return data

    def to_representation(self, instance):
        """
        Customizes the representation of the Expense instance for serialization.

        Args:
            instance (Expense): The Expense instance to be serialized.

        Returns:
            dict: The serialized representation of the expense.
        """
        representation = super().to_representation(instance)
        representation['amount'] = float(representation['amount'])
        representation['details'] = {k: float(v) for k, v in representation['details'].items()}
        return representation
