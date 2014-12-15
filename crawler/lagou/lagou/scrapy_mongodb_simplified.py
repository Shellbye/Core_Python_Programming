__author__ = 'shellbye'
"""
This is a simplified pipeline from https://github.com/sebdah/scrapy-mongodb
"""

from pymongo.mongo_client import MongoClient
import settings


class MongoDBPipelineSimplified(object):

    def __init__(self):
        connection = MongoClient(settings.MONGODB_URI)
        database = connection[settings.MONGODB_DATABASE]
        self.collection = database[settings.MONGODB_COLLECTION]

    def process_item(self, item, spider):
        if not isinstance(item, list):
            item = dict(item)
        self.collection.insert(item, continue_on_error=True)
        return item


if __name__ == "__main__":
    d0 = {'category': "value0"}
    d1 = {'category': "value1"}
    d2 = {'category': "value2"}
    m = MongoDBPipelineSimplified()
    a_list = [d0, d1]
    m.process_item(a_list, None)
    m.process_item(d2, None)