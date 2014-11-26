# -*- coding: utf-8 -*-
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
            # image_urls is not a single image url but multi of them
            # notice that the image url need to be full path
            item['image_urls'] = [a.xpath("@src").extract()[0]]
            item_list.append(item)
        return item_list