# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Jogador(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    apelido = scrapy.Field()
    nome = scrapy.Field()

class Time(scrapy.Item):
    id = scrapy.Field()
    nome = scrapy.Field()
