# 🐾 Kittygram

[![Kittygram Deployment](https://github.com/ArtemYuvanov/kittygram_final/actions/workflows/kittygram_workflow.yml/badge.svg)](https://github.com/ArtemYuvanov/kittygram_final/actions/workflows/kittygram_workflow.yml)

Kittygram — социальная сеть для размещения фотографий домашних животных.  
Пользователи могут регистрироваться, загружать фото своих котов, делиться их достижениями и любоваться другими питомцами.

---

## 🚀 Технологии

- Python 3.9  
- Django 3.2.3  
- Django REST Framework 3.12.4  
- Djoser 2.1.0  
- PostgreSQL  
- Nginx  
- Gunicorn 20.1.0  
- Docker, Docker Compose  
- GitHub Actions  

---

## 📦 Установка и запуск проекта

### 1. Клонировать репозиторий
git clone https://github.com/ArtemYuvanov/kittygram_final.git
cd kittygram_final

### 2. Создать .env файл в корне проекта
SECRET_KEY=указать_секретный_ключ
ALLOWED_HOSTS=указать_IP_или_домен
POSTGRES_DB=kittygram
POSTGRES_USER=kittygram_user
POSTGRES_PASSWORD=kittygram_password
DB_NAME=kittygram
DB_HOST=db
DB_PORT=5432
DEBUG=False

### 3. Запустить проект в Docker-контейнерах
docker compose -f docker-compose.production.yml up -d

### 4. Выполнить миграции и собрать статику
docker compose -f docker-compose.production.yml exec backend python manage.py migrate
docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic --noinput
docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/

### 5. Создать суперпользователя
docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser

---

## ⚙️ CI/CD (финальное задание)

В проекте настроен автоматический деплой через GitHub Actions.

### Настройка CI/CD

1. В корне проекта создайте файл tests.yml со следующим содержанием:
repo_owner: ваш_логин_на_GitHub
kittygram_domain: https://домен_проекта_Kittygram
taski_domain: https://домен_проекта_Taski
dockerhub_username: ваш_логин_на_DockerHub

2. Скопируйте содержимое .github/workflows/main.yml в файл kittygram_workflow.yml в корне проекта.

3. Убедитесь, что:
   - Пуш в ветку main запускает workflow;
   - После успешного деплоя приходит сообщение в Telegram;
   - Проект развёрнут и доступен по доменному имени из tests.yml.

---

## 🧪 Локальный запуск автотестов
python -m venv venv
source venv/Scripts/activate
pip install -r backend/requirements.txt
pytest 

---

## 👨‍💻 Автор

GitHub: [@ArtemYuvanov](https://github.com/ArtemYuvanov)  
