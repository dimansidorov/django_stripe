from django.core.management.base import BaseCommand

from products.models import Item


class Command(BaseCommand):
    help = 'Добавить Товар'

    def handle(self, *args, **options):
        Item.objects.create(name='Ноутбук Apple MacBook Air 13 2022',
                            description='MacBook Air 2022 года можно назвать одним из крупнейших обновлений линейки за всю историю. ',
                            price=179900)
