from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render

from .models import Product

# Create your views here.

# Function based view
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

# http based response
def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        # render html page, with HTTP status code of 404
        raise Http404
    return HttpResponse(f"Product id {obj.id}")

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