from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render

from .models import Product

# Create your views here.

# Function based view
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    context = {"name": "Huzzy"}
    return render(request, "home.html", context)

# http based response
def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        # render html page, with HTTP status code of 404
        raise Http404
    # print(dir(request))
    # return HttpResponse(f"Product id {obj.id}")
    return render(request, "products/detail.html", {"object": obj})

def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all() # [obj1, obj2, obj3, ...]
    context = {"object_list": qs}
    return render(request, 'products/list.html', context)

# json based response
def product_api_detail_view(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'Not found'})
    return JsonResponse({"id": obj.id})


# Class based view
# class HomeView():
#     pass