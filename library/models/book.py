from django.db import models
from .author import Author

class Book(models.Model):
  title = models.CharField(max_length=100)
  # author = models.CharField(max_length=100)
  # we need to provide a model to relate to
  # so we'll import Author at the top
  # we also want to use on_delete, in the event one of our authors is deleted, it will
  # "cascade" and delete all the books assiciated with that author
  #this way is considered by many the "lazy"
  # authors = models.ForeignKey('Author', on_delete=models.CASCADE)
  # the preferred way to do this, which you should try to do unless its unavoidable
  #for whatever reason, looks like this
  author = models.ForeignKey(
    Author,
    on_delete=models.CASCADE,
    related_name='written_books'
  )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
