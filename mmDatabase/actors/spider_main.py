# -*- coding: utf-8 -*-
import traceback
from urllib.request import urlretrieve

from actors import db_manager
from actors import html_downloader
from actors import html_parser
from actors import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.db_manager = db_manager.DBManager()

    # 爬取所有页面的资料
    def craw(self, root_url):
        for i in range(1, 16):
            url = root_url + str(i) + ".html"
            self.crawPage(url)
            print("------finish page No." + str(i))
        self.db_manager.disconnect()

    def crawPage(self, root_url):
        # 将入口页加入待爬url集
        self.urls.add_new_url(root_url)

        try:
            # 获取待爬url
            menu_url = self.urls.get_new_url()
            # 下载目录页面
            html_menu = self.downloader.download(menu_url)
            # 获取页面内url
            new_urls = self.parser.parse_url(menu_url, html_menu)
            self.urls.add_new_urls(new_urls)
            while self.urls.has_new_urls():
                # 下载内容页面
                cont_url = self.urls.get_new_url()
                html_cont = self.downloader.download(cont_url)
                # 获取内容数据
                res_data, img_data = self.parser.parse(html_cont)
                print(res_data["name_m"])
                # 保存图片
                urlretrieve(img_data["url"], "img/%s.jpg" % img_data["name"])
                # 将数据储存到数据库
                self.db_manager.save_data(res_data)

        except Exception as e:
            print(str(e))
            traceback.print_exc()

            print("保存失败")


if __name__ == "__main__":
    root_url = "http://www.zngirls.com/tag/riben/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
