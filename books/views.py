from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def home(request):
    data = Book.objects.all()
    context = {
        'data':data
    }
    return render(request, 'index.html', context)

def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form':form})

def update_book(request, id):
    data = get_object_or_404(Book,id=id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm(instance=data)

    return render(request, 'create_book.html', {'form':form})

def detail_book(request, id):
    object = Book.objects.get(id=id)
    context = {'object':object}
    return render(request, 'detail.html', context)

def delete_book(request, id):
    data = get_object_or_404(Book, id=id)
    if request.method=="POST":
        data.delete()
        return redirect('/')
    return render(request, 'delete.html', {'data':data})


