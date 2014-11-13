# -*- coding: utf-8 -*-
import re

import scrapy

from ..items import LagouItem


class JdSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com/',
    )

    def parse(self, response):
        item_list = []
        for category_selector in response.css(".mainNavs .menu_box"):
            category = category_selector.css(".menu_main h2").extract()[0]
            m = re.search("<h2>(.+?)<span></span></h2>", category)
            if m:
                current_category_text = m.group(1).strip()
                # print current_category_text
                for sub_category_selector in category_selector.css(".menu_sub dl.reset"):
                    c = sub_category_selector.css("dt a").extract()[0]
                    c = re.sub('\r\n', '', c)
                    c = re.sub('\t', '', c)
                    c = re.sub(' ', '', c)
                    # 因为上面去掉了所有的空格，所以这里的a标签直接和href属性连在了一起
                    m = re.search("""<ahref="(.+?)">(.+?)</a>""", c)
                    if m:
                        current_sub_category_text = m.group(2).strip()
                        # print current_sub_category_text
                        for keywords_selector in sub_category_selector.css("dd a"):
                            k = keywords_selector.extract()
                            # 这里class前面的空格必须要有
                            k = re.sub(' class="curr"', '', k)
                            m = re.search("""<a href="(.+?)">(.+?)</a>""", k)
                            if m:
                                current_keywords = m.group(2).strip()
                                # print current_keywords
                                item = LagouItem()
                                item['category'] = current_category_text
                                item['sub_category'] = current_sub_category_text
                                item['keywords'] = current_keywords
                                item_list.append(item)
                                # todo
                            else:
                                continue
                    else:
                        continue
            else:
                continue
        return item_list