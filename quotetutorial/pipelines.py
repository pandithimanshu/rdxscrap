# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import random
import sqlite3

class QuotetutorialPipeline:

    def __init__(self):
        self.create_connection()
        # self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("../db.sqlite3")
        self.curr = self.conn.cursor()

    # def create_table(self):
    #     self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        # self.curr.execute("""create table quotes_tb( title , author ,tag)""")



    def process_item(self, item, spider):
        self.store_db(item)
        print("Pipeline :" + item["title"][0])

        return item

    def store_db(self,item):
        n = random.randint(0, 22000)

        self.curr.execute("""insert into app_quote values (?,?,?,?)""",(
            n,
            item['title'][0],
            item['token'],
            item['url']

        ))
        self.conn.commit()

# class QuotetutorialPipeline(object):
#     def process_item(self, item, spider):
#         item.save()
#         return item