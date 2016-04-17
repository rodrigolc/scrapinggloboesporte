# -*- coding: utf-8 -*-
import scrapy
import logging
from globoesporte.items import Time
import sqlite3


class globoesporteSpider(scrapy.Spider):
    name = 'globoesportespider'
    allowed_domains = ['globoesporte.globo.com']

    def start_requests(self):
        yield scrapy.Request("http://globoesporte.globo.com/futebol/times/",self.parse_lista_times)


    def parse_lista_times(self,response):
        for url in response.xpath('//li [@itemprop="itemListElement"]/a/@href').extract():
            yield scrapy.Request(url,self.parse_time)

    def parse_time(self,response):
        time = Time()
        time["nome"] = response.xpath('//div/h1/a [@class="logo"]/text()').extract()[0]
        time["url_suffix"] = '/'.join(response.url.split('/')[3:])
        return time
