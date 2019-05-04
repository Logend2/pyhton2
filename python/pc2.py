import urllib.request
import urllib.parse
import re

#url = 'https://sex8.cc/books-shaixuan-2-2-1.html'
def getlist(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/51.0.2704.63 Safari/537.36'}
    reg = urllib.request.Request(url=url,headers=headers)
    repone = urllib.request.urlopen(reg)
    html = repone.read().decode("utf-8")
    file =  open('data.html','r',buffering=-1,encoding='utf-8')
    p = r'<h4 style="margin:0 0 6px 0;"><a href="(.*?)">(.*?)</a>'
    textlist = re.findall(p,html)
    a = 0
    list = []
    for i in textlist:
        a += 1
        if a > 3:
            break
        url1 = 'https://sex8.cc'+ i[0]
        #print(url1)
        
        headers1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/51.0.2704.63 Safari/537.36'}
        reg1 = urllib.request.Request(url=url1,headers=headers)
        repone1 = urllib.request.urlopen(reg1)
        html1 = repone1.read().decode("utf-8")
        p1 = r'<a class="z xw1 xs3" href="(.*?)".*?<span style="color: #0072ff;">'
        text1 = re.findall(p1,html1)
        list.append([i[1],text1[0]])
        print(list)
     
    return list

list1 = getlist('https://sex8.cc/books-shaixuan-2-2-1.html?zishu=0_1')
for i in list1:
    print(i)

