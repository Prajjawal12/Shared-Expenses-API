from django.db import models

class User(models.Model):
    """
    Model representing a user.

    Attributes:
        email (EmailField): Unique email address of the user.
        name (CharField): Name of the user.
        mobile_number (CharField): Mobile number of the user.
    """
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=10)

    def __str__(self):
        """
        Returns the string representation of the User instance.

        Returns:
            str: The name of the user.
        """
        return self.name

class Expense(models.Model):
    """
    Model representing an expense.

    Attributes:
        title (CharField): Title of the expense.
        amount (DecimalField): Total amount of the expense.
        users (ManyToManyField): Users associated with the expense.
        split_method (CharField): Method of splitting the expense ('equal', 'exact', 'percentage').
        details (JSONField): Detailed split information of the expense.
    """
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    users = models.ManyToManyField(User, related_name='expenses')
    split_method = models.CharField(max_length=10)  # 'equal', 'exact', 'percentage'
    details = models.JSONField(default=dict)  # Store split details

    def __str__(self):
        """
        Returns the string representation of the Expense instance.

        Returns:
            str: The title of the expense.
        """
        return self.title
