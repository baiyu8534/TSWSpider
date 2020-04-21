# 交互式有声小说爬虫
- 命令行的一个交互程序，接受用户输入，判断输入内容，进行内容展示
- request发送请求，拿到json数据，用json库进行解析
- 解析到音频文件地址，使用multiprocessing.Pool进行多进程下载，可以设置进程数量，在settings配置文件中
