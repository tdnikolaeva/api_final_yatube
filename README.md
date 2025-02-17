# Yatube API

## Описание

REST API для социальной сети Yatube. Предоставляет
функциональность для управления постами, группами,
комментариями и подписками. Позволяет создавать, читать,
обновлять и удалять контент,
а также взаимодействовать с другими пользователями.

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
## Примеры API запросов

### Посты (Posts)

*   **Получение списка постов:**

    ```
    GET /api/v1/posts/
    ```

    Возвращает список всех постов.

*   **Получение списка постов с пагинацией:**

    ```
    GET /api/v1/posts/?limit=10&offset=20
    ```

    Возвращает 10 постов, начиная с 21-го (смещение 20).

*   **Получение списка постов с фильтрацией:**

    ```
    GET /api/v1/posts/?search=example
    ```

    Возвращает посты, содержащие "example" в тексте или имени автора.

*   **Получение конкретного поста:**

    ```
    GET /api/v1/posts/{id}/
    ```

*   **Создание нового поста:**

    ```
    POST /api/v1/posts/
    Content-Type: application/json
    Authorization: Bearer <your_token>

    {
        "text": "Текст нового поста",
        "group": <id_группы>  // (опционально)
    }
    ```

*   **Обновление поста (PUT или PATCH):**

    ```
    PUT /api/v1/posts/{id}/
    Content-Type: application/json
    Authorization: Bearer <your_token>

    {
        "text": "Новый текст поста",
        "group": <id_группы>  // (опционально)
    }
    ```

*   **Удаление поста:**

    ```
    DELETE /api/v1/posts/{id}/
    Authorization: Bearer <your_token>
    ```

### Комментарии (Comments)

*   **Получение списка комментариев к посту:**

    ```
    GET /api/v1/posts/{post_id}/comments/
    ```

*   **Получение списка комментариев с фильтрацией:**

    ```
    GET /api/v1/posts/{post_id}/comments/?search=example
    ```

    Возвращает комментарии, содержащие "example" в тексте или имени автора.

*   **Получение конкретного комментария:**

    ```
    GET /api/v1/posts/{post_id}/comments/{id}/
    ```

*   **Создание нового комментария:**

    ```
    POST /api/v1/posts/{post_id}/comments/
    Content-Type: application/json
    Authorization: Bearer <your_token>

    {
        "text": "Текст комментария"
    }
    ```

*   **Обновление комментария (PUT или PATCH):**

    ```
    PUT /api/v1/posts/{post_id}/comments/{id}/
    Content-Type: application/json
    Authorization: Bearer <your_token>

    {
        "text": "Новый текст комментария"
    }
    ```

*   **Удаление комментария:**

    ```
    DELETE /api/v1/posts/{post_id}/comments/{id}/
    Authorization: Bearer <your_token>
    ```

### Подписки (Follows)

*   **Получение списка подписок текущего пользователя:**

    ```
    GET /api/v1/follow/
    Authorization: Bearer <your_token>
    ```

*   **Получение списка подписок с фильтрацией:**

    ```
    GET /api/v1/follow/?search=john
    Authorization: Bearer <your_token>
    ```

    Возвращает подписки, где имя пользователя или автора содержит "john".

*   **Создание новой подписки:**

    ```
    POST /api/v1/follow/
    Content-Type: application/json
    Authorization: Bearer <your_token>

    {
        "following": <id_пользователя, на которого подписываемся>
    }
    ```

*   **Удаление подписки:**

    ```
    DELETE /api/v1/follow/{id}/
    Authorization: Bearer <your_token>
    ```

### Группы (Groups)

*   **Получение списка групп:**

    ```
    GET /api/v1/groups/
    ```

*   **Получение конкретной группы:**

    ```
    GET /api/v1/groups/{id}/
    ```
    
