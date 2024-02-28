from random import choice, randint, uniform
import string

from django.core.management.base import BaseCommand
from myapp5.models import Product, Order

class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of products to create')
        parser.add_argument('orders_count', type=int, help='Number of orders')

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        products = []
        count = kwargs.get('count')
        orders_count = kwargs.get('orders_count')
        for _ in range(orders_count):
            random_suffix = ''.join(choice(string.ascii_letters) for _ in range(5))
            product_name = f'продукт номер {_}_{random_suffix}'

            # Проверка, существует ли продукт с таким именем
            while Product.objects.filter(name=product_name).exists():
                random_suffix = ''.join(choice(string.ascii_letters) for _ in range(5))
                product_name = f'продукт номер {_}_{random_suffix}'

            products.append(Product(
                name=product_name,
                order=choice(orders),
                description='длинное описание продукта, которое и так никто не читает',
                price=uniform(0.01, 999_999.99),
                amount=randint(1, 10_000),
            ))
        Product.objects.bulk_create(products)
