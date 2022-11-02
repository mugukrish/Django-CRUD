from django.shortcuts import render, redirect
from django.views import View
from .models import ProductModel
# Create your views here.

class ProductsListView(View):
    def get(self, request):
        queryset = ProductModel.objects.all()
        context = {
            'object':queryset
        }
        return render(request, 'product/displayall.html', context)

    def post(self, request):
        if 'add' in request.POST:
            return redirect('addproducturlname')
        if 'update' in request.POST:
            return redirect('updateproducturlname')
        if 'delete' in request.POST:
            return redirect('deleteproducturlname')


class ProductAddView(View):
    def get(self, request):
        return render(request, 'product/productadd.html')

    def post(self, request):
        ProductModel.objects.create(productname=request.POST['productname'],
                                   price=request.POST['price'])
        return redirect('viewproducturlname')


class ProductUpdateView(View):
    def post(self, request, **kwargs):
        if 'updateproductname' in request.POST:
            obj = ProductModel.objects.get(id=kwargs['id'])
            obj.productname = request.POST['updateproductname']
            obj.price = request.POST['updateprice']
            obj.save()
            return redirect('viewproducturlname')

        obj = ProductModel.objects.get(id=kwargs['id'])
        context = {
                   'object':obj
        }
        return render(request, 'product/productupdate.html', context)


class ProductDeleteView(View):
    def post(self, request, **kwargs):
        obj = ProductModel.objects.get(id=kwargs['id'])
        obj.delete()
        return redirect('viewproducturlname')
