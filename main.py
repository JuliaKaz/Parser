from bs4 import BeautifulSoup
import requests


product = input('Что ищем? ')
url = 'https://www.avito.ru/ekaterinburg?q=' + product
print(url)
request = requests.get(url)

bs = BeautifulSoup(request.text, 'html.parser')

all_links = bs.find_all('a', class_='title-root-zZCwT')
print(all_links)
for link in all_links:
    print('https://www.avito.ru' + link)
