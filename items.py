# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Spider01Item(scrapy.Item):
    # 小说url地址
    # href=scrapy.Field()
    # 小说名
    name=scrapy.Field()
    # 作者
    # worker=scrapy.Field()
    # 小说简介
    # introduction=scrapy.Field()
    # 章节名
    title=scrapy.Field()
    # 章节url
    # title_url=scrapy.Field()
    # 内容
    content=scrapy.Field()

