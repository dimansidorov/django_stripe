from django.urls import path

from .views import ItemTemplateView

urlpatterns = [
    path('get/<int:pk>/', ItemTemplateView.as_view(), name='item'),
]
