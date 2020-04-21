# function
# JieMa(u)
# {
#     var
# tArr = u.split("*"), str = '';
# for (var i = 0, n = tArr.length; i < n; i++)
# {
#     str += String.fromCharCode(tArr[i]);
# }
# return str;
# }

path = "104*116*116*112*58*47*47*97*117*100*105*111*46*99*111*115*46*120*109*99*100*110*46*99*111*109*47*103*114*111*117*112*55*48*47*77*48*66*47*54*66*47*69*68*47*119*75*103*79*122*108*52*72*71*116*67*105*114*117*68*95*65*70*108*89*74*66*76*108*79*117*89*52*55*48*46*109*52*97"


def jiema(s):
    return ''.join(map(chr, [int(i) for i in s.split("*")]))


# print(jiema(path))

'''
UM_distinctid=17191432d6617f-0e92e99913bcd6-f313f6d-e1000-17191432d676ff;
Hm_lvt_b3038a04fad08f9e74270f8999205b49=1587280031;
PHPSESSID=4dbl7nnaqscpq93eovoftfk875;
shistory=think%3A%5B%22%25E5%2589%2591%25E6%259D%25A5%22%5D;
__gads=ID=c6595d0bce9d1c88:T=1587280083:S=ALNI_MaGE17ztzI78IKeskDx3adv78O68A;
index_setID=1721;
CNZZDATA1278740084=1471695963-1587280029-%7C1587280544
1721_setNAME=%E5%89%91%E6%9D%A5%20%E7%AC%AC%E4%BA%8C%E9%83%A8%20%E7%AC%AC8%E5%8D%B7-%E6%80%9D%E6%97%A0%E9%82%AA1839%20%E4%BA%BA%E9%9A%BE%E7%A7%B0%E5%BF%83,%E4%BA%8B%E9%9A%BE%E9%81%82%E6%84%BF;
1721_setURL=https://www.ting22.com/ting/1721-961.html;
Hm_lpvt_b3038a04fad08f9e74270f8999205b49=1587280546;
'''

"""
UM_distinctid=17191432d6617f-0e92e99913bcd6-f313f6d-e1000-17191432d676ff; 
Hm_lvt_b3038a04fad08f9e74270f8999205b49=1587280031; 
PHPSESSID=4dbl7nnaqscpq93eovoftfk875; 
shistory=think%3A%5B%22%25E5%2589%2591%25E6%259D%25A5%22%5D; 
__gads=ID=c6595d0bce9d1c88:T=1587280083:S=ALNI_MaGE17ztzI78IKeskDx3adv78O68A; 
index_setID=1721;
CNZZDATA1278740084=1471695963-1587280029-%7C1587280170;
Hm_lpvt_b3038a04fad08f9e74270f8999205b49=1587280173; 
1721_setNAME=%E5%89%91%E6%9D%A5%20%E7%AC%AC%E4%BA%8C%E9%83%A8%20%E7%AC%AC8%E5%8D%B7-%E6%80%9D%E6%97%A0%E9%82%AA1839%20%E4%BA%BA%E9%9A%BE%E7%A7%B0%E5%BF%83,%E4%BA%8B%E9%9A%BE%E9%81%82%E6%84%BF;
1721_setURL=https://www.ting22.com/ting/1721-961.html
"""

import requests
from requests.cookies import RequestsCookieJar

# cookie_str = "UM_distinctid=17191432d6617f-0e92e99913bcd6-f313f6d-e1000-17191432d676ff; Hm_lvt_b3038a04fad08f9e74270f8999205b49=1587280031; PHPSESSID=4dbl7nnaqscpq93eovoftfk875; shistory=think%3A%5B%22%25E5%2589%2591%25E6%259D%25A5%22%5D; __gads=ID=c6595d0bce9d1c88:T=1587280083:S=ALNI_MaGE17ztzI78IKeskDx3adv78O68A; index_setID=1721; 1721_setNAME=%E5%89%91%E6%9D%A5%20%E7%AC%AC%E4%BA%8C%E9%83%A8%20%E7%AC%AC8%E5%8D%B7-%E6%80%9D%E6%97%A0%E9%82%AA1839%20%E4%BA%BA%E9%9A%BE%E7%A7%B0%E5%BF%83,%E4%BA%8B%E9%9A%BE%E9%81%82%E6%84%BF; 1721_setURL=https://www.ting22.com/ting/1721-961.html; Hm_lpvt_b3038a04fad08f9e74270f8999205b49=1587280546; CNZZDATA1278740084=1471695963-1587280029-%7C1587280544"
cookie_str = "UM_distinctid=17191432d6617f-0e92e99913bcd6-f313f6d-e1000-17191432d676ff; Hm_lvt_b3038a04fad08f9e74270f8999205b49=1587280031; PHPSESSID=4dbl7nnaqscpq93eovoftfk875; shistory=think%3A%5B%22%25E5%2589%2591%25E6%259D%25A5%22%5D; __gads=ID=c6595d0bce9d1c88:T=1587280083:S=ALNI_MaGE17ztzI78IKeskDx3adv78O68A; index_setID=1721; 1721_setNAME=%E5%89%91%E6%9D%A5%20%E7%AC%AC%E4%BA%8C%E9%83%A8%20%E7%AC%AC8%E5%8D%B7-%E6%80%9D%E6%97%A0%E9%82%AA1839%20%E4%BA%BA%E9%9A%BE%E7%A7%B0%E5%BF%83,%E4%BA%8B%E9%9A%BE%E9%81%82%E6%84%BF; 1721_setURL=https://www.ting22.com/ting/1721-961.html; Hm_lpvt_b3038a04fad08f9e74270f8999205b49=1587280546; CNZZDATA1278740084=1471695963-1587280029-%7C1587280544"
cookie = {i.split("=")[0]: i.split("=")[1] for i in cookie_str.split("; ")}
# print(cookie)

import time

t = time.time()
sign = str(int(round(t * 1000)))

headers = {
    "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "Accept-encoding": "gzip, deflate, br",
    "Accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8",
    "X-Requested-With": "XMLHttpRequest",
    # "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Referer": "https://www.ting22.com/ting/1721-961.html",
    "Sign": sign,
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"

}

# response = requests.get("https://www.ting22.com/api.php?c=Json&id=1721&page=96&pagesize=10", headers=headers,
#                         cookies=cookie)
# print(response.request.headers)
# print(response.status_code)
#
# proxies = {
#   "http": "http://10.10.1.10:3128",
#   "https": "http://10.10.1.10:1080",
# },proxies=proxies

response = requests.get(
    "https://www.ting22.com/api.php?c=Json&id=1721&page=4&pagesize=10&callback=jQuery21405409841079541011_{}&_={}".format(
        sign, sign), headers=headers)

print(response.content.decode())

json_str = response.text
json_str = json_str.encode('raw_unicode_escape').decode('raw_unicode_escape').replace(r'\/\/', '//').replace(r'\/', '/')
# print(response.raw._connection.sock.getsockname()[0])
import json

json_data = json.loads(json_str.split("(")[1].split(")")[0])
from pprint import pprint

pprint(json_data)

mp4_url_list = [x["file"] for x in json_data["playlist"]]

mp4_real_url_list = [''.join(map(chr, [int(i) for i in s.split("*")])) for s in mp4_url_list]

pprint(mp4_real_url_list)

# mp4 = requests.get(mp4_real_url_list[0])
#
# with open('./test.mp4',"wb") as f:
#     f.write(mp4.content)

import os

print(os.listdir("./剑来 第二部"))
print("%.2fMB" % (os.path.getsize(r"D:\剑来有声书\第8卷-思无邪1842 小师叔最从容2_剑来 第二部.mp3") / 1024 / 1024))


def get_dir_size(dir_path):
    file_list = os.listdir(dir_path)
    size = 0
    for file_name in file_list:
        size += os.path.getsize(dir_path + "/" + file_name)

    return round(size / 1024 / 1024, 2)


print(get_dir_size("./剑来 第二部"))
