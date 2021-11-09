from django.http import request
from django.shortcuts import redirect, render,HttpResponseRedirect,HttpResponse
from django.views import View
from .models import Movie
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def movie_page(request):

    all_movies = Movie.objects.all().order_by("-id")  # select all movies in database

    paginator = Paginator(all_movies, 9)

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
    return render(request,'menu/ecommerce/ecommerce-customers.html',{'movies':movies})

@csrf_exempt
def movie_list_home(request):

    all_movies = Movie.objects.all().order_by("-id")   # select all movies in database

    paginator = Paginator(all_movies, 9)

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

@csrf_exempt
def delete(request):
    delete_id = request.GET.get('id')

    Movie.objects.filter(id=delete_id).delete()

    return HttpResponseRedirect('/about-us/movie_manage')

@csrf_exempt
def select(request):
    select_id = request.GET.get('id')
    all_movies = Movie.objects.filter(id=select_id)
    paginator = Paginator(all_movies, 9)
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

@csrf_exempt
def select_tp(request):
    select_type = request.GET.get('type')
    all_movies = Movie.objects.filter(type__icontains=select_type)
    paginator = Paginator(all_movies, 9)
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

@csrf_exempt
def select_ct(request):
    select_country = request.GET.get('country')
    all_movies = Movie.objects.filter(country__icontains=select_country)
    paginator = Paginator(all_movies, 9)
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

@csrf_exempt
def select_prc(request):
    select_minPrice = request.GET.get('minPrice')
    select_maxPrice = request.GET.get('maxPrice')
    all_movies = Movie.objects.filter(price__range=(select_minPrice, select_maxPrice))
    paginator = Paginator(all_movies, 9)
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

@csrf_exempt
def add(request):
    # if request.method == "GET":
    #    return HttpResponseRedirect('/about/movie')

    if request.method == 'POST':
        new_item = request.POST
        print(new_item)
        Movie.objects.create(name=new_item['movie_name'],img_url=new_item['img_url'],
                             duration=new_item['duration'],grade=new_item['grade'],
                             type=new_item['category'],watch_url=new_item['watch_url'],
                             price=new_item['price'],features=new_item['features'],
                             description=new_item['productdesc'],meta_description=new_item['metadescription'],
                             country=new_item['country'],restriction=new_item['restriction'],)

        return HttpResponseRedirect('/about-us/movie_manage')

def search(request):
    movie_name = request.GET.get('movie_name')
    all_movies = Movie.objects.filter(name__icontains=movie_name)
    paginator = Paginator(all_movies, 9)
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

    return render(request, 'menu/ecommerce/ecommerce-products.html', {'movies': movies})

# Products
class ProductsView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Movies"
        greeting['pageview'] = "Services"
        return render(request, 'menu/ecommerce/ecommerce-products.html',greeting)

# Product Details
class ProductDetailsView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Movie Detail"
        greeting['pageview'] = "Services"
        return render(request, 'menu/ecommerce/ecommerce-product-detail.html',greeting)

# Orders
class OrdersView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Movies"
        greeting['pageview'] = "Services"
        return render(request, 'menu/ecommerce/ecommerce-orders.html',greeting)

# Customers
class CustomersView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Movies Management"
        greeting['pageview'] = "Services"
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

# Add Movie
class AddProductView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Add Movie"
        greeting['pageview'] = "Services"
        return render(request, 'menu/ecommerce/ecommerce-add-product.html',greeting)
