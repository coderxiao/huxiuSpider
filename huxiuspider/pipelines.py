# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class HuxiuspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class AddToMySQl(object):
	def __init__(self):
		try:
			self.conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='wx',db='huxiu',port=3306,charset='utf8')
			self.cur = self.conn.cursor()
			self.conn.select_db('huxiu')
		except MySQLdb.Error,e:
			print 'conn db fail'

	def process_item(self, item, spider):
		sql = "insert into books(title,name) values(%s,%s)"
		pars = (str(item["title"]).decode("raw_unicode_escape"),str(item["name"]).decode("raw_unicode_escape"))
		self.cur.execute(sql,pars)
		self.conn.commit()
		return item
	
	def close_spider(self,spider):		
		self.cur.cloes()
		self.conn.close()
		




