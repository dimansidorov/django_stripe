from django.http import JsonResponse
from django.views import View
import stripe
from django.conf import settings
from django.views.generic import TemplateView

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemTemplateView(TemplateView):
    template_name = 'products/item.html'

    def get_context_data(self, pk, **kwargs):
        item = Item.objects.get(pk=pk)
        context = super().get_context_data(**kwargs)
        context['item'] = item
        return context


