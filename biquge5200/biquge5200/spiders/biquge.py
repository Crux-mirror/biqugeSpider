# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from biquge5200.items import Biquge5200Item

class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['biquge5200.cc']
    start_urls = ['https://www.biquge5200.cc']
    server_link='https://www.biquge5200.cc/'

    #从start_request发送请求
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0],callback=self.parse_home_page)
    #首页解析,跳转到小说分类
    def parse_home_page(self,response):
        items = Biquge5200Item()
        #获取分类信息查找所有xiaoshuo
        category = response.xpath("//div[@class='nav']/ul/li/a/text()").extract()[2:]
        category_urls = response.xpath("//div[@class='nav']/ul/li/a/@href").extract()[2:]
        for i in range(len(category_urls)):
            items["category"] = category[i]
            print("开始爬取"+category[i]+"-------------:"+category_urls[i][2:])
            yield scrapy.Request("https:"+category_urls[i], callback=self.parse,meta={'items': items})
    #获取小说名及作者信息
    def parse(self, response):
        items=response.meta["items"]
        books=response.xpath("//ul/li/span[1]/a/text()").extract()
        books_urls = response.xpath("//ul/li/span[1]/a/@href").extract()
        for i in range(len(books_urls)):
            items["book_name"] = books[i]
            items["book_url"] = books_urls[i]
            yield scrapy.Request(url=books_urls[i],meta={"items":items},callback=self.parse_novel)

    #小说章节目录解析 ,第一章url
    def parse_novel(self, response):
        items=response.meta["items"]
        items["book_name"] = response.xpath("//div[@id='info']/h1/text()").extract()[0]
        items["book_author"] = response.xpath("//div[@id='info']/p[1]/text()").extract()[0][7:]
        #章节url及章节名
        section_url = response.xpath("//div[@id='list']/dl/div/following-sibling::dd[1]/a/@href").extract()[0]
        section_name = response.xpath("//div[@id='list']/dl/div/following-sibling::dd[1]/a/text()").extract()[0]
        items["section_name"] = section_name
        items["section_url"] = section_url
        yield scrapy.Request(section_url,meta={'items':items},callback=self.parse_content)
    #章节内容解析
    def parse_content(self,response):
        items = response.meta['items']
        items["section_name"] = response.xpath("//div/h1/text()").extract()[0]
        strs = ''
        list = response.xpath("//div[@id='content']/p/text()").extract()
        for i in list:
            strs = strs + i.replace(u'\u3000', u' ')
        items["content"] = strs
        yield items
        next_section_url =  response.xpath("//div[@class='bottem2']/a[4]/@href").extract()[0]
        #items["section_name"] = response.xpath("//div/h1/text()").extract()[0]
        items["section_url"] = next_section_url
        if next_section_url is not None and next_section_url is not self.server_link:
            yield scrapy.Request(next_section_url, meta={'items': items}, callback=self.parse_content)

