# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Jogador(scrapy.Item):
    url_suffix = scrapy.Field()
    nome_popular = scrapy.Field()
    nome = scrapy.Field()
    sobrenome = scrapy.Field()

class Time(scrapy.Item):
    url_suffix = scrapy.Field()
    nome = scrapy.Field()

class Noticia(scrapy.Item):
    url_suffix = scrapy.Field()
    titulo = scrapy.Field()
    subtitulo = scrapy.Field()

class JogadorMencionado(scrapy.Item):
    url_suffix_noticia = scrapy.Field()
    url_suffix_jogador = scrapy.Field()

class TimeMencionado(scrapy.Item):
    url_suffix_noticia = scrapy.Field()
    url_suffix_time = scrapy.Field()

class JogadorNoTime(scrapy.Item):
    url_suffix_time = scrapy.Field()
    url_suffix_jogador = scrapy.Field()
