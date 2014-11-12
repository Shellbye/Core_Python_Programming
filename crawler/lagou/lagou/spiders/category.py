# -*- coding: utf-8 -*-
import scrapy
from ..items import CategoryItem


class CategorySpider(scrapy.Spider):
    name = "category"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com/',
    )

    def parse(self, response):
        for a in response.css(".menu_box .menu_main h2"):
            item = CategoryItem()
            item['category'] = a.extract()
            return item
            # print a.extract()
