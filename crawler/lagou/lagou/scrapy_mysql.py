__author__ = 'shellbye'
import peewee
from peewee import *

db = MySQLDatabase(host='127.0.0.1', user='root', passwd='', database='scrapy')


class Keywords(peewee.Model):
    link = peewee.CharField()
    text = peewee.TextField()

    class Meta:
        database = db


class Category(peewee.Model):
    category = peewee.TextField()

    class Meta:
        database = db


class MySQLPipeline(object):
    config = {
        'name': 'scrapy',
        'user': 'root',
        'password': '',
    }

    def process_item(self, item, spider):
        if not Category.table_exists():
            Category.create_table()
        k = Category(category=item['category'])
        k.save()

        return item


if __name__ == "__main__":
    d = {'category': "value"}
    m = MySQLPipeline()
    m.process_item(d, None)