# -*- coding: utf-8 -*-
import scrapy


class ZhihuloginSpider(scrapy.Spider):
    name = 'zhihulogin'
    allowed_domains = ['https://www.zhihu.com/#signin']
    start_urls = ['http://https://www.zhihu.com/#signin/']


    def parse(self, response):
        pass
