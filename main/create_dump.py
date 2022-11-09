"""
Нужно запустить этот скрипт, чтобы получить файл txt со ссылками, откуда будем
вытягивать нужную нам информацию. Файл создаем для того, чтобы не отправлять
большое количество запросов сайту, т.к. это чревато блокировкой доступа.
"""
import requests
from bs4 import BeautifulSoup


persons_url_list = []

for i in range(0, 760, 20):
    url = f'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}'

    q = requests.get(url)
    result = q.content

    soup = BeautifulSoup(result, 'lxml')
    persons = soup.find_all('a')

    for person in persons:
        person_page_url = person.get('href')
        persons_url_list.append(person_page_url)

with open('persons_url_list.txt', 'a') as file:
    for line in persons_url_list:
        file.write(f'{line}\n')
