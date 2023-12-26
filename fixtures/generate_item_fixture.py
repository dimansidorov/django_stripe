import json
from faker import Faker
import random


fake = Faker()


def generate_fake_product() -> dict:
    product = {
        "name": fake.word().title(),
        "description": fake.text(),
        "price": random.randint(1, 10000)
    }

    return product


def create_fixture(count: int = 10):
    products = []

    for idx in range(1, count + 1):
        item = {
            "model": "product.item",
            "pk": idx,
            "fields": generate_fake_product()
        }
        products.append(item)

    with open('items.json', 'w', encoding='utf-8') as new_file:
        json.dump(products, new_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    create_fixture()
