import re
import scrapy
from spider01.items import Spider01Item


class Testdemo(scrapy.Spider):

    name = 'spider001'

    item = Spider01Item()

    allowd_domains = ['http://www.xbiquge.la']

    url = 'http://www.xbiquge.la'

    start_urls = ['http://www.xbiquge.la/xiaoshuodaquan/', ]

    book_url = {}

    def parse(self, response, **kwargs):

        node_list = response.xpath('//*[@id="main"]/div/ul/li')

        for node in node_list:
            href = node.xpath('./a/@href').extract()

            self.item['name']= node.xpath('./a/text()').extract()

            yield scrapy.Request(''.join(href), callback=self.parse_title)


    def parse_title(self, response):

        worker = response.xpath('//*[@id="info"]/p[1]/text()').extract()[0]

        intodution = response.xpath('//*[@id="intro"]/p[2]/text()').extract()[0]

        titles = response.xpath('//*[@id="list"]/dl/dd/a/@href').extract()


        for url2 in titles:
            url1 = self.url + url2

            yield scrapy.Request(url1, callback=self.parse_text)


    def parse_text(self, response):

        title = response.xpath('//*[@class="bookname"]/h1/text()').extract()

        data = response.xpath('//*[@id="content"]').extract()[0]

        data=re.findall('<div id="content">(.*?)<p><a hre', data)

        data=str(data)

        data = data.replace("\\r", ' ')

        data = data.replace("<br>", ' ')

        data = data.replace("\\xa0", ' ')


        self.item['content'] = data
        self.item['title'] = title


        yield self.item
