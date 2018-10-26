import urllib
import re


def getRes(url):
    reswxurl = "https://res.wx.qq.com/voice/getvoice?mediaid="
    header = {'User-Agent': "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN"}
    request = urllib.request.Request(url, headers=header)
    data = urllib.request.urlopen(request).read()
    # ,"\S+":{
    content = data.decode('utf-8')
    restr = '(?<=,")\S+(?=":{)'
    sn = re.search(restr, content).group(0)
    resurl = reswxurl+sn
    # request = urllib.request.Request(resurl, headers=header)
    print(resurl)
    # urllib.request.urlretrieve(resurl, "d:\\1.mp3")
    return resurl
