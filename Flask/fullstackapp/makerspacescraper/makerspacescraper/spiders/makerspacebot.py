# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
import logging

class MakerspacebotSpider(scrapy.Spider):
    name = 'makerspacebot'
    allowed_domains = ['www.diyhacking.com/makerspaces/']
    start_urls = ['https://www.diyhacking.com/makerspaces//']

    def parse(self, response):
        #view the HTML to see how the data looks
        tablecontents = response.css().extract()
        #/html/body/table/tbody/tr[332]/td[2]/span[2]/a
        for row in response.xpath('/html/body/table/tbody/tr'):
            makerspaces = {}
            from scrapy.shell import inspect_response
            inspect_response(response, self)
            logging.log(DEBUG, row)
            makerspaces['makerspacelink'] = row.xpath('td[2]/span[2]/a').extract()
            yield makerspaces





