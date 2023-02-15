from django.http import JsonResponse
from django.views import View
import stripe
from django.conf import settings
from django.views.generic import TemplateView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(['GET'])
@renderer_classes((TemplateHTMLRenderer,))
def item(request, pk):
    data = {'item': Item.objects.get(pk=pk)}
    return Response(data, template_name='products/item.html')

# class ItemTemplateView(TemplateView):
#     template_name = 'products/item.html'
#
#     def get_context_data(self, pk, **kwargs):
#         item = Item.objects.get(pk=pk)
#         context = super().get_context_data(**kwargs)
#         context['item'] = item
#         return context


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
        return JsonResponse({
            'id': checkout_session.id
        })

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
