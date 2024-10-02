# 使用Xray实现主动模式批量url漏扫脚本

由于权限问题推荐使用超级管理员运行

## 安装库



```
pip install PySocks
pip install tqdm
```

## 以下为Python脚本请根据实际情况修改



```
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

```

## 免责声明


1. 如果您下载、安装、使用、修改本工具及相关代码，即表明您信任本工具
2. 在使用本工具时造成对您自己或他人任何形式的损失和伤害，我们不承担任何责任
3. 如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任
4. 请您务必审慎阅读、充分理解各条款内容，特别是免除或者限制责任的条款，并选择接受或不接受
5. 除非您已阅读并接受本协议所有条款，否则您无权下载、安装或使用本工具
6. 您的下载、安装、使用等行为即视为您已阅读并同意上述协议的约束