# Tasks API

## Описание

REST API для управления задачами с использованием Python, Django REST Framework и Postgres.

## Функционал

* Регистрация и аутентификация пользователей
* CRUD операции для задач
* Поиск и фильтрация задач
* Фоновая обработка задач с использованием Celery
* Генерация отчетов в PDF
* Импорт данных из CSV

## Установка

* Клонировать репозиторий
* Установить зависимости ``pip install -r requirements.txt``
* Настроить переменные окружения в ``.env``
* Запустить миграции ``python manage.py migrate``
* Запустить сервер ``python manage.py runserver``
  
## Использование
Документация API доступна по адресу ``http://localhost:8000/api/docs/``

Примеры запросов можно найти в Postman коллекции ``api_requests.json``

## Тестирование

``pytest``

## Деплой
* Настроить Nginx и Gunicorn
* Собрать статику ``python manage.py collectstatic``
* Переопределить Allowed Hosts и DEBUG в ``.env``
