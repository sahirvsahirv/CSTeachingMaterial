# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import insepect_response

class MakerspacebotSpider(scrapy.Spider):
    name = 'makerspacebot'
    allowed_domains = ['https://diyhacking.com/makerspaces/']
    start_urls = ['http://https://diyhacking.com/makerspaces//']

    def parse(self, response):
        #view the HTML to see how the data looks
        tablecontents = response.css(".mk-fancy-table.mk-shortcode table-style2").extract()
        for row in response.xpath('//table/tbody/tr/'):
            makerspaces = {}
            makerspaces['country'] = row.xpath('td[1]//text()').extract()
        yield tablecontents





