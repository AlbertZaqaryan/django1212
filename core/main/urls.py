from django.urls import path
from .views import BagListView, BagDetailView

urlpatterns = [
    path('', BagListView.as_view(), name='home'),
    path('<int:id>', BagDetailView.as_view(), name='home_detail')
]