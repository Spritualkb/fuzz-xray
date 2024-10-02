#!/usr/bin/env python
# coding=utf-8
################
#   Spritualkb   #
################

import os
import hashlib
import re
import datetime
import random
from time import strftime
import socks
import socket
from tqdm import tqdm  # 导入tqdm库

# 设置代理
def set_proxy(proxy_address, proxy_port):
    socks.set_default_proxy(socks.SOCKS5, proxy_address, proxy_port)
    socket.socket = socks.socksocket

# 扫描
def get_url():
    # 输入要批量扫描的url文件
    with open("url.txt") as f:
        lines = f.readlines()

    # 匹配http | https请求头
    pattern = re.compile(r'^(https|http)://')
    
    # 使用 tqdm 显示进度条
    for line in tqdm(lines, desc="Scanning URLs", unit="URL"):
        try:
            if not pattern.match(line.strip()):
                targeturl = "http://" + line.strip()
            else:
                targeturl = line.strip()
            now = datetime.datetime.now()  # 当前日期
            outputfilename = now.strftime("%Y-%m-%d_") + str(random.randint(1, 1000000))
            do_scan(targeturl.strip(), outputfilename)
        except Exception as e:
            print(e)
            pass
            
    print("Xray Scan End~")
    return

# 报告
def do_scan(targeturl, outputfilename="xray"):
    scan_command = "xray.exe webscan --basic-crawler {} --html-output {}.html".format(targeturl, outputfilename)
    os.system(scan_command)
    return

if __name__ == '__main__':
    proxy_address = "127.0.0.1"  # 你的代理地址
    proxy_port = 10809  # 你的代理端口
    set_proxy(proxy_address, proxy_port)
    get_url()
