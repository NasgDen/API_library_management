# Дипломный проект - API для управления библиотекой. 

## Описание
Разработан REST API для управления библиотекой. API предоставляет возможности для управления книгами, авторами и пользователями, а также для отслеживания выдачи книг пользователям. Для реализации API использовать Django Rest Framework (DRF).
Проект написан на языке программирования Python с помощью фреймворка Django и инструмента Django REST framework.
Фреймворк Django - это набор инструментов, библиотек и правил, которые помогают разработчикам создавать приложения, упрощая и ускоряя процесс разработки. Фреймворк предоставляет структуру, внутри которой можно разрабатывать веб-приложения.
Django использует шаблон проектирования MTV (Model — Template — View).
Django REST framework (DRF) — это библиотека для Python, которая является надстройкой над веб-фреймворком Django и предназначена для создания RESTful API (интерфейсов прикладного программирования). Она предоставляет набор мощных и гибких инструментов, таких как сериализаторы, наборы представлений и аутентификация, которые значительно упрощают разработку и развертывание веб-сервисов, позволяя внешним приложениям взаимодействовать с Django-приложением.

### В проекте использованы следующие зависимости:
1. Django v6.0 - [Официальный сайт](https://djangoproject.com), [GitHub](https://github.com/django/django)
2. Django Rest Framework - [Официальный сайт](http://django-rest-framework.org), [GitHub](https://github.com/encode/django-rest-framework)
3. Python-dotenv [GitHub](https://github.com/theskumar/python-dotenv)
4. Psycopg2 - [Официальный сайт](https://psycopg.org), [GitHub](https://github.com/psycopg/psycopg2)
5. Django Rest Framework simplejwt - [Документация](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/), [GitHub](https://github.com/jazzband/djangorestframework-simplejwt)
6. Django-filter - [Документация](https://django-filter.readthedocs.io/en/stable/), [GitHub](https://github.com/carltongibson/django-filter/tree/main)
7. Drf-spectacular - [Документация](https://drf-spectacular.readthedocs.io/en/latest/), [GitHub](https://github.com/tfranzel/drf-spectacular)
8. Gunicorn - [Официальный сайт](https://gunicorn.org/), [GitGub](https://github.com/benoitc/gunicorn)
9. Django-cors-headers - [GitHub](https://github.com/adamchainz/django-cors-headers)
10. Pillow - [Документация](https://pillow.readthedocs.io/en/stable/), [GitHub](https://github.com/python-pillow/Pillow)
11. Drf-api-logger - [GitHub](https://github.com/vishalanandl177/DRF-API-Logger)


## Описание Моделей
Приложение library_management - модуль моделей models.py:
1. Author - Описание полей модель - Авторы.
2. Book - Описание полей модель - Книги.
3. BookIssuance - Описание полей модель - Выдача книги.

Приложение users - модуль моделей models.py:
1. User - Описание полей модель - Пользователь.

## Описание Контроллеров
Приложение library_management - модуль контроллеров view.py:
### CRUD операции для модели Book - Книга:
1. BookCreateApiView - Класс реализует интерфейс для создания книги на основе generics.
2. BookListApiView - Класс реализует интерфейс для вывода списка всех книг на основе generics.
3. BookUpdateApiView - Класс реализует интерфейс для изменения данных о книге на основе generics.
4. BookRetrieveAPIView - Класс реализует интерфейс для отображения данных об одной книге на основе generics.
5. BookDestroyApiView - Класс реализует интерфейс для удаления данных о книге на основе generics.
### CRUD операции для модели Author - Автор:
1. AuthorCreateApiView - Класс реализует интерфейс для создания автора на основе generics.
2. AuthorListApiView - Класс реализует интерфейс для вывода списка всех авторов на основе generics.
3. AuthorUpdateApiView - Класс реализует интерфейс для изменения данных об авторе на основе generics.
4. AuthorRetrieveAPIView - Класс реализует интерфейс для отображения данных об одном авторе на основе generics.
5. AuthorDestroyApiView - Класс реализует интерфейс для удаления данных об авторе на основе generics.

Приложение users - модуль контроллеров view.py:
### CRUD операции для модели User - Автор:
1. UserCreateApiView - Класс реализует интерфейс для создания пользователя на основе generics.
2. UserListApiView - Класс реализует интерфейс для вывода списка всех пользователей на основе generics.
3. UserUpdateApiView - Класс реализует интерфейс для изменения данных о пользователе на основе generics.
4. UserRetrieveAPIView - Класс реализует интерфейс для отображения данных об одном пользователе на основе generics.
5. UserDestroyApiView - Класс реализует интерфейс для удаления данных о пользователе на основе generics.

## Установка проекта локально

1. Клонируйте репозиторий:
```
git clone https://github.com/NasgDen/API_library_management
```
2. В PyCharm установите менеджер проекта poetry.
3. В PyCharm устанавливаем все зависимости проекта из файла pyproject.toml
4. Переименуйте файл .env.sample в .env. Заполните файл конфигурации .env параметрами.

## Использование проекта локально:

1. В терминале введите: python manage.py runserver
2. Сервер запускается по адресу: 127.0.0.1:8000
3. Используйте postman для создания и отправки HTTP-запросов к серверу (GET, POST, PUT, DELETE и др.) и анализ их ответов.

## Запуск приложения с помощью Docker локально

1. Установите Docker по ссылке https://www.docker.com/products/docker-desktop/
2. Запустите установленный Docker.
3. Для создания многоконтейнерного приложения используйте Docker Compose.
4. Для сборки контейнеров и последующего запуска всех сервисов выполните команду:
    ```
    docker compose up --build
    ```
5. Для проверки запущенных контейнеров выполните команду:
    ```
    docker ps
    ```
6. Сервер запущен по адресу 127.0.0.1:8000 (localhost:8000)
7. Для просмотра документации по приложению в браузере введите следующий адрес:
    ```
    127.0.0.1:8000/swagger-ui/
    
    ```
    или
    ```
    127.0.0.1:8000/redoc/
    ```
8. Для остановки всех запущенных сервисов выполните команду:
    ```
    docker compose down
    ```

## CI/CD (Continuous Integration/Continuous Delivery)

Это методология DevOps, которая автоматизирует процессы сборки, тестирования и развертывания кода для ускорения и повышения надежности разработки программного обеспечения.
CI/CD описан в файле ci.yml (папка .github/workflows).
При каждом push и pull-request на git hub репозиторий происходит проверка кода линтером flake8, далее происходит блок тестирования кода. 
После успешных проверок происходит автоматическое развертывание и запуск приложения на сервере.
Все переменные проекта должны быть указаны в git hub secrets.
Проект доступен на сервере 158.160.194.250.\
Документация API:\
http://158.160.194.250/api/redoc/ \
или\
http://158.160.194.250/api/swagger-ui/

## Тестирование:
В проекте проводились тестирование CRUD операций для всех моделей с помощью APITestCase фреймворка DjangoRestFramework.

## Лицензия

Этот проект лицензирован по [лицензии MIT](http://www.opensource.org/licenses/mit-license.php).
