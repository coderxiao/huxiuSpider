
import scrapy
from scrapy.selector import Selector
import re
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as selink
from scrapy.contrib.spiders import CrawlSpider,Rule

from huxiuspider.items import BookItem

class BookSpider(CrawlSpider):
	name = "books"
	allow_domains = ["huxiu.com"]
	start_urls = ["http://www.huxiu.com/books"]
	rules = (
		Rule(selink(allow=("books/([0-9]+)\.html",))
			,),
		Rule(selink(allow=("article/([0-9]+)/1\.html"))
			,callback='parse_3')
	)

	def parse_2(self,response):
		for sel in response.xpath("//div[@class='clearfix mod-b mod-list-book']"):
			item = BookItem()
			item["title"] = sel.xpath("//ul[@class='clearfix ul-list']/li[1]/i/text()").extract()
			item["name"] = sel.xpath("div[@class='b-info-list']/h3/a/@href").extract()
			
			return item

	def parse_3(self,response):
		sel = Selector(response)
		item = BookItem()
		item["title"] =  sel.xpath("//h1[@class='t-h1']/text()").extract()
		item["name"] = sel.xpath("//ul[@class='clearfix ul-list']/li[1]/i/text()").extract()
		yield item


