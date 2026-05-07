# Hybrid Scroll Spider — Scrapy + Playwright

Гибридный паук для сбора цитат с сайта с бесконечной лентой [quotes.toscrape.com/scroll](http://quotes.toscrape.com/scroll).

## Что делает

- Открывает страницу через Playwright
- Ждёт загрузки первой цитаты
- Скроллит страницу 5 раз со случайными паузами (имитация человека)
- Собирает текст цитаты, автора и теги
- Сохраняет результат в JSON/CSV через Item Feed

<<<<<<< HEAD
## Структура проекта
my_hybrid/
├── my_hybrid/          # исходный код
│   ├── spiders/        # пауки
│   ├── items.py        # модели данных
│   └── settings.py     # настройки
├── requirements.txt    # зависимости
├── .gitignore          # что не грузить на GitHub
├── README.md           # описание проекта
└── venv/               # виртуальное окружение (не в Git)

## Пример вывода
{"text": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”", "author": "Albert Einstein"},
{"text": "“It is our choices, Harry, that show what we truly are, far more than our abilities.”", "author": "J.K. Rowling"},
{"text": "“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”", "author": "Albert Einstein"},
{"text": "“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”", "author": "Jane Austen"},
{"text": "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”", "author": "Marilyn Monroe"}

=======
>>>>>>> 71d78e057f41789dcc9bf7c1a58617eacd5e88cf
## Стек

- Python 3.x
- Scrapy
- Scrapy Playwright
- Playwright

<<<<<<< HEAD
```bash
# 1. Клонируем проект
git clone https://github.com/NikolayDom/hybrid_scraper
cd my_hybrid

# 2. Создаём виртуальное окружение и активируем
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Mac/Linux

# 3. Устанавливаем зависимости
pip install -r requirements.txt
playwright install

# 4. Запускаем паука
scrapy crawl hybrid -o quotes.json
```
=======
# Установка зависимостей

pip install scrapy scrapy-playwright
playwright install

# Запуск паука

scrapy crawl quotes_scroll -o quotes.json
>>>>>>> 71d78e057f41789dcc9bf7c1a58617eacd5e88cf

## Ключевые навыки

- Гибридный парсинг (Scrapy + Playwright)
- Обход бесконечной ленты (скролл)
- Случайные задержки (анти-бан)
- Вынесение логики в отдельные методы
- Чистый код, переиспользуемая архитектура