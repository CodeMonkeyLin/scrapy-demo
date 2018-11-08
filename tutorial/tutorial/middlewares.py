# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy import log
import random
import requests
import base64
from bs4 import BeautifulSoup
import lxml
from multiprocessing import Process, Queue
import random
import json
import time


class ProxyMiddleWare(object):
    """docstring for Proxies"""
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8"
    }

    proxies = []
    t = 0

    def process_request(self, request, spider):
        '''对request对象加上proxy'''

        url = 'https://h.wandouip.com/get/ip-list?pack=353&num=1&xy=1&type=1&mr=1&app_key=09ff74d76adc8c240e36ca12912d7437'
        html = requests.get(url, self.headers).content
        # b = html.split('\\/r\\/n')
        # url = "https://h.wandouip.com/get/ip-list?pack=0&num=1&xy=1&type=1&lb=\r\n&mr=2&"

        html = requests.get(url, headers=self.headers).content
        proxy = "http://" + html
        self.t = self.t + 1
        print proxy.strip()
        print self.t
        request.meta['proxy'] = proxy.strip().decode('utf-8')
