# -*- coding: utf-8 -*-

# Scrapy settings for huxiuspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import sys
import os
from os.path import dirname
path = dirname(dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(path)

BOT_NAME = 'huxiuspider'

SPIDER_MODULES = ['huxiuspider.spiders']
NEWSPIDER_MODULE = 'huxiuspider.spiders'
DEFAULT_ITEM_CLASS = 'huxiuspider.items.BookItem'

LOG_LEVEL = 'INFO'

ITEM_PIPELINES = {
	'huxiuspider.pipelines.AddToMySQl':100
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'huxiuspider (+http://www.yourdomain.com)'
