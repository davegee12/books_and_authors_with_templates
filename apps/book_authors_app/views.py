from django.shortcuts import render, HttpResponse, redirect
from .models import Books, Authors

def index(request):
    context = {
        "all_books": Books.objects.all(),
        "all_authors": Authors.objects.all()
    }
    return render(request, 'book_authors_app/index.html', context)

def show(request):
    context = {
        "all_books": Books.objects.all(),
        "all_authors": Authors.objects.all()
    }
    return render(request, 'book_authors_app/show.html', context)

def view_book(request, id):
    id = int(id)
    request.session['book'] = id
    context = {
        "this_book": Books.objects.get(id = id),
        "all_authors": Authors.objects.all()
    }
    return render(request, 'book_authors_app/book.html', context)

def view_author(request, id):
    id = int(id)
    request.session['author'] = id
    context = {
        "this_author": Authors.objects.get(id = id),
        "all_books": Books.objects.all()
    }
    return render(request, 'book_authors_app/author.html', context)

def add_book(request):
    if request.method == "POST":
        book = Books.objects.create(title = request.POST['title'], desc = request.POST['desc'])
        print(book)
        return redirect("/", book)

def add_author(request):
    if request.method == "POST":
        author = Authors.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], notes = request.POST['notes'])
        print(author)
        return redirect("/authors", author)

def new_book(request):
    if request.method == "POST":
        book = Books.objects.get(id = request.POST['book_id'])
        author = Authors.objects.get(id = request.session['author'])
        print(request.POST['book_id'])
        author.books.add(book)
        return redirect("/authors", book)

def new_author(request):
    if request.method == "POST":
        author = Authors.objects.get(id = request.POST['author_id'])
        book = Books.objects.get(id = request.session['book'])
        print(request.POST['author_id'])
        book.author.add(author)
        return redirect("/", author)