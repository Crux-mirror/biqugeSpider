# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Biquge5200Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
     #小说名字
    novel_name = scrapy.Field()
    #小说类别
    novle_family = scrapy.Field()
    #小说主页地址
    novel_url = scrapy.Field()
    #小说作者
    novel_author = scrapy.Field()
    #小说状态
    novel_status = scrapy.Field()
    #小说字数
    novel_number = scrapy.Field()
    #小说所有章节页面
    novel_all_section_url = scrapy.Field()
    #小说最后更新时间
    novel_updatetime = scrapy.Field()
    #存放小说地址列表
    novel_section_urls = scrapy.Field()
    #存放小说章节地址和小说章节名臣对应关系，字典
    section_url_And_section_name = scrapy.Field()
