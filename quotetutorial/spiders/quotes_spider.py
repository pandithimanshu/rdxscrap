import scrapy

from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    token = ""
    url = ""

    def __init__(self, url='',key='', **kwargs):
        QuoteSpider.token = key
        QuoteSpider.url = url

        self.start_urls = [f'{url}']
        super().__init__(**kwargs)

    def parse(self,response):

        items = QuotetutorialItem()

        title = response.css('title::text').extract()

        items["title"] = title
        items["token"] = QuoteSpider.token
        items["url"] = QuoteSpider.url
        yield items


