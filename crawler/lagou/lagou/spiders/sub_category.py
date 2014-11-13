# -*- coding: utf-8 -*-
import re
import scrapy
from ..items import SubCategoryItem


class SubCategorySpider(scrapy.Spider):
    name = "sub-category"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com/',
    )

    def parse(self, response):
        item_list = []
        for a in response.css("#sidebar div.mainNavs div.menu_box div.menu_sub dl.reset dt a"):
            item = SubCategoryItem()
            c = a.extract()
            c = re.sub('\r\n', '', c)
            c = re.sub('\t', '', c)
            c = re.sub(' ', '', c)
            print c
            # 因为上面去掉了所有的空格，所以这里的a标签直接和href属性连在了一起
            m = re.search("""<ahref="(.+?)">(.+?)</a>""", c)
            if m:
                item['link'] = m.group(1).strip()
                item['text'] = m.group(2).strip()
            item_list.append(item)
        return item_list