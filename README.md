## Тестовое задание в компанию "Безопасность Он-лайн"

Сервис по управлению задачами внутри компании

### 1. Стек технологий:

- Python 3.11.2
- Django 5.0.6
- DRF 3.15.0

### 2. Как скопировать проект:

```bash
git clone https://github.com/mulphers/drf_company_manager.git
```

### 3. Env-файл:

Переименуйте файл .env_example в .env и заполните его

```
SECRET_KEY=your_secret_key

DEBUG=your_debug_mode

DATABASE_HOST=your_database_host
DATABASE_PORT=your_database_port
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_NAME=your_database_name
```

### 4. Запуск проекта:

Перейдите в Вашу рабочую директорию и введите команду

```bash
docker-compose up
```

### 5. База данных:

Вы можете управлять базой данных перейдя по ссылке

```bash
http://127.0.0.1:8080
```

## 6. Эндпоинты:

### 1. Создание сотрудника

- **Маршрут:** `http://127.0.0.1:8000/api/v1/employee/create/`
- **Описание:** Создает нового сотрудника.
- **Тип запроса:** POST
- **Заголовки:**
    - Нет
- **Параметры:**
    - `username` (строка): Имя сотрудника.
    - `email` (строка): Электронная почта сотрудника.
    - `phone_number` (строка): Мобильный телефон сотрудника.
    - `password` (строка): Пароль сотрудника.
- **Скриншоты из Postman:**
    - **Заголовки:**
      ![1_headers](https://github.com/mulphers/drf_company_manager/blob/master/images/1_headers.png)
    - **Параметры:**
      ![1_body](https://github.com/mulphers/drf_company_manager/blob/master/images/1_body.png)
    - **Ответ:**
      ![1_response](https://github.com/mulphers/drf_company_manager/blob/master/images/1_response.png)

### 2. Генерация токена

- **Маршрут:** `http://127.0.0.1:8000/api/v1/token/`
- **Описание:** Генерирует токен аутентификации для сотрудника.
- **Тип запроса:** POST
- **Заголовки:**
    - Нет
- **Параметры:**
    - `username` (строка): Имя сотрудника.
    - `password` (строка): Пароль сотрудника.
- **Скриншоты из Postman:**
    - **Заголовки:**
      ![2_headers](https://github.com/mulphers/drf_company_manager/blob/master/images/2_headers.png)
    - **Параметры:**
      ![2_body](https://github.com/mulphers/drf_company_manager/blob/master/images/2_body.png)
    - **Ответ:**
      ![2_response](https://github.com/mulphers/drf_company_manager/blob/master/images/2_response.png)

### 3. Обновление токена

- **Маршрут:** `http://127.0.0.1:8000/api/v1/token/refresh/`
- **Описание:** Обновляет токен аутентификации.
- **Тип запроса:** POST
- **Заголовки:**
    - Нет
- **Параметры:**
    - `refresh` (строка): Токен обновления.
- **Скриншоты из Postman:**
    - **Заголовки:**
      ![3_headers](https://github.com/mulphers/drf_company_manager/blob/master/images/3_headers.png)
    - **Параметры:**
      ![3_body](https://github.com/mulphers/drf_company_manager/blob/master/images/3_body.png)
    - **Ответ:**
      ![3_response](https://github.com/mulphers/drf_company_manager/blob/master/images/3_response.png)

### 4. Текущий сотрудник

- **Маршрут:** `http://127.0.0.1:8000/api/v1/employee/current/`
- **Описание:** Получает данные текущего аутентифицированного сотрудника.
- **Тип запроса:** GET
- **Заголовки:**
    - `Authorization` (строка): Токен авторизации.
- **Параметры:**
    - Нет
- **Скриншоты из Postman:**
    - **Заголовки:**
      ![4_headers](https://github.com/mulphers/drf_company_manager/blob/master/images/4_headers.png)
    - **Параметры:**
      ![4_body](https://github.com/mulphers/drf_company_manager/blob/master/images/4_body.png)
    - **Ответ:**
      ![4_response](https://github.com/mulphers/drf_company_manager/blob/master/images/4_response.png)

### 5. Все задачи

- **Маршрут:** `http://127.0.0.1:8000/api/v1/task/all/`
- **Описание:** Для пользователя со статусом CUS будут получены все созданные им задания.
  Для пользователя со статусом EXC будут получены все задания без назначенного исполнителя.
  Для пользователя с доступом ко всем заданиям буду получены абсолютно все задания.
- **Тип запроса:** GET
- **Заголовки:**
    - `Authorization` (строка): Токен авторизации.
- **Параметры:**
    - Нет
- **Скриншоты из Postman:**
    - **Заголовки:**
      ![5_headers](https://github.com/mulphers/drf_company_manager/blob/master/images/5_headers.png)
    - **Параметры:**
      ![5_body](https://github.com/mulphers/drf_company_manager/blob/master/images/5_body.png)
    - **Ответ:**
      ![5_response](https://github.com/mulphers/drf_company_manager/blob/master/images/5_response.png)

### 6. Назначить задачу

- **Маршрут:** `http://127.0.0.1:8000/api/v1/task/assign/`
- **Описание:** Назначает задачу сотруднику.
- **Тип запроса:** POST
- **Заголовки:**
    - `Authorization` (строка): Токен авторизации.
- **Параметры:**
    - `task_id` (целое число): ID задачи.
- **Скриншоты из Postman:**
    - **Заголовки:**
      ![6_headers](https://github.com/mulphers/drf_company_manager/blob/master/images/6_headers.png)
    - **Параметры:**
      ![6_body](https://github.com/mulphers/drf_company_manager/blob/master/images/6_body.png)
    - **Ответ:**
      ![6_response](https://github.com/mulphers/drf_company_manager/blob/master/images/6_response.png)

### 7. Назначенные задачи

- **Маршрут:** `http://127.0.0.1:8000/api/v1/task/assigned/`
- **Описание:** Получает задачи, назначенные текущему аутентифицированному сотруднику.
- **Тип запроса:** GET
- **Заголовки:**
    - `Authorization` (строка): Токен авторизации.
- **Параметры:**
    - Нет
- **Скриншоты из Postman:**
    - **Заголовки:**
      ![7_headers](https://github.com/mulphers/drf_company_manager/blob/master/images/7_headers.png)
    - **Параметры:**
      ![7_body](https://github.com/mulphers/drf_company_manager/blob/master/images/7_body.png)
    - **Ответ:**
      ![7_response](https://github.com/mulphers/drf_company_manager/blob/master/images/7_response.png)

### 8. Создание задачи

- **Маршрут:** `http://127.0.0.1:8000/api/v1/task/create/`
- **Описание:** Создает новую задачу.
- **Тип запроса:** POST
- **Заголовки:**
    - `Authorization` (строка): Токен авторизации.
- **Параметры:**
    - `title` (строка): Заголовок задачи.
    - `description` (строка): Описание задачи.
- **Скриншоты из Postman:**
    - **Заголовки:**
      ![8_headers](https://github.com/mulphers/drf_company_manager/blob/master/images/8_headers.png)
    - **Параметры:**
      ![8_body](https://github.com/mulphers/drf_company_manager/blob/master/images/8_body.png)
    - **Ответ:**
      ![8_response](https://github.com/mulphers/drf_company_manager/blob/master/images/8_response.png)

### 9. Обновление задачи

- **Маршрут:** `http://127.0.0.1:8000/api/v1/task/update/`
- **Описание:** Обновляет существующую задачу.
- **Тип запроса:** POST
- **Заголовки:**
    - `Authorization` (строка): Токен авторизации.
- **Параметры:**
    - `task_id` (целое число): ID задачи для обновления.
    - `report` (файл): Отчет к заданию.
- **Скриншоты из Postman:**
    - **Заголовки:**
      ![9_headers](https://github.com/mulphers/drf_company_manager/blob/master/images/9_headers.png)
    - **Параметры:**
      ![9_body](https://github.com/mulphers/drf_company_manager/blob/master/images/9_body.png)
    - **Ответ:**
      ![9_response](https://github.com/mulphers/drf_company_manager/blob/master/images/9_response.png)

### 10. Закрытие задачи

- **Маршрут:** `POST http://127.0.0.1:8000/api/v1/task/close/`
- **Описание:** Закрывает задачу.
- **Тип запроса:** POST
- **Заголовки:**
    - `Authorization` (строка): Токен авторизации.
- **Параметры:**
    - `task_id` (целое число): ID задачи для закрытия.
- **Скриншоты из Postman:**
    - **Заголовки:**
      ![10_headers](https://github.com/mulphers/drf_company_manager/blob/master/images/10_headers.png)
    - **Параметры:**
      ![10_body](https://github.com/mulphers/drf_company_manager/blob/master/images/10_body.png)
    - **Ответ:**
      ![10_response](https://github.com/mulphers/drf_company_manager/blob/master/images/10_response.png)

## 7. Контакты исполнителя:

- Telegram: https://t.me/mulphers
- Email: alexanderdenisenya@gmail.com
