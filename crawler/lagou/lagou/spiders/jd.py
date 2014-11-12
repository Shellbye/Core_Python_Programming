# -*- coding: utf-8 -*-
import scrapy


class JdSpider(scrapy.Spider):
    name = "jd"
    allowed_domains = ["lagou.com"]
    start_urls = (
        # comes from keywords results
        "http://www.lagou.com/jobs/115600.html?source=search",
    )

    def parse(self, response):
        for a in response.css(".job_bt"):
            print a.extract()