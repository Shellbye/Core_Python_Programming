# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.contrib.loader import ItemLoader
from ..items import CategoryItem


class ItemloadertestSpider(scrapy.Spider):
    name = "itemloadertest"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com/',
    )

    def get_text(self, html):
        return re.search("<h2>(.+?)<span></span></h2>", html).group(1).strip()

    def parse(self, response):
        item_list = []
        for a in response.css(".menu_box .menu_main h2"):
            l = ItemLoader(item=CategoryItem(), response=response)
            # l.add_css('category', ".menu_box .menu_main h2")
            l.add_value("category", a.extract(), self.get_text)
            item_list.append(l.load_item())
        return item_list
