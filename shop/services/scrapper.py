
import requests
from django.db import transaction
from selectolax.parser import HTMLParser

from django.utils.text import slugify
from shop.models import Product, Image, Category

urls = [
    "https://masterzoo.ua/ua/catalog/sobaki/",
    "https://masterzoo.ua/ua/catalog/koti/",
    "https://masterzoo.ua/ua/catalog/ptaxi/",
    "https://masterzoo.ua/ua/catalog/grizuni/",
    "https://masterzoo.ua/ua/catalog/akvariumistika/",
    "https://masterzoo.ua/ua/catalog/terariumistika/",
]


def parse_categories(url):
    response = requests.get(url)
    response.raise_for_status()

    html = response.text
    parser = HTMLParser(html)

    links = parser.css(".catalogCard-a")
    titles = [link.text(strip=True) for link in links]
    return titles


@transaction.atomic
def write_category_to_db(category_title):
    category, _ = Category.objects.get_or_create(slug=f"{slugify(category_title['Title'])}",
        defaults={'title': category_title['Title']})


def main():
    # Проходим по каждому URL и парсим категории
    for url in urls:
        categories = parse_categories(url)

        if categories:
            for category in categories:
                write_category_to_db(category)
        else:
            print(f"Категории на странице {url} не найдены")

if __name__ == "__main__":
    main()

