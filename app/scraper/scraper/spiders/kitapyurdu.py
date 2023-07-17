import scrapy
from urllib.parse import urlparse, parse_qs
from ..items import ScraperItem


# can i use linkextractors?
class KitapyurduSpider(scrapy.Spider):
    name = "kitapyurdu"

    def __init__(self, query=str, name=None, **kwargs):
        self.query = query

    def start_requests(self):
        url = f"https://www.kitapyurdu.com/index.php?route=product/search&filter_name={self.query}&filter_in_stock=1"
        yield scrapy.Request(url=url, callback=self.paging)

    def paging(self, response):
        paging = response.xpath("//a[@class='last']/@href").get()
        if paging:
            parsed_url = urlparse(paging)
            parsed_query = parse_qs(parsed_url.query)
            max_page = int(parsed_query.get("page",[0])[0]) # parse the URL and get the value of "page" from it
            for i in range(2, max_page+1):
                url = f"https://www.kitapyurdu.com/index.php?route=product/search&page={i}&filter_name={self.query}&filter_in_stock=1"
                yield scrapy.Request(url, callback=self.parse_books_from_search)

        yield scrapy.Request(
            url= "http://",
            meta={
                "first_page": True,
                "html": response.text
            },
            dont_filter=True,
            callback=self.parse_books_from_search
        )

    def parse_books_from_search(self, response):
        books_in_page = response.xpath("//div[@class='product-grid']/div[@class='product-cr']")

        for book in books_in_page:
            url = book.xpath(".//div[@class='name ellipsis']/a/@href").get()
            yield scrapy.Request(
                url=url,
                callback=self.parse_book_data
            )

    def parse_book_data(self, response):

        price = response.xpath("//div[@class='price__item']/text()").get().strip().replace(",","")
        price_small = response.xpath("//div[@class='price__item']/small/text()").get().strip()
        price_final = f"{price}.{price_small}"

        producers = response.xpath("//div[@class='pr_producers__item']")
        producers = [
            producer.xpath(".//a/text()").get().strip() for producer in producers
        ]

        title = response.xpath("//h1[@class='pr_header__heading']/text()").get().strip()

        item = ScraperItem()
        item["title"] = title
        item["publisher"] = producers[-1]
        item["writers"] = producers[:-1]
        item["price"] = float(price_final)
        item["url"] = response.url
        item["query"] = self.query
        yield item
