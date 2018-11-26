# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class UserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    name = Field()
    avatar_url = Field()
    headline = Field()
    is_followed = Field()
    answer_count = Field()
    is_following = Field()
    url = Field()
    url_token = Field()
    allow_message = Field()
    is_blocking = Field()
    is_vip = Field()
    is_advertiser = Field()
    avatar_url = Field()
    is_org = Field()
    gender = Field()
    follower_count = Field()
