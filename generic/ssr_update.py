# -*- coding: utf-8 -*-

'''
zhouzhongqing
2019年11月5日18:30:30
ssr帐号更新
'''

import os
import requests
from bs4 import BeautifulSoup
import base64

# 写入文件
def write_to_file(file_name, txt):
    '''''
        讲txt文本存入到file_name文件中
    '''
    print("正在存储文件" + str(file_name));
    # 1 打开文件
    # w 如果没有这个文件将创建这个文件
    '''
    'r'：读

    'w'：写

    'a'：追加

    'r+' == r+w（可读可写，文件若不存在就报错(IOError)）

    'w+' == w+r（可读可写，文件若不存在就创建）

    'a+' ==a+r（可追加可写，文件若不存在就创建）
    '''
    f = open(file_name, 'a+', encoding='utf-8');
    # 2 读写文件
    f.write(str(txt));
    # 3 关闭文件
    f.close();


if __name__ == '__main__':
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

    ssr_domain = "https://github.com/Alvin9999/pac2/blob/master/ssconfig.txt";
    try:
        content_string = "";
        content = requests.get(ssr_domain, headers=headers,timeout=999);
        # print(content.status_code)
        if content.status_code == 200:
            # print(content.text)
            # 初始化并制定解析器
            soup = BeautifulSoup(content.text, "lxml");
            tableContent = soup.find_all(class_='highlight tab-size js-file-line-container');
            # print(tableContent)
            for item in tableContent[0]:
                if item is not None and str(item).strip() != "":
                    # print(item)
                   #print(item.text);
                    #content_string += str(item.text).replace("\n","")+"\n";
                    content_string += str(item.text).replace("\n", "");

            #if os.path.exists("ssconfig.txt"):
              #  os.remove("ssconfig.txt")
            #write_to_file("ssconfig.txt",content_string);
            ssr_info = str(base64.b64decode(content_string),encoding='utf-8')#.replace("\n", "").replace("\t", "").replace("\r", "");
            print(ssr_info)
        else:
            print("访问ssr帐号失败!")

    except Exception as e:
        print("program error %s " % e)
    finally:
     print("finally print!")

    random = input("请按任意键退出")
