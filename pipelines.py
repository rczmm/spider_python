# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import pymysql
from spider01.items import Spider01Item


class Spider01Pipeline:

    def __init__(self):
        self.d = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='test'
        )

        self.cursor = self.d.cursor()

        create_sql = '''
                    create table book_datas(
                    name varchar(40),
                    title varchar(50),
                    content text
                    )'''

        print('start create book_datas table! ')
        self.cursor.execute(create_sql)

        # self.f = open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        item=dict(item)
        item['name']=''.join(item['name'])
        item['title']=''.join(item['title'])
        item['content']=item['content'].replace("['",'')
        item['content']=item['content'].replace("']",'')
        item['content']=item['content'].replace("\\",'')
        item['content']=''.join(item['content'])

        try:
            insert_sql = '''
                insert into book_datas(name,title,content)values({},{},{})
                '''.format('"'+item['name']+'"','"'+item['title']+'"','"'+item['content']+'"')

            self.cursor.execute(insert_sql)

            self.d.commit()
        except:
            print("What the hell is this? Don't throw everything!")

        # data=json.dumps(dict(item),ensure_ascii=False)+',\n'

        # self.f.write(data)

        return item
