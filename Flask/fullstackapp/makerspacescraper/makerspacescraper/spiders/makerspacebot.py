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
    name = scrapy.Field()

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

            #*[@id="mk-page-section-5a5dd165039f5"]/div[3]/div[1]/div/div[5]/div/table[3]/tbody/tr[8]/td[2]

        #examples
        #//table[@id="table_text"]//tr//td[2]//a//@href'
        #response.xpath('//*[@id="Year1"]/table//tr')
        #item['hol'] = product.xpath('td[1]//text()').extract_first()
        #mk-fancy-table mk-shortcode table-style2

        #response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " product-item view-list ")]')
        #response.css('div.product-item.view-list')
        urls = response.css('div.mk-fancy-table.mk-shortcode.table-style2')
        msnames = urls.xpath('//table//tr//td[2]//text()').extract()
        msurls = urls.xpath('//table//tr//td[4]//text()').extract()
        item = MakerSpaces()
        item['url'] = msurls
        item['name'] = msnames
        #print("item is = " + str(item))
        return item
        #for count in range(len(msurls)):
         #   item = MakerSpaces()
          #  item.url = msurls[count]
           # item.name = msnames[count]
        #    #item.name = dataname
        #   print("item is = " + str(item))



        print("item is = " + str(item))
        #print("first item is = " + str(makerspaceurls[0]))
        #item['url'] = urls
        #return item

        logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
        logging.debug('In the parse method:')
        hxs = scrapy.Selector(response)
        logging.debug('In the parse method:  ' + str(hxs))





