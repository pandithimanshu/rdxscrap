 # Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# from scrapy_djangoitem import DjangoItem
#
class QuotetutorialItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    token = scrapy.Field()
    url = scrapy.Field()
#
# from rdxscrap.app.models import Quote
#
# class QuotetutorialItem(DjangoItem):
#     """
#     Define a item based on django model BlogPost
#     """
#     django_model = Quote