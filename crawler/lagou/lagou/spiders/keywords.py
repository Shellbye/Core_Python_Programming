# -*- coding: utf-8 -*-
import scrapy


class KeywordsSpider(scrapy.Spider):
    name = "keywords"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com/',
    )

    def parse(self, response):
        for a in response.css("#sidebar div.mainNavs div.menu_box div.menu_sub dl.reset dd a"):
            print a.extract()

