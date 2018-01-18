# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from scrapy.selector import HtmlXPathSelector
import sys
from scrapy import Item, Field
import urllib2
import logging

LOG_FILENAME = 'scraperspider.log'

class MakerSpaces(scrapy.Item):
    url = scrapy.Field()

class MakerspacebotSpider(scrapy.Spider):
    #name with which you run the command line - scrapy crawl ,akerspacebot
    name = 'makerspacebot'

    allowed_domains = ['diyhacking.com']
    #allowed_domains = ['en.wikipedia.org']
    try:
        start_urls = ['https://www.diyhacking.com/makerspaces']

        #start_urls = ['http://en.wikipedia.org']
    except Exception as e:
        logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
        logging.debug('There was an exception in the code:  ' + str(e))
        #sys.exit()

    #def start_requests(self):
     #   for urls in self.start_urls:
      #      yield scrapy.Request(urls, callback=self.parse_bot,
       #                             errback=self.err_bot,
        #                            dont_filter=True)

    def parse_bot(self, response):
        try:
            logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
            logging.debug('In the parse method:')
            hxs = scrapy.Selector(text=response).xpath('//div[@id="mk-page-section-5a5dd165039f5"]/text()').extract()
            logging.debug('In the parse method:  ' + str(hxs))
        except Exception as e:
            logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
            logging.debug('There was an exception in the code:  ' + str(e))
            #sys.exit()
        finally:
            logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
            logging.debug('There was an exception in the code - in finally:  ')
            #sys.exit()
    def err_bot(self, failure):
        self.logger.error(repr(failure))

    def parse(self, response):
     #   #view the HTML to see how the data looks
        #object of the Item class
        item = MakerSpaces()
            #*[@id="mk-page-section-5a5dd165039f5"]/div[3]/div[1]/div/div[5]/div/table[3]/tbody/tr[8]/td[2]
        #mk-fancy-table mk-shortcode table-style2
        urls = scrapy.Selector(response).xpath('//div[@class="mk-fancy-table"]//div[@class="mk-shortcode"]').extract()
        print("url is = " + str(urls))

        #item['url'] = urls
        #return item

        logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
        logging.debug('In the parse method:')
        hxs = scrapy.Selector(response)
        logging.debug('In the parse method:  ' + str(hxs))





