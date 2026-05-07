from django.shortcuts import render, redirect
from .models import Author
from .forms import CommentForm
# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    authors = Author.objects.all()
    comment_form = CommentForm()
    context = {
        'author': author,
        'comment_form': comment_form,
        'authors': authors,
    }
    return render(request, 'libraries/detail.html', context)

def create(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = author
        comment.save()

        return redirect('libraries:detail', author_pk=author.pk)
    context = {
        'author': author,
        'comment_form': comment_form,
    }

    return render(request, 'libraries/detail.html', context)