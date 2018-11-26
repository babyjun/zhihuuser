# -*- coding: utf-8 -*-
import json

import scrapy

from zhihuuser.items import UserItem


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    start_user='excited-vczh'
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'allow_message,is_followed,is_following,is_org,is_blocking,employments,' \
                 'answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'

    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?' \
                  'include={include}&offset={offset}&limit={limit}'
    follows_query = 'data[*].answer_count,articles_count,' \
                    'gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'



    def start_requests(self):
        '''
        url = 'https://www.zhihu.com/api/v4/members/mi-meng-2?' \
              'include=allow_message,is_followed,is_following,is_org,is_blocking,employments,' \
              'answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'

        url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?' \
              'include=data[*].answer_count,articles_count,gender,follower_count,is_followed,' \
              'is_following,badge[?(type=best_answerer)].topics&offset=40&limit=20'
        yield scrapy.Request(url, callback=self.parse)
        '''
        yield scrapy.Request(self.user_url.format(user=self.start_user, include=self.user_query), self.parse_user)
        yield scrapy.Request(self.follows_url.format(user=self.start_user, include=self.follows_query, offset=0, limit=20), callback=self.parse_follows)

    def parse_user(self, response):
        result = json.loads(response.text)
        item = UserItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item

        yield scrapy.Request(self.follows_url.format(user=result.get('url_token'), include=self.user_query, limit=20, offset=0), callback=self.parse_follows)

    def parse_follows(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield scrapy.Request(self.user_url.format(user=result.get('url_token'), include=self.user_query), self.parse_user)
        if 'paging' in results.keys() and results.get('paging').get('is_end') is False:
            next_page = results.get('paging').get('next')
            yield scrapy.Request(next_page, callback=self.parse_follows)
