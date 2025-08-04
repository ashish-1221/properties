import scrapy


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["web"]
    start_urls = ["https://web"]

    def parse(self, response):
        pass
