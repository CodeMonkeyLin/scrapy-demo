# -*- coding: utf-8 -*-

import base64
import MySQLdb
import scrapy
from scrapy.http import FormRequest
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import CrawlSpider
from scrapy.utils.project import get_project_settings
from .. import items
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Type = sys.getfilesystemencoding()

settings = get_project_settings()
conn = MySQLdb.connect(host=settings.get('DB_ADDR'), user=settings.get('DB_USER'), passwd=settings.get(
            'DB_PWD'), db=settings.get('DB_NAME'), port=settings.get('DB_PORT'), charset='utf8')
cur = conn.cursor()
class CompanyListSpider(CrawlSpider):
    base_url = "http://www.jszhaobiao.com/corp.html"

    name = "company-list"
    start_urls = [
        base_url,
    ]

    def parse(self, response):
        yield scrapy.Request(url=self.base_url, callback=self.parse_list)

    def parse_list(self, response):
        sel = scrapy.Selector(text=response.body)
        detail_hrefs = sel.xpath("//tr[@class='even']/td/a/@href").extract()
        company_names = sel.xpath("//tr[@class='even']/td[2]/text()").extract()
        print company_names
        try:
            for index in range(len(detail_hrefs)):
                company_name = company_names[index]
                print company_name
                detail_href = detail_hrefs[index]
                print cur.execute
                count = cur.execute('SELECT company_name FROM company_list WHERE company_name = "%s"' % company_name)
                if cur.rowcount == 0:
                    print 1
                    cur.execute(
                        'INSERT INTO company_list (`company_name`,`detail_href`) values ("%s","%s")' % (company_name,detail_href))
                    conn.commit()
        except MySQLdb.Error, e:
            print '[Error] INSERT INTO company_list: ', e[0]
