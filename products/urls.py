from django.urls import path

from .views import CreateCheckoutSessionView, item

urlpatterns = [
    path('item/<int:pk>/', item, name='item'),
    path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='buy')
]
