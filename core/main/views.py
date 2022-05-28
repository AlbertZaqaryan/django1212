from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, Shoose, Brend
# Create your views here.

class CategoryListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        categories = Category.objects.all()
        return render(request, self.template_name, {'categories':categories})


def test(request):
    return render(request, 'home_detail.html')


def test_detail(request):
    return render(request, 'home_detail_detail.html')