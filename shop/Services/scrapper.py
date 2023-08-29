import requests
from selectolax.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
import threading

STATIC_URL = 'https://masterzoo.ua'
base_url = "https://masterzoo.ua/ua/catalog/koti/korm-dlya-kotv/"
page_number = 1

# Замените 'Your-User-Agent-String' на фактический User-Agent вашей системы
headers = {'User-Agent': 'Your-User-Agent-String'}

# Создаем блокировку для управления доступом к выводу
output_lock = threading.Lock()

def get_product_links(page_url):
    response = requests.get(page_url, headers=headers)
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
        product_response = requests.get(product_link, headers=headers)
        product_html = product_response.text
        product_parser = HTMLParser(product_html)

        product_title = product_parser.css_first("h1").text()
        product_price = product_parser.css_first(".product-price__item").text(strip=True)
        product_old_price = product_parser.css_first(".product-price__old-price").text(strip=True)

        with output_lock:
            print("Название товара:", product_title)
            print("цена товара:", product_price)
            print("старая цена товара:", product_old_price)
            print('*' * 100)
    except Exception as error:
        print(f"Ошибка при запросе товара по ссылке {product_link}: {error}")


while True:
    page_url = f"{base_url}?page={page_number}"
    product_links = get_product_links(page_url)

    if not product_links:
        break

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_product_link, product_links)

    page_number += 1