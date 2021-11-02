from django.urls import path
from utility import views


urlpatterns = [
    # About-us
    path('about-us',views.FaqsView.as_view(),name='pages-faqs'),# Faqs

]
