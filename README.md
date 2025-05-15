# QA Portfolio Project

🚀 **Цель**: Практика ручного и автоматизированного тестирования

## 📂 Структура
- `manual-testing/` - Баг-репорты и тест-кейсы
- `api-testing/` - Тесты для REST API
- `ui-testing/` - Автотесты на Selenium/Playwright

## 🛠 Как запустить автотесты
```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск тестов
pytest ui-testing/selenium-python/ --alluredir=allure-results
```
## 🚀 Запуск нагрузочных тестов
```bash
locust -f load-testing/locustfile.py

## 🏆 Проекты для тестирования
| Проект         | Тип тестирования | Ссылка                |
|----------------|------------------|-----------------------|
| DemoQA         | Ручное           | https://demoqa.com    |
| ReqRes         | API              | https://reqres.in     |
| Saucedemo      | UI-автотесты     | https://saucedemo.com |

## 📈 Статистика
- Найдено багов: 15
- Автотестов: 25
- Покрытие API: 80%
