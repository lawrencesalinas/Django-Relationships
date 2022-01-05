from django.urls import path

from .views.book_views import Books, BookDetail
from .views.author_views import Authors, AuthorDetail
from .views.loan_views import Loans, LoanDetail
from .views.borrower_views import Borrowers, BorrowerDetail


urlpatterns = [
    path('authors', Authors.as_view(), name='authors'),
    path('authors/<int:pk>', AuthorDetail.as_view(), name='author_detail'),
    path('books', Books.as_view(), name='books'),
    path('books/<int:pk>', BookDetail.as_view(), name='book_detail'),
    path('loans', Loans.as_view(), name='loans'),
    path('loans/<int:pk>', LoanDetail.as_view(), name='loan_detail'),
    path('borrowers', Borrowers.as_view(), name='loans'),
    path('borrowers/<int:pk>', BorrowerDetail.as_view(), name='loan_detail'),
]
