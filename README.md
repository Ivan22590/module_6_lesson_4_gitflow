# FastAPI Time Server

Простой тестовый бэкенд на FastAPI, возвращающий текущее время сервера.

## Установка

1. Создайте виртуальное окружение:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Установите зависимости:
```powershell
pip install -r requirements.txt
```

## Запуск

```powershell
.venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8001 --reload
```

## Эндпоинты

| Метод | Путь | Описание |
|-------|------|----------|
| GET | `/` | Приветственное сообщение |
| GET | `/time` | Текущее время сервера |
| GET | `/date` | Текущая дата сервера |

### Пример ответа `/time`:
```json
{
  "server_time": "2026-10-12 14:41:29",
  "iso": "2026-10-12T14:41:29.208071",
  "timezone": "local"
}
```

### Пример ответа `/date`:
```json
{
  "server_date": "2026-10-12",
  "iso": "2026-10-12",
  "day_of_week": "Monday"
}
```

## Docker

### Сборка образа:
```powershell
docker build -t time-server .
```

### Запуск контейнера:
```powershell
docker run -p 8001:8001 time-server
```

## CI/CD

Workflow автоматически собирает Docker-образ, публикует его в GitHub Container Registry (GHCR) и деплоит на удалённый сервер по SSH.

### Необходимые секреты

В настройках репозитория (**Settings → Secrets and variables → Actions**) добавьте:

| Секрет | Описание |
|--------|----------|
| `SSH_HOST` | Адрес удалённого сервера |
| `SSH_USER` | Пользователь для SSH-подключения |
| `SSH_KEY` | Приватный SSH-ключ |
| `SSH_PORT` | (опционально) Порт SSH, по умолчанию `22` |

> **Примечание:** `GITHUB_TOKEN` предоставляется GitHub автоматически — добавлять его не нужно.

### Требования к серверу

На удалённом сервере должны быть установлены:
- Docker
- Docker должен быть доступен от имени пользователя `SSH_USER`

### Триггеры

Workflow запускается:
- При пуше в ветку `main`
- Вручную через **Actions → Build and Deploy → Run workflow**
