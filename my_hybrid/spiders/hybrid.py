import scrapy
from scrapy_playwright.page import PageMethod
import random

class MySpider(scrapy.Spider):
    name = "hybrid"

    def start_requests(self):
        url = "http://quotes.toscrape.com/scroll"
        yield scrapy.Request(
            url,
            meta={
                "playwright": True,
                "playwright_page_methods": 
                [
                    action
                    for _ in range(5)
                    for action in (
                        PageMethod("wait_for_selector", ".quote", timeout=10000),
                        PageMethod("evaluate", "window.scrollTo(0, document.body.scrollHeight)"),
                        PageMethod("wait_for_timeout", 2000),
                    )
                ],
            },
            callback=self.parse,
        )

    def parse(self, response):
        quotes = response.css(".quote")
        for q in quotes:
            yield{
                "text": q.css(".text::text").get(),
                "author": q.css(".author::text").get(),
            }
    