from django.shortcuts import render, redirect

from .models import BookRecord

# Create your views here.

def create_view(request):
    context = {}
    if request.method=='POST':
        BookRecord.objects.create(title=request.POST['title'],
                                 description=request.POST['description'])
    return render(request, 'createdata.html', context)


def view_books_list(request):
    data = BookRecord.objects.all()
    context = {
               'object':data
    }
    return render(request, 'viewlist.html', context)

def delete_book(request, id=None):
    if request.method == 'POST':
        obj = BookRecord.objects.get(id=id)
        obj.delete()
    return redirect(view_books_list)


def update_book(request, id=None):
    print(request.POST)
    if request.method == 'POST' and 'update' in request.POST :

        obj = BookRecord.objects.get(id=id)
        context = {
                   "object": obj
        }
        return render(request, 'updatebook.html', context)

    if request.method == 'POST' and 'update' not in request.POST:
        obj = BookRecord.objects.get(id=id)
        print(obj.title)
        obj.title = request.POST['title']
        obj.description  = request.POST['description']
        obj.save()
        return redirect(view_books_list)
