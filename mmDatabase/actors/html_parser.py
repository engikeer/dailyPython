import re
from urllib import parse
from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse_url(self, menu_url, html_cont):
        if menu_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
        new_urls = self._get_new_urls(menu_url, soup)
        return new_urls

    def parse(self, html_cont):
        res_data = dict(name_m="", name_o="", name_a="", act_birthday="", constel="",
                        blood_type="", height="", weight="", BWH="", homeplace="", job="",
                        debut="", hobby="")
        img_data = {}
        soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")
        # 解析名字
        name_node = soup.find("h1")
        name_text = name_node.get_text()
        res_data["name_m"] = re.findall(r"(.*?)\(", name_text)[0]
        res_data["name_o"] = re.findall(r"\((.*?)\)", name_text)[0]

        # 解析信息
        data_nodes = soup.find("div", class_="infodiv").find_all("tr")
        for data_node in data_nodes:
            nodes = data_node.find_all("td")
            argu = nodes[0].get_text()
            value = nodes[1].get_text()
            if "别" in argu or "其" in argu:
                res_data["name_a"] = value
            elif "道" in argu:
                res_data["debut"] = value
            elif "趣" in argu:
                res_data["hobby"] = value
            elif "生日" in argu or "生 日" in argu:
                res_data["act_birthday"] = value
            elif "座" in argu:
                res_data["constel"] = value
            elif "血" in argu:
                res_data["blood_type"] = value
            elif "高" in argu:
                res_data["height"] = value
            elif "重" in argu:
                res_data["weight"] = value
            elif "围" in argu:
                res_data["BWH"] = value
            elif "国" in argu or "出 生" in argu or "出生" in argu:
                res_data["homeplace"] = value
            elif "作" or "职" in argu:
                res_data["job"] = value

        img_node = soup.find("a", class_="imglink").find("img")
        # img_data["name"] = img_node["alt"] # 问题：没法与数据库保持一致
        img_data["name"] = res_data["name_m"]
        img_data["url"] = img_node["src"]
        return res_data, img_data

    def _get_new_urls(self, menu_url, soup):
        new_urls = set()
        # /girl/23790/
        links = soup.find_all("a", href=re.compile(r"/girl/\d+/"))
        for link in links:
            new_url = link["href"]
            new_full_url = parse.urljoin(menu_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
