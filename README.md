## 环境配置
* pip（下载管理Python包）
```bash
    sudo apt-get install python-pip
```
* pyenv(管理Python版本)
```bash
    git clone git://github.com/yyuu/pyenv.git ~/.pyenv
```
>- 如果使用的是bash
```bash
    $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    $ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```
>- 如果使用的是zsh
```bash
    $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
    $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
    $ echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```
>- 之后，重新加载shell
```bash
    $ exec $SHELL -l
```
* 安装以下包
>- mysql数据库 for Python
```bash
    pip install MySQL-python 
```
>- scrapy框架
```bash
    pip install scrapy 
```
>- 工具类
```bash
    pip install requests 
```
```bash
    pip install bs4 
```
```bash
    pip install moment 
```
>- 部署
```bash
    pip install scrapyd
```
````bash
     pip install scrapyd-client
````

## 创建项目
    scrapy startproject tutorial
* scrapy.cfg: 项目的配置文件
* tutorial/: 该项目的python模块。之后您将在此加入代码。
* tutorial/items.py: 项目中的item文件.
* tutorial/pipelines.py: 项目中的pipelines文件.
* tutorial/settings.py: 项目的设置文件.
* tutorial/spiders/: 放置spider代码的目录.

## 创建一个爬虫文件
    在spiders目录下创建company_list.py

## 创建表
```sql
CREATE TABLE `company_list` (
    `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
    `company_name` varchar(50) DEFAULT NULL COMMENT '企业名称',
    `detail_href` varchar(255) DEFAULT NULL COMMENT '详情地址',
    PRIMARY KEY (`id`),
    KEY `company_name` (`company_name`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT=' 企业列表';
```

## 中间件
```bash
    DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
    'tutorial.middlewares.ProxyMiddleWare': 25,
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': None
}
```

## 代理
* 在middlewares文件下写代理逻辑

## 本地部署管理
* [Scrayp-通过scrapyd部署爬虫]（https://my.oschina.net/RanboSpider/blog/1610171）

## 服务端部署管理
* [用Scrapyd把Scrapy爬虫一步一步部署到腾讯云上]（https://juejin.im/post/5b0b87796fb9a009e405d12c）