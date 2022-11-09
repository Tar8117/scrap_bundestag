# scrap_bundestag
Tool for parsing https://www.bundestag.de/ for getting parliament members data.

Парсинг https://www.bundestag.de/ для получения данных всех членов парламента. 

* Склонируйте проект и откройте его
* Создайте и активируйте виртуальное окружение

    `python -m venv venv`

    `source venv/Scripts/activate`
    
* Установите зависимости из файла requirements.txt

    `python -m pip install -r requirements.txt`
* Запустите файл _create_dump_. Когда скрипт отработает, в той же директории
должен появиться файл _persons_url_list.txt_.
* Запустите файл _parse_data_. Подождите некоторое время. После завершения скрипта,
в той же директории появится файл _data.json_ с нужной нам информацией.


_Код актуален на 11.11.2022._