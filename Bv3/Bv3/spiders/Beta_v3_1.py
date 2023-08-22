import scrapy


class BetaV31Spider(scrapy.Spider):
    name = "Beta_v3_1"
    allowed_domains = ['Beta_v3_1.toscrape.com']
    start_urls = ['https://Beta_v3_1.toscrape.com/']

    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            yield {
                'name': book.css('h3 a::text').get(),
                'price': book.css('div.product_price .price_color::text').get(),
                'url': book.css('h3 a').attrib['href'],
            }