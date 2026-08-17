# Tender Tracker API

Микросервис для управления тендерами на FastAPI с Docker, PostgreSQL, Redis и CI/CD.

---

## 📌 Описание проекта

Это тестовое задание для компании Crown. Проект демонстрирует:

- Разработку REST API на FastAPI
- Контейнеризацию с помощью Docker
- Оркестрацию контейнеров через Docker Compose
- Настройку CI/CD с GitHub Actions
- Работу с PostgreSQL и Redis

---

## 🧠 Архитектура проекта

Проект состоит из трёх сервисов, каждый запускается в отдельном контейнере:

| Сервис | Назначение |
|--------|------------|
| **FastAPI App** | Основное приложение с REST API |
| **PostgreSQL** | База данных для хранения тендеров |
| **Redis** | Кеширование и брокер сообщений |

---

## ⚙️ Как запустить проект локально

### 1. Клонировать репозиторий

```bash
git clone https://github.com/ТВОЙ_НИК/fastapi-tender-tracker.git
cd fastapi-tender-tracker