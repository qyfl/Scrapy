# -*- coding:utf-8 -*-
# Create by qyfl on 17-10-29

from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(['scrapy', 'crawl', 'book'])