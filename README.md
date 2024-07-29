# TASHBULATOV_MAY2002

## Тестирование интернет-магазина "Дикий сбор"

## ШАГИ
1. Склонировать проект https://github.com/alfredtashbulatov/tasbulatov_2may2002.git

2. Установить зависимости

4. Запустить тесты с указанием пути к директории результатов тестирования pytest pytest --alluredir allure-result

5. Сформировать отчет allure serve allure-results

### Стек:
- pytest
- selenium
- requests
- allure

### Структура 
- ./test - тесты 
  - test_api.py - Api тесты
  - test_ui.py - Ui тесты
  - conftest.py - Файл с фикстурами
  - pytest.ini - файл с настройками pytest
 - User_api.py - Методы для Аpi тестов
 - Main_page.py - Методы для UI тестов

### Библиотеки
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install requests
- pip install allure
- pip install json

### Запуск тестов 
- pytest (Запуск всех тестов )
- pytest - m api (Запуск api тестов )
- pytest - m ui (Запуск ui тестов )
- python -m pytest --alluredir allure-result (Запустить тесты с указанием пути к каталогу результатов тестирования)
- allure serve allure-result (Запустить Allure и конвертирует результаты теста в отчет)

