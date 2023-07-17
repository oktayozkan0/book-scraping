### Notes about scraper development

- kitapyurdu.com
  - No communication with the API, data must be retrieved from the page source.
  - Selenium is not required, the page is not rendered with javascript, http request is enough.
- kitapsepeti.com
  - same as kitapyurdu.com

In fact, Scrapy is not even necessary, but it will be used because it is required for the given task.
Selenium will not be used. JS rendering time extends the scraping time. Downloading CSS and images makes scraping slower.

Do not scrape if data exists in database.

backend and frontend was written in a hurry. It should be written much better.