import requests
from lxml import etree
import os
import time
from DownloadProduct import download_product_by_id

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
}

def get_dir_size(dir_path):
    file_list = os.listdir(dir_path)
    size = 0
    for file_name in file_list:
        size += os.path.getsize(dir_path + "/" + file_name)

    return round(size / 1024 / 1024, 2)


def start_spider():
    flag = True
    while flag:
        product_name = input("请输入要搜索的小说：")
        # product_name = "剑来"
        # print("正在搜索《{}》...".format(product_name))
        response = requests.get("https://www.ting22.com/search.php?q={}".format(product_name), headers=headers)
        # print(response.content.decode())
        if "抱歉，找不到" in response.content.decode():
            print("没有搜索到内容")
            continue
        else:
            flag = False
        html = etree.HTML(response.content.decode().replace("<em>", "").replace("</em>", ""))
        result_list_element = html.xpath('//div[@class="result"]')
        result_list = []
        for result_element in result_list_element:
            result = {}
            result["product_name"] = result_element.xpath(".//h3/a/text()")[0]
            result["product_url"] = result_element.xpath(".//h3/a/@href")[0]
            result["product_id"] = result_element.xpath(".//h3/a/@href")[0].split("/")[-1].split(".")[0]
            result["writer1"] = result_element.xpath('.//span')[0].xpath('./text()')[0]
            result["writer2"] = result_element.xpath('.//span')[1].xpath('./text()')[0]
            result_list.append(result)

        # pprint(result_list)

        print("-" * 10 + "搜索结果" + "-" * 10)
        for i, result in zip(range(len(result_list)), result_list):
            print("{}.{}\t\t\t{}\t\t\t{}\n".format(i + 1, result["product_name"], result["writer1"], result["writer2"]))

        product_num = input("请输入要爬取的作品编号：")
        # print(product_name)
        # print(type(product_name))
        # print(product_name.isnumeric())
        # print(product_name.isdigit())
        while not product_num.isdigit() or int(product_num) > len(result_list):
            print("请输入正确的编号")
            product_num = input("请输入要爬取的作品编号：")
        result = result_list[int(product_num) - 1]
        if not os.path.exists('./{}'.format(result["product_name"])):
            os.mkdir('./{}'.format(result["product_name"]))
        print("开始爬取《{}》....".format(result["product_name"]))
        print("保存路径为当前路径下“{}”文件夹里....".format(result["product_name"]))
        start_time = time.time()

        # 调用爬虫方法
        print(result["product_id"])
        download_product_by_id(result["product_id"], result["product_name"])

        print("-"*20)
        print("全部爬取完毕,共{}条音频，占用空间：{}MB".format(
            len(os.listdir("./{}".format(result["product_name"]))),
            get_dir_size("./{}".format(result["product_name"]))))
        end_time = time.time()
        print('用时:%s秒' % (end_time - start_time))


if __name__ == "__main__":
    start_spider()
