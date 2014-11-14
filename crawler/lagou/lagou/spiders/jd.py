# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.http import Request

from ..items import LagouItem


class JdSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com/',
    )

    def parse(self, response):
        for category_selector in response.css(".mainNavs .menu_box"):
            category = category_selector.css(".menu_main h2").extract()[0]
            m = re.search("<h2>(.+?)<span></span></h2>", category)
            if m:
                current_category_text = m.group(1).strip()
                for sub_category_selector in category_selector.css(".menu_sub dl.reset"):
                    c = sub_category_selector.css("dt a").extract()[0]
                    c = re.sub('\r\n', '', c)
                    c = re.sub('\t', '', c)
                    c = re.sub(' ', '', c)
                    # 因为上面去掉了所有的空格，所以这里的a标签直接和href属性连在了一起
                    m = re.search("""<ahref="(.+?)">(.+?)</a>""", c)
                    if m:
                        current_sub_category_text = m.group(2).strip()
                        for keywords_selector in sub_category_selector.css("dd a"):
                            k = keywords_selector.extract()
                            # 这里class前面的空格必须要有
                            k = re.sub(' class="curr"', '', k)
                            m = re.search("""<a href="(.+?)">(.+?)</a>""", k)
                            if m:
                                current_keywords = m.group(2).strip()
                                current_keywords_link = m.group(1).strip()
                                yield Request(current_keywords_link,
                                              meta={
                                                  'category': current_category_text,
                                                  'sub_category': current_sub_category_text,
                                                  'keywords': current_keywords,
                                                  'keywords_link': current_keywords_link
                                              },
                                              callback=self.parse_2)
                            else:
                                continue
                    else:
                        continue
            else:
                continue

    def parse_2(self, response):
        for job_selector in response.css(".hot_pos .clearfix .hot_pos_l .mb10 a"):
            j = job_selector.extract()
            m = re.search("""<a href="(.+?)">(.+?)</a>""", j)
            if m:
                job_link = m.group(1).strip()
                job_name = m.group(2).strip()
                response.meta.update({
                    'job_link': job_link,
                    'job_name': job_name,
                }),
                yield Request(job_link,
                              meta=response.meta,
                              callback=self.parse_3)
            else:
                continue

    def parse_3(self, response):
        job_info = response.css(".job_bt")[0]
        jd = job_info.extract()
        item = LagouItem()
        item['category'] = response.meta['category']
        item['sub_category'] = response.meta['sub_category']
        item['keywords'] = response.meta['keywords']
        item['keywords_link'] = response.meta['keywords_link']
        item['job_link'] = response.meta['job_link']
        item['job_name'] = response.meta['job_name']
        item['jd'] = jd
        return item