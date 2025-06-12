## Описание

Автоматизированные тесты для проверки авторизациис использованием Python и Selenium WebDriver

Сайт: https://berpress.github.io/selenium-login-demo/

## Установка
1. Клонировать репозиторий:

git clone https://github.com/nOoBenok/selenium-test.git

2. Установить зависимость

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

## Запуск тестов

pytest -v tests/test_login.py
