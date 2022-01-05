from django.db import models

class Loan(models.Model):
    # A good reason to create a custom through table, is the ability to add extra/helpful fields like due_date etc
    due_date = models.DateField()
    # we need two fields for the book relationship and the borrower relationship
    # book will have many loans
    # borrower will have many loans
    # loans will track 1 book and 1 borrower each
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    borrower = models.ForeignKey('Borrower', on_delete=models.CASCADE)

    def __str__(self):
        return self.due_date