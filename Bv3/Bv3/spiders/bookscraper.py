
import scrapy


class BookscraperSpider(scrapy.Spider):
    name = "bookscraper"
    allowed_domains = ["bookscraper.py"]
    start_urls = ["https://bookscraper.py"]

    def parse(self, response):
        pass
