from rest_framework import serializers

from .models.book import Book
from .models.author import Author
from .models.borrower import Borrower
from .models.loan import Loan

# this is our regular BookSerializer -> used for creating/updating
class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = '__all__'
    # if the author field is missing, this will fail create/update validations

# this will be our BookReadSerializer
class BookReadSerializer(serializers.ModelSerializer):
  author = serializers.StringRelatedField()
  class Meta:
    model = Book
    fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
  # this utilizes our custom related_name set on the model Book
  # this is not the only way to make this reference, but it is the preferred way
  # by running through the serializer, we have access to all the fields
  written_books = BookSerializer(many=True, read_only=True)
  # if we wanted to, we could do this like so, but we only get the book title:
  # written_books = serializers.StringRelatedField(many=True)
  class Meta:
    model = Author
    fields = '__all__'

class BorrowerSerializer(serializers.ModelSerializer):
  borrowed_books = serializers.StringRelatedField(many=True)
  class Meta:
    model = Borrower
    fields = '__all__'

class LoanReadSerializer(serializers.ModelSerializer):
  book = BookSerializer()
  borrower = BorrowerSerializer()
  class Meta:
    model = Loan
    fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
  class Meta:
      model = Loan
      fields = '__all__'