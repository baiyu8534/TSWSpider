import requests
from multiprocessing import Process, Pool
import time
import os
import random
import copy
import json
import math
import re
from settings import DEFAULT_HEADERS, USER_AGENTS_LIST, PROCESS_NUM

# 一页大小，多一点，就请求次数少 一点
page_size = 50

def _check_file_name(file_name):
    return re.sub('[\/:*?"<>|]', '-', file_name)  # 去掉非法字符


def _slepp_time():
    """
    每次请求之前随机睡眠一段时间，以免同一时间请求多次
    :return:
    """
    time.sleep(random.choice([0.3, 0.5, 0.8, 1.1, 1.5, 1.8, 2, 2.3, 2.5]))


def _parse_music_url(url):
    return ''.join(map(chr, [int(i) for i in url.split("*")]))


def _get_full_headers(sign):
    headers = copy.deepcopy(DEFAULT_HEADERS)
    # headers["User_Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    headers["User_Agent"] = random.choice(USER_AGENTS_LIST)
    #
    headers["Sign"] = sign
    return headers


def _get_simple_headers():
    headers = {"User_Agent": random.choice(USER_AGENTS_LIST)}
    return headers


def _download_one_music(url, file_name, dir_name):
    mp4 = requests.get(url, headers=_get_simple_headers())
    file_name = _check_file_name(file_name)
    dir_name = _check_file_name(dir_name)
    # print('./{}/{}.mp3'.format(dir_name, file_name))
    with open('./{}/{}.mp3'.format(dir_name, file_name), "wb") as f:
        f.write(mp4.content)
    print("{}.mp3--下载完成".format(file_name))


def _download_music(music_infos, dir_name):
    pool = Pool(PROCESS_NUM)
    for music_info in music_infos:
        pool.apply_async(_download_one_music, (list(music_info.keys())[0], list(music_info.values())[0], dir_name,))

    pool.close()
    pool.join()
    # print(music_infos)
    # _download_one_music(list(music_infos[0].keys())[0], list(music_infos[0].values())[0])


def download_product_by_id(product_id, dir_path_name):
    # 获取声音列表
    # 要带时间戳，毫秒，否则没数据
    sign = str(int(round(time.time() * 1000)))
    # 先获取这个作品有多少条声音
    headers = _get_full_headers(sign)
    response = requests.get(
        "https://www.ting22.com/api.php?c=Json&id={}&page=0&pagesize=10&callback=jQuery21405409841079541011_{}&_={}".format(
            product_id, sign, sign), headers=headers)
    json_str = response.content.decode()
    json_str = json_str.encode('raw_unicode_escape').decode('raw_unicode_escape').replace(r'\/\/', '//').replace(r'\/','/')
    # print(json_str)
    json_data = json.loads("{"+json_str.split("({")[1].split(");")[0])

    music_count = json_data["limit"]

    if music_count > page_size:
        page_count = math.ceil(music_count / page_size)
    else:
        page_count = 1

    music_infos = []

    print("一共{}页".format(page_count))
    # page_count = 1
    # 获取声音地址列表
    for page in range(1, page_count + 1):
        _slepp_time()
        response = requests.get(
            "https://www.ting22.com/api.php?c=Json&id={}&page={}&pagesize={}&callback=jQuery21405409841079541011_{}&_={}".format(
                product_id, page, page_size, str(int(round(time.time() * 1000))), str(int(round(time.time() * 1000)))),
            headers=_get_full_headers(sign))
        json_str = response.content.decode()
        json_str = json_str.encode('raw_unicode_escape').decode('raw_unicode_escape').replace(r'\/\/', '//').replace(
            r'\/',
            '/')
        json_data = json.loads("{"+json_str.split("({")[1].split(");")[0])
        music_infos.extend([{_parse_music_url(x["file"]): x["trackName"]} for x in json_data["playlist"]])
    _download_music(music_infos, dir_path_name)

