from django.urls import path,re_path
from ecommerce import views
urlpatterns = [
    # Ecommerce
    # path('movies',views.ProductsView.as_view(),name='ecommerce-products'),# Products
    path('product-details',views.ProductDetailsView.as_view(),name='ecommerce-product-detail'),# Product Details
    path('orders',views.OrdersView.as_view(),name='ecommerce-orders'),# Orders
    # path('management',views.CustomersView.as_view(),name='ecommerce-customers'),# Cusomers
    path('cart',views.CartView.as_view(),name='ecommerce-cart'),# Cart
    path('check-out',views.CheckoutView.as_view(),name='ecommerce-checkout'),# Checkout
    path('shops',views.ShopsView.as_view(),name='ecommerce-shops'),# Shops
    path('add-product',views.AddProductView.as_view(),name='ecommerce-add-product'),# Shops

    path('add',views.add),
    path('movie_manage',views.movie_page),
    path('movies',views.movie_list_home),
    re_path(r'^delete$',views.delete),
    path('search',views.search),
    re_path(r'^select_tp$',views.select_tp),
    re_path(r'^select_ct$',views.select_ct),
    re_path(r'^select_prc$', views.select_prc),
]
