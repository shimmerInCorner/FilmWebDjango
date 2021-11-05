from django.http import request
from django.shortcuts import redirect, render
from django.views import View   
from django.contrib.auth.mixins import LoginRequiredMixin

# Dashboard
class DashboardView(LoginRequiredMixin,View):
    def get(self, request):
        print(request.session)
        greeting = {}
        greeting['title'] = "Home"
        greeting['pageview'] = "OnlineMovie"        
        return render(request, 'menu/index.html',greeting)
        # return render(request, 'pages/pages-faqs.html', greeting)
