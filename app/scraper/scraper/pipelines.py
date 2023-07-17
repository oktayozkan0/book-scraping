from itemadapter import ItemAdapter
import pymongo
from os import environ

class ScraperPipeline:
    def process_item(self, item, spider):
        return item

class MongoPipeline:

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = "mongodb://apiuser:apipass@mongodb:27017/test"
        self.mongo_db = environ.get("MONGO_DB")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DB"),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[spider.name].insert_one(ItemAdapter(item).asdict())
        return item
