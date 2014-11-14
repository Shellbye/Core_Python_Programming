# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy import log
from ..items import CategoryItem


class CategorySpider(scrapy.Spider):
    name = "category"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com/',
    )

    def parse(self, response):
        item_list = []
        for a in response.css(".menu_box .menu_main h2"):
            log.msg("This is a warning", level=log.ERROR)
            item = CategoryItem()
            c = a.extract()
            m = re.search("<h2>(.+?)<span></span></h2>", c)
            if m:
                item['category'] = m.group(1).strip()
            item_list.append(item)
            # print a.extract()
        return item_list