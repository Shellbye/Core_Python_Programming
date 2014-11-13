# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    category = scrapy.Field()
    sub_category = scrapy.Field()
    keywords = scrapy.Field()
    keywords_link = scrapy.Field()
    jd = scrapy.Field()


class CategoryItem(scrapy.Item):
    category = scrapy.Field()


class SubCategoryItem(scrapy.Item):
    link = scrapy.Field()
    text = scrapy.Field()


class KeywordsItem(scrapy.Item):
    link = scrapy.Field()
    text = scrapy.Field()