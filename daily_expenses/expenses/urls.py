from django.urls import path
from .views import UserCreate, UserDetail, ExpenseCreate, ExpenseDetail, BalanceSheetView, DownloadBalanceSheetView, ExpenseList

urlpatterns = [
    path('users/', UserCreate.as_view(), name='user-create'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('expenses/', ExpenseList.as_view(), name='expense-list'),
    path('expenses/create/', ExpenseCreate.as_view(), name='expense-create'),
    path('expenses/<int:pk>/', ExpenseDetail.as_view(), name='expense-detail'),
    path('balance_sheet/', BalanceSheetView.as_view(), name='balance_sheet'),
    path('balance_sheet/download/', DownloadBalanceSheetView.as_view(), name='download_balance_sheet'),
]
