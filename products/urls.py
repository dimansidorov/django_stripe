from django.urls import path

from .views import ItemTemplateView, CreateCheckoutSessionView

urlpatterns = [
    path('item/<int:pk>/', ItemTemplateView.as_view(), name='item'),
    path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='buy')
]
