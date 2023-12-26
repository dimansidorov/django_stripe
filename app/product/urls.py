from django.urls import path

from .views import ItemDetailView, buy_item_view


urlpatterns = [
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item'),
    path('buy/<pk>/', buy_item_view, name='buy')
]
