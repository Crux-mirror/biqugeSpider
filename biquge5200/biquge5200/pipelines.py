# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

#将每个小说存放MongoDB数据库
class Biquge5200Pipeline(object):
    def process_item(self, item, spider):
        client = MongoClient('127.0.0.1',27017)
        #连接数据库
        db = client.admin
        db.authenticate("crux","163444")
        book_name = item["book_name"]
        book = db[book_name]
        print("开始下载："+book_name+":"+item["section_name"])
        book.insert({"category":item["category"],"book_name":item["book_name"],
                   "book_author":item["book_author"],"content":item["content"]})
        return item

