import json
import random
from time import sleep

import requests
from bs4 import BeautifulSoup


with open('persons_url_list.txt') as file:

    lines = [line.strip() for line in file.readlines()]

    data_dict = []
    count = 0

    for line in lines:
        q = requests.get(line)
        result = q.content

        soup = BeautifulSoup(result, 'lxml')
        person = soup.find(class_='bt-biografie-name').find('h3').text
        person_name_company = person.strip().split(',')
        person_name = person_name_company[0]
        person_company = person_name_company[1].strip()

        social_networks = soup.find_all(class_='bt-link-extern')

        social_networks_urls = []
        for item in social_networks:
            social_networks_urls.append(item.get('href'))

        data = {
            'person_name': person_name,
            'company_name': person_company,
            'social_networks': social_networks_urls
        }
        count += 1
        sleep(random.randrange(2, 4))
        print(f'#{count}: {line} is done!')

        data_dict.append(data)

        with open('data.json', 'w') as json_file:
            json.dump(data_dict, json_file, indent=4)
