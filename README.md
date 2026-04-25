# Hybrid Scroll Spider — Scrapy + Playwright

Гибридный паук для сбора цитат с сайта с бесконечной лентой [quotes.toscrape.com/scroll](http://quotes.toscrape.com/scroll).

## Что делает

- Открывает страницу через Playwright
- Ждёт загрузки первой цитаты
- Скроллит страницу 5 раз со случайными паузами (имитация человека)
- Собирает текст цитаты, автора и теги
- Сохраняет результат в JSON/CSV через Item Feed

## Стек

- Python 3.x
- Scrapy
- Scrapy Playwright
- Playwright

# Установка зависимостей

pip install scrapy scrapy-playwright
playwright install

# Запуск паука

scrapy crawl quotes_scroll -o quotes.json

## Ключевые навыки

- Гибридный парсинг (Scrapy + Playwright)
- Обход бесконечной ленты (скролл)
- Случайные задержки (анти-бан)
- Вынесение логики в отдельные методы
- Чистый код, переиспользуемая архитектура