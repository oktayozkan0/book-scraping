# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# pydantic might be better choice than scrapy items.
class ScraperItem(scrapy.Item):
    title = scrapy.Field()
    publisher = scrapy.Field()
    writers = scrapy.Field() # authors?
    price = scrapy.Field()
    url = scrapy.Field()
    query = scrapy.Field()
