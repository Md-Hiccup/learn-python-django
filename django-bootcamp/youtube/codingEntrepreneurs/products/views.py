from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render

from .models import Product
from .forms import ProductForm

# Create your views here.

# Function based view
# def bad_view(request, *args, **kwargs):
#     my_request_data = dict(request.GET)
#     new_product = my_request_data.get("new_product")
#     print(my_request_data, new_product)
#     if new_product[0].lower() == 'true':
#         print("new product")
#         Product.objects.create(title=my_request_data.get('title')[0], content=my_request_data.get('content')[0])
#     return HttpResponse('Bad Views')


def search_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    query = request.GET.get('q')  # q
    qs = Product.objects.filter(title__icontains=query[0])
    print(query, qs)
    context = {"name": "Huzzy"}
    return render(request, "home.html", context)

def product_create_view(request, *args, **kwargs):
    print(request.POST)
    print(request.GET)
    context = {}
    if request.method == 'POST':
        post_data = request.POST or None
        if post_data != None:
            my_form = ProductForm(request.POST)
            print(my_form.is_valid())
            print('post data', post_data)
    return render(request, 'forms.html', context)

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