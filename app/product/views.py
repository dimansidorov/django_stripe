from typing import Any
from django.http import JsonResponse, Http404
from django.views.generic import DetailView
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

import stripe

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemDetailView(DetailView):
    """Item Detail View"""

    model = Item
    template_name = 'product/product_detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        return context


@csrf_exempt
def buy_item_view(request, pk: int):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=settings.DOMAIN + '/success.html',
        cancel_url=settings.DOMAIN + '/cancel.html',
    )
    return JsonResponse({"session_id": session.id}, status=200)
