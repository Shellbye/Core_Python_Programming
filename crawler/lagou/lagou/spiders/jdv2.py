# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from ..items import *


class Jdv2Spider(CrawlSpider):
    name = "jdv2"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com/zhaopin/Java?labelWords=label',
    )
    rules = [
        Rule(LxmlLinkExtractor(
            allow=("http://www.lagou.com/jobs/")),
            callback='parse_item',
            follow=True)
    ]

    def parse_item(self, response):
        item = CategoryItem()
        item['category'] = response.css(".job_bt").extract()
        return item