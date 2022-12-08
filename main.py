from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


#Фейковый юзер агент
ua = UserAgent()
headers = {'User-Agent': ua.chrome}

#Запрос
url = 'https://www.wildberries.ru/catalog/0/search.aspx?sort=popular&search=носки+женские'
response = requests.get(url, headers=headers)
print(response)
#Какой headers передается
for key, value in response.request.headers.items():
    print(key+": "+value)

#Текст из респонса
bs = BeautifulSoup(response.text, 'html.parser')
print(response.text)

#Ищет ссылки в тексте респонса
all_links = bs.find_all('a', class_='j-wba-footer-item')
print(all_links)
for link in all_links:
    print(link['href'])

