__author__ = 'shellbye'
import MySQLdb


class MySQLPipeline(object):

    def __init__(self):
        self.conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="scrapy",
                                    charset="utf8", use_unicode=True)
        self.cur = self.conn.cursor()
        # create table with the utf-8
        create_tbl = """ALTER TABLE scrapy.category
                        MODIFY COLUMN category VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;"""

    def process_item(self, item, spider):
        sql = """insert into category(category) values('%s');""" % item['category'].encode('utf-8')
        print sql
        self.cur.execute(sql)
        self.conn.commit()
        return item


if __name__ == "__main__":
    d = {'category': "value"}
    m = MySQLPipeline()
    m.process_item(d, None)