# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.http import Request
from scrapy import log

from ..items import LagouItem


class JdSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com/',
    )

    def parse(self, response):
        """run <pre>$ scrapy check </pre> to check
        @url http://www.lagou.com/
        @returns item 0 0
        @returns requests 7000
        """
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
                                for page in range(1, 30):
                                    current_keywords_link = u"http://www.lagou.com/jobs/list_" \
                                                            + current_keywords + u"?kd=" \
                                                            + current_keywords + u"&spc=1&pl=&gj=&xl=&yx=&gx=&st=" \
                                                                                 u"&labelWords=label%2Clabel&lc=" \
                                                                                 u"&workAddress=&city=全国&requestId=" \
                                                                                 u"&pn=" \
                                                            + unicode(page)
                                    yield Request(current_keywords_link,
                                                  meta={
                                                      'category': current_category_text,
                                                      'sub_category': current_sub_category_text,
                                                      'keywords': current_keywords,
                                                      'keywords_link': current_keywords_link,
                                                      'current_page': str(page),
                                                  },
                                                  callback=self.parse_2)
                            else:
                                continue
                    else:
                        continue
            else:
                continue

    def parse_2(self, response):
        # 更多页码已没有结果
        if response.css(".noresult"):
            log.msg(response.meta['category'] + "\t"
                    + response.meta['sub_category'] + "\t"
                    + response.meta['keywords'] + "\t no more page \t since "
                    + response.meta['current_page'],
                    level=log.ERROR)
            return
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
        job_info = response.css(".job_bt")
        if not job_info:
            log.msg("JOB "
                    + response.meta['job_name'] + " no longer exits, the link is "
                    + response.meta['job_link'],
                    level=log.CRITICAL)
            return
        jd = job_info[0].extract()
        item = LagouItem()
        item['category'] = response.meta['category']
        item['sub_category'] = response.meta['sub_category']
        item['keywords'] = response.meta['keywords']
        item['keywords_link'] = response.meta['keywords_link']
        item['job_link'] = response.meta['job_link']
        item['job_name'] = response.meta['job_name']
        item['jd'] = jd
        return item