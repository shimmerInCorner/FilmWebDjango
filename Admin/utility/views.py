from django.shortcuts import render
from django.views import View


# about-us
class FaqsView(View):
    def get(self,request):
        greeting = {}
        greeting['title'] = "About"
        greeting['pageview'] = "OnlineMovie"
        return render(request, 'pages/pages-faqs.html', greeting)

