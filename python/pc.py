import urllib.request
import urllib.parse
import re

url = 'https://sex8.cc/books-shaixuan-2-2-1.html'
#url = "http://www.baidu.com"

data = ['null']
head = {}

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.63 Safari/537.36'}
'''
reg = urllib.request.Request(url=url,headers=headers)
repone = urllib.request.urlopen(reg)
html = repone.read().decode("utf-8")
'''
file =  open('data.html','r',buffering=-1,encoding='utf-8')
#file.write(html)
f = file.read()
print(f)
file.close()

p = r'<h4 style="margin:0 0 6px 0;"><a href="(.*?)">(.*?)</a>'
textlist = re.findall(p,f)

