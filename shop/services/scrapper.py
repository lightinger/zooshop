# import requests
# from selectolax.parser import HTMLParser
# from concurrent.futures import ThreadPoolExecutor
# import threading
#
# STATIC_URL = 'https://masterzoo.ua'
# base_url = "https://masterzoo.ua/ua/catalog/koti/korm-dlya-kotv/"
# page_number = 1
#
# # Замените 'Your-User-Agent-String' на фактический User-Agent вашей системы
# headers = {'User-Agent': 'Your-User-Agent-String'}
#
# # Создаем блокировку для управления доступом к выводу
# output_lock = threading.Lock()
#
# def get_product_links(page_url):
#     response = requests.get(page_url, headers=headers)
#     if response.status_code == 200:
#         html = response.text
#         parser = HTMLParser(html)
#         links = parser.css(".catalogCard-image ")
#         product_links = [STATIC_URL + link.attributes.get("href") for link in links]
#         return product_links
#     else:
#         print(f"Ошибка при запросе страницы. Код состояния: {response.status_code}")
#         return []
#
# def process_product_link(product_link):
#     try:
#         product_response = requests.get(product_link, headers=headers)
#         product_html = product_response.text
#         product_parser = HTMLParser(product_html)
#
#         product_title = product_parser.css_first("h1").text()
#         product_price = product_parser.css_first(".product-price__item").text(strip=True)
#         product_old_price = product_parser.css_first(".product-price__old-price").text(strip=True)
#
#         with output_lock:
#             print("Название товара:", product_title)
#             print("цена товара:", product_price)
#             print("старая цена товара:", product_old_price)
#             print('*' * 100)
#     except Exception as error:
#         print(f"Ошибка при запросе товара по ссылке {product_link}: {error}")
#
#
# while True:
#     page_url = f"{base_url}?page={page_number}"
#     product_links = get_product_links(page_url)
#
#     if not product_links:
#         break
#
#     with ThreadPoolExecutor(max_workers=10) as executor:
#         executor.map(process_product_link, product_links)
#
#     page_number += 1

import re
import requests
from django.db import transaction
from selectolax.parser import HTMLParser
from anyascii import anyascii
from django.utils.text import slugify
from shop.models import Product, Image

@transaction.atomic
def write_to_db(data: dict) -> None:
    product, _ = Product.objects.get_or_create(
        slug=f"{slugify(anyascii(data['Title']))}",
        defaults={
            'title': data['Title'],
            'price': data['Price'],
            'old_price': data['Old price'],
            'article': data['Article']
        }
    )


def scrape_product_data(base_url: str):
    try:
        product_response = requests.get(base_url)
        product_response.raise_for_status()
        product_html = product_response.text
        product_parser = HTMLParser(product_html)

        title = product_parser.css_first("h1").text()
        price = product_parser.css_first(".product-price__item").text(strip=True).replace("грн", "").strip()
        old_price = product_parser.css_first(".product-price__old-price").text(strip=True).replace("грн", "").strip()
        if not old_price:
            old_price = price
        product_article = product_parser.css_first(".product-header__code").text(strip=True)
        article_numbers = re.findall(r'\d+', product_article)
        article = ''.join(article_numbers)
        description = product_parser.css_first('.text').text(strip=True)

        return {
            'Title': title,
            'Price': price,
            'Old price': old_price,
            'Article': article,
            'Description': description
        }
    except Exception as error:
        print(f"Ошибка при запросе товара по ссылке {base_url}: {error}")
        return None


def main():
    base_url = "https://masterzoo.ua/ua/sukhiy-korm-dlya-doroslikh-vibaglivikh-kotiv-savory-400-g-indichka-ta-kachka/"
    product_data = scrape_product_data(base_url)
    if product_data:
        write_to_db(product_data)


if __name__ == "__main__":
    main()


