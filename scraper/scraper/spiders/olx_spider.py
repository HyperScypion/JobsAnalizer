import scrapy


class OlxScrapper(scrapy.Spider):
    name = "olx"

    def start_requests(self):
        url = "https://olx.pl/praca"

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        pass
