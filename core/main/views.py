from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bag 
# Create your views here.

class BagListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        bags = Bag.objects.all()
        return render(request, self.template_name, {'bags':bags})

class BagDetailView(DetailView):
    template_name = 'home_detail.html'

    def get(self, request, id):
        bag = Bag.objects.get(pk=id)
        return render(request, self.template_name, {'bag':bag})