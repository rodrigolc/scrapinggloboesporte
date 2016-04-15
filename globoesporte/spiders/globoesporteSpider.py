# -*- coding: utf-8 -*-
import scrapy
import logging


class globoesporteSpider(scrapy.Spider):
    name = 'globoesportespider'
    allowed_domains = ['globoesporte.globo.com']

    def start_requests(self):
        yield scrapy.Request("http://globoesporte.globo.com/futebol/times/",self.parse_times)

    def parse_times(self,response):
        for url in response.xpath('//li [@itemprop="itemListElement"]/a/@href').extract():
            logging.info(url)
