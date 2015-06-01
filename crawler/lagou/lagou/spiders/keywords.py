# -*- coding: utf-8 -*-
import re
import scrapy
from ..items import KeywordsItem


class KeywordsSpider(scrapy.Spider):
    name = "keywords"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com/',
    )

    def parse(self, response):
        item_lists = []
        for a in response.css("#sidebar div.mainNavs div.menu_box div.menu_sub dl.reset dd a"):
            item = KeywordsItem()
            c = a.extract()
            # 这里class前面的空格必须要有
            c = re.sub(' class="curr"', '', c)
            m = re.search("""<a href="(.+?)">(.+?)</a>""", c)
            if m:
                item['link'] = m.group(1).strip()
                item['text'] = m.group(2).strip()
            item_lists.append(item)
        return item_lists