from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import LibrariesForm
# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    form = LibrariesForm()
    context = {
        'book': book,
        'form': form,
    }
    return render(request, 'libraries/detail.html', context)

def create(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == 'POST':
        form = LibrariesForm(request.POST)

        if form.is_valid():
            library = form.save(commit=False)
            library.book = book
            library.user = request.user
            library.save()
            return redirect('libraries:detail', book.pk)
        
def delete(request, book_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    
    return redirect('libraries:detail', book_pk)