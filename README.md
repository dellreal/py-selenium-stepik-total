# **Автоматизация тестирования с помощью Selenium и Python**

# Final step (4.3.15)

## Руководство по использованию репозитория

При работе с виртуальным окружением необходимо выполнить следующие команды:

на Windows:

`$ python -m venv .venv`

`$ .venv/scripts/activate`

на Linux/MacOS:

`$ python3 -m venv .venv`

`$ source .venv/bin/activate`

Установка зависимостей:

`$ pip install -r requirements.txt`

Если виртуальное окружение не используется, то необходимо выполнить только команду установки зависимостей.

Для запуска тестов выполнить команду:

`$ pytest -v --tb=line --language=en -m need_review`