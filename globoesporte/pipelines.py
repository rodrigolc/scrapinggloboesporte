# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import items
import sqlite3
import logging

class GloboesportePipeline(object):
    def open_spider(self, spider):
        self.connection = sqlite3.connect('database/database.sqlite')
        self.cursor = self.connection.cursor()
    def close_spider(self, spider):
        self.connection.commit()
        self.connection.close()
    def process_item(self, item, spider):
        if isinstance(item,items.Time):
            self.cursor.execute('insert into Time(url_suffix,nome) values (?,?)',(item['url_suffix'],item['nome']))
        logging.info(item)
        return item
