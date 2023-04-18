from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book, Category, Author
# Create your views here.

# def index(request):
#     categories = Category.objects.all().prefetch_related('book_set')
#     for cat in categories:
#         print(cat.book_set.all())
#     return HttpResponse("<body> </body>")

def index(request):
    Books = Book.objects.all().select_related("category")
    for book in Books:
        print(book)
    return HttpResponse("<body> </body>")