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

## Структура проекта

\`\`\`
my_hybrid/
├── my_hybrid/
│   ├── spiders/
│   │   └── quotes_scroll.py   # Паук
│   └── settings.py            # Настройки (Playwright + Twisted Reactor)
├── scrapy.cfg
└── README.md
\`\`\`

## Запуск

\`\`\`bash
# Установка зависимостей
pip install scrapy scrapy-playwright
playwright install

# Запуск паука
scrapy crawl quotes_scroll -o quotes.json
\`\`\`

## Результат

100 цитат с текстом, автором и тегами. Пример:

\`\`\`json
{
  "text": "The world as we have created it...",
  "author": "Albert Einstein",
  "tags": ["change", "deep-thoughts", "world"]
}
\`\`\`

## Ключевые навыки

- Гибридный парсинг (Scrapy + Playwright)
- Обход бесконечной ленты (скролл)
- Случайные задержки (анти-бан)
- Вынесение логики в отдельные методы
- Чистый код, переиспользуемая архитектура