from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from .models import *



# Create your views here.
class HomeView(View):
    def get(self, request):
        data = {
            'todos' : TODO.objects.all()
        }
        return render(request, 'home.html', context=data)