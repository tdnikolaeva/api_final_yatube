# Yatube API

## Описание

Этот проект представляет собой REST API для социальной сети Yatube.
Он позволяет пользователям создавать, читать,
обновлять и удалять публикации и комментарии. Авторизованные
пользователи также могут подписываться на других пользователей.

## Запуск проекта

1.  Клонируйте репозиторий и перейдите в него в командной строке:

    ```
    git clone https://github.com/tdnikolaeva/api_final_yatube
    cd https://github.com/tdnikolaeva/api_final_yatube
    ```


2.  Создайте и активируйте виртуальное окружение:

    ```
    python3 -m venv venv
    source venv/bin/activate   # Для Linux/macOS
    # venv\Scripts\activate  Для Windows
    ```

3.  Установите зависимости из файла `requirements.txt`:

    ```
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

4.  Выполните миграции:

    ```
    python3 manage.py migrate
    ```

5.  Создайте суперпользователя при необходимости:

    ```
    python3 manage.py createsuperuser
    ```

6.  Запустите проект:

    ```
    python3 manage.py runserver
    ```

