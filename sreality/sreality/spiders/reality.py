import scrapy

from scrapy_playwright.page import PageMethod
from sreality.items import SrealityItem


class RealitySpider(scrapy.Spider):
    name = "reality"

    def _get_meta(self):
        return {
            "playwright": True,
            "playwright_include_page": True,
            "playwright_page_methods": [PageMethod('wait_for_selector', '.property')],
            "errback": self.errback,
        }

    def start_requests(self):
        for i in range(1, 26):
            yield scrapy.Request(
                f"https://www.sreality.cz/hledani/prodej/byty?strana={i}",
                meta=self._get_meta())

    async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.close()
        for item in response.css(".property"):

            title = item.css(".name::text").get()
            #   Here I was not sure whether to get only the first image or if I was supposed to get them all, however,
            #   the task was in singular therefore I decided to grab only the first one
            src = item.css("img")[0].attrib["src"]
            yield SrealityItem(
                title=title,
                image_url=src)

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
