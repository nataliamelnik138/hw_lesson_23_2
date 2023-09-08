import json
import subprocess

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        with open('catalog_data.json') as f:
            list_of_fixtures = json.load(f)
            list_category = []
            for item in list_of_fixtures:
                if item["model"] == "catalog.category":
                    list_category.append(item["fields"])

        category_for_create = []
        for category_item in list_category:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_for_create)

        with open('catalog_data.json', encoding='cp1251') as f:
            list_of_fixtures = json.load(f)
            list_product = []
            for item in list_of_fixtures:
                if item["model"] == "catalog.product":
                    category_pk = item['fields']['category']
                    item["fields"]["category"] = Category.objects.get(pk=category_pk)
                    list_product.append(item["fields"])

        product_for_create = []
        for category_item in list_product:
            product_for_create.append(
                Product(**category_item)
            )

        Product.objects.bulk_create(product_for_create)
