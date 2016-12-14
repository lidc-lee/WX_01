# coding=utf-8

"""
@version: ??
@author: AA-ldc
@license: Apache Licence 
@file: pyPaqu.py
@time: 2016/12/9 11:29
爬虫
"""

import requests
import re
import sys

reload(sys)


# html = requests.get('http://tieba.baidu.com/f?ie=utf-8&kw=python')

# header是我们自己构造的一个字典，里面保存了user-agent
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
# html = requests.get('http://jp.tingroom.com/yuedu/yd300p/', headers=header)
# html.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。
# # print html.text
#
# title = re.findall('color:#666666;">(.*?)</span>', html.text, re.S)
# for each in title:
#     print each
#
# chinese = re.findall('color: #039;">(.*?)</a>', html.text, re.S)
# for each in chinese:
#     print each
# url = 'https://www.crowdfunder.com/browse/deals'
# url = 'https://www.crowdfunder.com/browse/deals&template=false'

# 构造字典
# data = {
#     'entities_only': 'true',
#     'page': '2'
# }
# html_post = requests.post(url, data=data)
# title = re.findall('"card-title">(.*?)</div>', html_post.text, re.S)
# for each in title:
#     print each

# 极客学院爬取
class spider(object):
    def __init__(self):
        print u'开始爬取信息'

    # getsource用来获取网页源代码
    def getSource(self, url):
        html = requests.get(url)
        return html.text

    def changePage(self, url, total_page):
        now_page = int(re.search('pageNum=(\d+)', url, re.S).group(1))
        page_group = []
        for i in range(now_page, total_page + 1):
            link = re.sub('pageNum=\d+', 'pageNum=%s' % i, url, re.S)
            page_group.append(link)
        return page_group

    # geteveryclass用来抓取每个课程块的信息
    def getEveryClass(self, source):
        everyclass = re.findall('(<li deg="".*?</li>)', source, re.S)
        return everyclass

    # getinfo用来从每个课程块中提取出我们需要的信息
    def getInfo(self, eachclass):
        info = {}
        info['title'] = re.search('target="_blank">(.*?)</a>', eachclass, re.S).group(1)
        info['content'] = re.search('</h2><p>(.*?)</p>', eachclass, re.S).group(1)
        timeandlevel = re.findall('<em>(.*?)</em>', eachclass, re.S)
        info['classtime'] = timeandlevel[0]
        info['classlevel'] = timeandlevel[1]
        info['learnnum'] = re.search('"learn-number">(.*?)</em>', eachclass, re.S).group(1)
        return info

    # saveinfo用来保存结果到info.txt文件中
    def saveinfo(self, classinfo):
        f = open('info.txt', 'a')
        for each in classinfo:
            f.writelines('title:' + each['title'] + '\n')
            f.writelines('content:' + each['content'] + '\n')
            f.writelines('classtime:' + each['classtime'] + '\n')
            f.writelines('classlevel:' + each['classlevel'] + '\n')
            f.writelines('learnnum:' + each['learnnum'] + '\n\n')
        f.close()


if __name__ == '__main__':
    classinfo = []
    url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    jikespider = spider()
    all_links = jikespider.changePage(url, 20)
    for link in all_links:
        print u'正在处理页面：' + link
        html = jikespider.getSource(link)
        everyclass = jikespider.getEveryClass(html)
        for each in everyclass:
            info = jikespider.getInfo(each)
            classinfo.append(info)
    jikespider.saveinfo(classinfo)
