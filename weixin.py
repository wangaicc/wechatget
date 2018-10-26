# coding=utf-8
from itchat.content import *
import itchat
import urllib
import time
import datetime
import re
import os


# global ctime, filename
ctime = 0
tt = False


def downRes(url, name):
    # print(usname)
    name = "123"
    name = name+".mp3"
    if os.path.exists(name):
        os.remove(name)
    urllib.request.urlretrieve(url, filename=name)
    filename = name
    time.sleep(30)
    # print(name)
    # itchat.send_file("1.txt", toUserName=usname)
    return filename


def getRes(url, usname):
    reswxurl = "https://res.wx.qq.com/voice/getvoice?mediaid="
    header = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN"
    }
    request = urllib.request.Request(url, headers=header)
    try:
        data = urllib.request.urlopen(request).read()
    except:
        itchat.send_msg("网络连接失败！请稍候再试！！", toUserName=usname)
    # ,"\S+":{
    content = data.decode('utf-8')
    restr = u'(?<=,")\S+(?=":{)'
    sn = re.search(restr, content).group(0)
    resurl = reswxurl+sn
    # request = urllib.request.Request(resurl, headers=header)
    print(resurl)
    return resurl


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    global ctime, tt
    # print(msg)
    if msg.text == "鱼头鱼头":
        ctime = msg.CreateTime + 10
        # print(ctime)
        msg.user.send("请在10秒内发送需要提取音频文件的连接发我，超时重新发送代号")
        tt = True
    if msg.CreateTime+10 > ctime and tt == True:
        # print(msg.url)
        u = getRes(msg.url, msg.FromUserName)
        msg.user.send("正在下载。。稍后（30秒后）将文件发送给你\n你也可以自行下载\n{}".format(u))
        filename = downRes(u, msg.text)
        tt = False
        print(filename)
        msg.user.send("@fil@%s" % filename)
    print("{}:{}".format(datetime.datetime.now(), msg.text))


def main():
    itchat.auto_login(hotReload=True, enableCmdQR=True)
    itchat.run()


if __name__ == '__main__':
    main()
