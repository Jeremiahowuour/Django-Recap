from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookForm
from .models import Book

# Create your views here.

def home(request):
	return render(request, 'library/home.html')

def createBook(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("readBooks")

    context = {"form": form}
    return render(request, "library/form.html", context)

def readBooks (request):
     books = Book.objects.all()
     context ={'books':books}
     return render(request, "library/books.html", context)