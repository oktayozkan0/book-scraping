import scrapy
from urllib.parse import urlparse, parse_qs
from ..items import ScraperItem


class KitapsepetiSpider(scrapy.Spider):
    name = "kitapsepeti"
    main_url = "https://www.kitapsepeti.com"

    def __init__(self, query:str, name=None, **kwargs):
        self.query = query

    def start_requests(self):
        yield scrapy.Request(f"https://www.kitapsepeti.com/arama?q={self.query}&stock=1", callback=self.paging)

    def paging(self, response):
        last_page = response.xpath("((//div[contains(@class, 'productPager')])[1]/a/preceding-sibling::a)[last()]/text()").get()
        if last_page:
            for i in range(2, int(last_page)+1):
                url = f"https://www.kitapsepeti.com/arama?q={self.query}&stock=1&pg={i}"
                yield scrapy.Request(url=url, callback=self.get_books)

        yield scrapy.Request(
            url="http://",
            meta={
                "first_page": True,
                "html": response.text
            },
            dont_filter=True,
            callback=self.get_books
        )

    def get_books(self, response):
        urls = response.xpath("//div[@id='katalog']/div[@class='col col-12 p-left']/div/div/div/div/div/a/@href")
        for u in urls:
            url = u.get()
            joined_url = f"{self.main_url}{url}"
            yield scrapy.Request(url=joined_url, callback=self.scrape_book)

    def scrape_book(self, response):
        title = response.xpath("//h1[@id='productName']/text()").get()
        price = response.xpath("//span[@class='product-price']/text()").get().replace(",",".")
        publisher = response.xpath("//a[contains(@class, 'product-brand')]/span/text()").get()
        
        writer = response.xpath("//a[@id='productModelText']/text()").get()
        writers = [writer.strip() if writer else "No Writer Info"]

        item = ScraperItem()
        item["title"] = title
        item["publisher"] = publisher
        item["writers"] = writers
        item["price"] = float(price)
        item["url"] = response.url
        item["query"] = self.query
        yield item
