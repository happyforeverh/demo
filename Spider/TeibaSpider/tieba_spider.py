# coding=utf-8
# 百度贴吧有反爬虫措施，此爬虫无效
import requests


class TeibaSpider:

    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw="+tieba_name+"ie=utf-8&pn={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    def get_url_list(self):
        return [self.url_temp.format(i*50) for i in range(1)]

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode(encoding="gbk")

    def save_html(self, html_str, page_num):
        file_path = "{}-第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "w", encoding="gbk") as f:
            f.write(html_str)

    def run(self):  # 实现主要逻辑
        # 1.构造url列表
        url_list = self.get_url_list()
        # 2.对列表中的url发起请求,获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3.保存请求的页面
            page_num = url_list.index(url)+1
            self.save_html(html_str, page_num)


if __name__ == '__main__':
    tieba_spider = TeibaSpider("美图")
    tieba_spider.run()
