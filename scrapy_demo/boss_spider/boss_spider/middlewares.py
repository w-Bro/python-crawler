# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import requests
import json
from boss_spider.modeles import ProxyModel
from twisted.internet.defer import DeferredLock


class UserAgentDownloaderMiddleware(object):
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    ]

    def process_request(self, request, spider):
        usre_agent = random.choice(self.USER_AGENTS)
        request.headers['User-Agent'] = usre_agent


class IPProxyDownloadMiddleware(object):
    PROXY_URL = 'http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=11&pack=41039&ts=1&ys=0&cs=0&lb=1&sb=0&pb=45&mr=1&regions='

    def __init__(self):
        super(IPProxyDownloadMiddleware, self).__init__()
        self.current_proxy = None
        self.lock = DeferredLock()

    def process_request(self, request, spider):
        if 'proxy' not in request.meta or self.current_proxy.is_expiring:
            # 请求代理
            self.update_proxy()
            request.meta['proxy'] = self.current_proxy.proxy

    def process_response(self, request, response, spider):
        if response.status != 200 or "captcha" in response.url:
            if not self.current_proxy.blacked:
                self.current_proxy.blacked = True
            print("%s这个代理被加入黑名单了" % self.current_proxy.ip)
            self.update_proxy()
            # 一定要返回request将这个请求重新加入到调度中，下次再发送，不然会漏掉这个数据
            return request
        # 如果正常也要记得返回response，不然就不会传到爬虫解析那里去
        return response

    # 异步请求过程中也可能会同时发生多个请求，导致请求太过频繁，需要加个锁限制
    def update_proxy(self):
        self.lock.acquire()
        if not self.current_proxy or self.current_proxy.is_expiring or self.current_proxy.blacked:
            response = requests.get(self.PROXY_URL)
            text = response.text
            print('重新获取了一个代理', text)
            # json格式的字符串load成字典
            result = json.loads(text)
            if len(result['data']) > 0:
                data = result['data'][0]
                proxy_model = ProxyModel(data)
                self.current_proxy = proxy_model
        self.lock.release()