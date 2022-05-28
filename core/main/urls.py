from django.urls import path
from . import views
from .views import CategoryListView

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('test/', views.test, name='test'),
    path('test/test_detail/', views.test_detail, name='test_detail'),

]