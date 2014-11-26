# -*- coding: utf-8 -*-
import urlparse
import scrapy
from ..items import MyImageItem


class CategorySpider(scrapy.Spider):
    name = "image"
    allowed_domains = ["douban.com"]
    start_urls = (
        'http://www.douban.com/',
    )

    def parse(self, response):
        item_list = []
        for a in response.xpath("//img"):
            item = MyImageItem()
            # I'm not clear why the url should be put in []
            item['image_urls'] = [urlparse.urljoin("http://www.douban.com", a.xpath("@src").extract()[0])]
            item_list.append(item)
        return item_list