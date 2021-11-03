from django.http import request
from django.shortcuts import redirect, render,HttpResponseRedirect,HttpResponse
from django.views import View
from .models import Movie
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage


def movie_page(request):

    all_movies = Movie.objects.all()  # select all movies in database

    paginator = Paginator(all_movies, 8)

    if request.method == "GET":
        page = request.GET.get('page')
        try:
            movies = paginator.page(page)
        except PageNotAnInteger:
            movies = paginator.page(1)
        except InvalidPage:
            return HttpResponse('404')
        except EmptyPage:
            movies = paginator.page(paginator.num_pages)

    return render(request,'menu/ecommerce/ecommerce-products.html',{'movies':movies})


def delete(request):
    delete_id = request.GET.get('id')

    Movie.objects.filter(id=delete_id).delete()

    return HttpResponseRedirect('/about-us/management')

def select(request):
    select_type = request.GET.get('type')
    all_movies = Movie.objects.filter(type__icontains=select_type)
    paginator = Paginator(all_movies, 8)
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            movies = paginator.page(page)
        except PageNotAnInteger:
            movies = paginator.page(1)
        except InvalidPage:
            return HttpResponse('404')
        except EmptyPage:
            movies = paginator.page(paginator.num_pages)

    return render(request,'menu/ecommerce/ecommerce-products.html',{'movies':movies})

def add(request):
    # if request.method == "GET":
    #    return HttpResponseRedirect('/about/movie')

    if request.method == 'POST':
        new_item = request.POST
        print(new_item)
        Movie.objects.create(name=new_item['name'],img_url=new_item['img_url'],
                             duration=new_item['duration'],grade=new_item['grade'],
                             type=new_item['type'],watch_url=new_item['watch_url'],
                             price=new_item['price'])

        return HttpResponseRedirect('/about-us/management')

def search(request):
    global search_item

    if request.method=='POST':
        search_item = request.POST['movie_name']

    all_movies = Movie.objects.filter(name__icontains=search_item)
    paginator = Paginator(all_movies, 8)

    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except InvalidPage:
        return HttpResponse('404')
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    return render(request, 'menu/ecommerce/ecommerce-products.html', {'movies': movies})
# Products
class ProductsView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Products"
        greeting['pageview'] = "Ecommerce"        
        return render(request, 'menu/ecommerce/ecommerce-products.html',greeting)

# Product Details
class ProductDetailsView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Product Detail"
        greeting['pageview'] = "Ecommerce"        
        return render(request, 'menu/ecommerce/ecommerce-product-detail.html',greeting)

# Orders
class OrdersView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Orders"
        greeting['pageview'] = "Ecommerce"        
        return render(request, 'menu/ecommerce/ecommerce-orders.html',greeting)

# Customers
class CustomersView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Customers"
        greeting['pageview'] = "Ecommerce"        
        return render(request, 'menu/ecommerce/ecommerce-customers.html',greeting)

# Cart
class CartView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Cart"
        greeting['pageview'] = "Ecommerce"        
        return render(request, 'menu/ecommerce/ecommerce-cart.html',greeting)

# Check-out
class CheckoutView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Checkout"
        greeting['pageview'] = "Ecommerce"        
        return render(request, 'menu/ecommerce/ecommerce-checkout.html',greeting)

# Shops
class ShopsView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Shops"
        greeting['pageview'] = "Ecommerce"        
        return render(request, 'menu/ecommerce/ecommerce-shops.html',greeting)

# Add Product
class AddProductView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Add Product"
        greeting['pageview'] = "Ecommerce"        
        return render(request, 'menu/ecommerce/ecommerce-add-product.html',greeting)
