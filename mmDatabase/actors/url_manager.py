class UrlManager(object):
    def __init__(self):
        # 待爬取url集合
        self.new_urls = set()
        # 已爬取url集合
        self.old_urls = set()

    def add_new_url(self, new_url):
        if new_url is None:
            return
        if new_url not in self.new_urls and new_url not in self.old_urls:
            self.new_urls.add(new_url)
        else:
            return

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_urls(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
