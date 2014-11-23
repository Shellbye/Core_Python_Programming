# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.http import Request
from scrapy import log

from ..items import LagouItem


class JdSpider(scrapy.Spider):
    name = "jd-xpath"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'http://www.lagou.com/',
    )

    def parse(self, response):
        for box in response.xpath("//div[@class='menu_box']"):
            for current_category_path in box.xpath("descendant::div[@class='menu_main']"):
                current_category_text = current_category_path.xpath("descendant::h2/text()").extract()[0]
                for current_sub_category_xpath in box.xpath("descendant::div[@class='menu_sub dn']//dl[@class='reset']"):
                    current_sub_category_text = current_sub_category_xpath.xpath("descendant::dt//a/text()").extract()[0].strip()
                    for current_keyword_xpath in current_sub_category_xpath.xpath("descendant::dd//a"):
                        current_keyword_text = current_keyword_xpath.xpath("descendant::text()").extract()[0]
                        for page in range(1, 2):
                            current_keywords_link = u"http://www.lagou.com/jobs/list_" \
                                                    + current_keyword_text + u"?kd=" \
                                                    + current_keyword_text + u"&spc=1&pl=&gj=&xl=&yx=&gx=&st=" \
                                                                         u"&labelWords=label%2Clabel&lc=" \
                                                                         u"&workAddress=&city=全国&requestId=" \
                                                                         u"&pn=" \
                                                    + unicode(page)
                            yield Request(current_keywords_link,
                                          meta={
                                              'category': current_category_text,
                                              'sub_category': current_sub_category_text,
                                              'keywords': current_keyword_text,
                                              'keywords_link': current_keywords_link,
                                              'current_page': str(page),
                                          },
                                          callback=self.parse_2)

    def parse_2(self, response):
        # 更多页码已没有结果
        if response.css(".noresult"):
            log.msg(response.meta['category'] + "\t"
                    + response.meta['sub_category'] + "\t"
                    + response.meta['keywords'] + "\t no more page \t since "
                    + response.meta['current_page'],
                    level=log.ERROR)
            return
        for job_selector in response.xpath("//ul[@class='hot_pos reset']//li[contains(@class,'clearfix')]//div[@class='hot_pos_l']//a"):
            job_link = job_selector.xpath("@href").extract()[0]
            response.meta.update({
                'job_link': job_selector.xpath("descendant::text()").extract()[0],
                'job_name': job_selector.xpath("@href").extract()[0],
            }),
            yield Request(job_link,
                          meta=response.meta,
                          callback=self.parse_3)

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