
# Загрузка данных в БД из файла csv

## Порядок установки и запуска

### Сборка

    docker-compose build

### Запуск

    docker-compose up

#### URL
    127.0.0.1:8000/app

GET запрос возвращает 5 клиентов которые потратили больше всего.

POST загружает файл .csv (строго) с данными.

В случае если файл не загружен или не соответствует формату: 
 - Ошибка - "Формат файла не .csv"

В случае если все корректно:
 - "Файл успешно загружен"



