# YaCut — Сократить ссылку

Сервис укорачивания ссылок.
Его назначение — ассоциировать длинную пользовательскую ссылку с короткой,
которую предлагает сам пользователь или предоставляет сервис.

### 🔥 Возможности

- Генерация коротких ссылок и связь их с исходными длинными ссылками.
- Переадресация на исходный адрес при обращении к коротким ссылкам.
- REST API

### Технологии

[![Flask][Flask-badge]][Flask-url]
[![SQLAlchemy][SQLAlchemy-badge]][SQLAlchemy-url]
[![Gunicorn][Gunicorn-badge]][Gunicorn-url]
[![Postgres][Postgres-badge]][Postgres-url]
[![Docker][Docker-badge]][Docker-url]
[![Nginx][Nginx-badge]][Nginx-url]

## ⚙ Начало Работы

Чтобы запустить локальную копию проекта, следуйте инструкциям ниже.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполните миграции
```
flask db upgrade
```

Запуск проекта
```
flask run
```

Автор
Муминова Мадина [https://github.com/madina-zvezda](https://github.com/muminova-madina)https://github.com/muminova-madina
