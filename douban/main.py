#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time       : 2019/7/30 14:10
# @Author     : wangxingxing
# @Email      : xingfengwxx@gmail.com 
# @File       : main.py
# @Software   : PyCharm
# @Description:

from scrapy import cmdline

cmdline.execute("scrapy crawl movie -o result.json".split())
