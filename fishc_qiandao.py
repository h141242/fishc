# -*- coding: utf-8 -*
'''
new Env('鱼C签到');
'''

import os
import datetime
import requests
from notify import send  # 导入青龙消息通知模块

def main(*args):
    
    cookie=os.environ['Fishc_COOKIE']
    
    url = "https://fishc.com.cn/plugin.php?id=k_misign:sign&operation=qiandao&formhash=3e9fc998&format=empty"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.14 Safari/537.36 Edg/83.0.478.13",
        "Cookie":cookie
    }
    html = requests.get(url=url,headers = headers).content.decode("gbk")
    print(html)
    print("=====================")
    if "今日已签" in html:
        #print("您已经签过到了哟")
        send('鱼C签到', '⚡您已经签过到了哟\n\n本通知 By HY-鱼C\n通知时间:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    else:
        #print("签到成功")
        send('鱼C签到', '💖签到成功\n\n本通知 By HY-鱼C\n通知时间:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == '__main__':
    main()
