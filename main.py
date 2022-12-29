from bs4 import BeautifulSoup
import requests
from requests import get
import lxml


# Получаем разметку

url = 'https://mail.ru/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_='news__list__item news__list__item_main')
print(soup)

# Читаем заголовки новостей

for quote in quotes:
    print(quote.text)


# # Проверяем, какой headers передается
# for key, value in response.request.headers.items():
#     print(key+": "+value)
#
