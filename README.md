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

### Пример ответа `/time`:
```json
{
  "server_time": "2026-10-12 14:41:29",
  "iso": "2026-10-12T14:41:29.208071",
  "timezone": "local"
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
