import re
import threading
from concurrent.futures import ThreadPoolExecutor
from http import HTTPStatus

import requests
from django.db import transaction
from selectolax.parser import HTMLParser
from anyascii import anyascii
from django.utils.text import slugify
from shop.models import Product, Image, Category

STATIC_URL = 'https://masterzoo.ua'
base_url = "https://masterzoo.ua/ua/catalog/koti/posud-dlya-kotiv/"
output_lock = threading.Lock()
page_number = 1

def get_product_links(page_url):
    response = requests.get(page_url)
    if response.status_code == 200:
        html = response.text
        parser = HTMLParser(html)
        links = parser.css(".catalogCard-image ")
        product_links = [STATIC_URL + link.attributes.get("href") for link in links]
        return product_links
    else:
        print(f"Ошибка при запросе страницы. Код состояния: {response.status_code}")
        return []


def process_product_link(product_link):
    try:
        product_response = requests.get(product_link)
        product_html = product_response.text
        product_parser = HTMLParser(product_html)

        product_title = product_parser.css_first('.product-title')
        title = product_title.text()
        price = product_parser.css_first(".product-price__item").text(strip=True).replace("грн", "").strip().replace(" ", "")
        old_price_element = product_parser.css_first(".product-price__old-price")
        if old_price_element:
            old_price = old_price_element.text(strip=True).replace("грн", "").strip().replace(" ", "")
        else:
            old_price = price
        product_article = product_parser.css_first(".product-header__code").text(strip=True)
        article_numbers = re.findall(r'\d+', product_article)
        article = ''.join(article_numbers)[:10].zfill(10)
        description = product_parser.css_first('.text').text(strip=True).replace("\u00A0'", "")
        categories = product_parser.css('.breadcrumbs span')
        if categories:
            categories = [category.text(strip=True) for category in categories]
        img = product_parser.css('.gallery__photo-img')
        if img:
            img = {i.attributes['src'] for i in img if
                   i.attributes['src'].startswith('/content')}
            images = [STATIC_URL + image for image in img]

        with output_lock:
            print("Название товара:", title)
            print("Цена товара:", price)
            print("Старая цена товара:", old_price)
            print("Артикул:", article)
            print("Описание:", description)
            print("Фото:", images)
            # print(categories)
            print('*' * 100)

            write_to_db({
                'Title': title,
                'Price': price,
                'Old price': old_price,
                'Article': article,
                'Description': description,
                'Categories': categories,
                'Image': images,
            })

    except Exception as error:
        print(f"Ошибка при запросе товара по ссылке {product_link}: {error}")


def upload_images(images: list[str], product: Product) -> None:
    for i, image in enumerate(images, start=1):
        with requests.Session() as session:
            response = session.get(image)
            assert response.status_code == HTTPStatus.OK, 'Wrong status code'

        with open(f'media/images/product/{product.slug}-{i}.jpg', 'wb') as file:
            file.write(response.content)

        Image.objects.create(
            product=product,
            image=f'images/product/{product.slug}-{i}.jpg',
            url=image,
        )


@transaction.atomic
def write_to_db(data: dict) -> None:
    product, _ = Product.objects.get_or_create(
        slug=f"{slugify(data['Title'], allow_unicode=False)}",
        defaults={
            'title': data['Title'],
            'price': data['Price'],
            'old_price': data['Old price'],
            'article': data['Article'],
            'description': data['Description'],
        }
    )
    for category in data['Categories']:
        category, _ = Category.objects.get_or_create(
            slug=f"{slugify(category, allow_unicode=False)}",
            defaults={
                'title': category}
        )
        product.categories.add(category)

    if data['Image']:
        upload_images(data['Image'], product)


def main():
    global page_number
    while True:
        page_url = f"{base_url}?page={page_number}"
        product_links = get_product_links(page_url)

        if not product_links:
            break

        with ThreadPoolExecutor(max_workers=3) as executor:
            executor.map(process_product_link, product_links)

        page_number += 1

if __name__ == "__main__":
    main()