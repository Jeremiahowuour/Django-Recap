from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
# from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, "library/home.html")

# Create Book
def createBook(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("readBooks")

    context = {"form": form}
    return render(request, "library/form.html", context)

# Read all books
def readBooks (request):
    books = Book.objects.all()
    context ={'books':books}
    return render(request, "library/books.html", context)

# Read a single book
def readOneBook(request, pk):
    book = Book.objects.get(id=pk)
    context = {"book":book}
    return render (request, "library/book.html", context)

# Update Book
def updateBook(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm (instance= book)

    if request.method == "POST":
        form = BookForm(request.POST, instance = book)
        if form.is_valid():
            form.save()
            return redirect("readBooks")
    context = {"form": form}
    return render(request, "library/form.html", context)

# Delete Book
def deleteBook(request, pk):
    book = Book.objects.get(id=pk)
    
    if request.method =='POST':
        book.delete()
        return redirect("readBooks")
    
    context = {"book": book}
    return render(request, "library/delete.html", context)