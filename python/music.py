import urllib.request
import urllib.parse
import json
import os

def get(id):
    list = {}   #歌曲名-歌手，id组成的字典
    url = ''.join(["http://music.163.com/api/playlist/detail?id=",id])#歌单地址
    print('正在获取歌单数据...')
    req = urllib.request.urlopen(url)
    html = req.read().decode('utf-8')
    list1 = json.loads(html)    #返回歌单的数据解析
    x = list1['result']['tracks']
    for i in x:
        name = str(i['name'])   #歌名
        song = str(i['artists'][0]['name']) #歌手
        id = str(i['id'])   #歌id，下载用
        x = ''.join([name,r"-",song])#把歌名和歌手拼接成‘歌名-歌手’的格式
        list[x] = id   #歌名歌手和id组成字典
    print("共有",len(list),'首歌')
    return list

def downalfile(list):
    len = 0
    if os.path.exists("music") == 'fasle':
        os.mkdir('music')
        print('no!')
    else:
        print("exist!")
    
    for i in list:
        name = ''.join(['music/',i,'.mp3'])
        song = urllib.parse.quote(list[i])    #歌名-歌手 中文字符转uel，否则下载会出问题
        address = ''.join(['http://music.163.com/song/media/outer/url?id=',song,'.mp3'])  #歌曲下载地址
       # downal.downal(address) #下载进度条失败的尝试
        print('(oﾟvﾟ)ノ开始下载',i,'...')

        data = urllib.request.urlopen(address) #开始下载
        with open(name,"wb+") as f:
            f.write(data.read()) #写入磁盘
            print(i,'下载已完成(￣▽￣)"')
            len += 1
    print(len,'首下载成功..')

if __name__ == '__main__':
    print(str(os.path.exists("test_dir")))
    list = get(input('输入歌单id:\n'))
    downalfile(list)
    input("按任意键退出")
