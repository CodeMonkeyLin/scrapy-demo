# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# DB_ADDR = '120.55.98.237'
# DB_PORT = 3306
# DB_USER = 'root'
# DB_PWD = '#!/root/Passw0rd@zeaho.com'
# DB_NAME = 'scrapy'

DB_ADDR = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PWD = '123456'
DB_NAME = 'scrapy'

RETRY_TIMES = 10
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 408, 407]

DOWNLOADER_MIDDLEWARES = {
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
    # 'tutorial.middlewares.ProxyMiddleWare': 25,
    # 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': None
}
# PROXY_LIST = '/Users/apple/Desktop/workspace/scrappy-spider/company/company/spiders/proxies.txt'
PROXY_MODE = 0
