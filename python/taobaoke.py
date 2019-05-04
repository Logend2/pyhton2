import urllib.request
import urllib.parse
import re

def zh1(url):
        data ={}
        data["turl"] = url
        print(data)
        data =urllib.parse.urlencode(data).encode("utf-8")
        response = urllib.request.urlopen("https://duanwangzhihuanyuan.51240.com/web_system/51240_com_www/system/file/duanwangzhihuanyuan/get/?ajaxtimestamp=1554596538671",data)
        html = response.read().decode("utf-8")
        html = str(html).split("href=\"")[-1].strip(r"</a>")
        return html
def zh2(url):
        req = urllib.request.urlopen(url)
        html = req.read().decode("utf-8")
        p = r'<a href="(.*?)".*?class="item-detail">'
        text = re.search(p,html)
        print()
        print(text)
        
        
print(zh1("http://t.cn/E6LgjzT"))
#zh2('https://uland.taobao.com/coupon/edetail?e=OECgyjGdYMsGQASttHIRqf1OcJrqkEL7cB55a/cehSOalfW/5nVWY4fHgDPJCtMJG5fGnE76BTF4JaeQmPOmm5Q5wfGz/u+N1fm3aBfYuJLMBAjZVSbr6yZ6Y/pkHtT5QS0Flu/fbSovkBQlP112cJ5ECHpSy25Ge6L+f9DtnlWeY/Ge5Cb26dtN7m9cS4TU&traceId=0b14f65d15545116572777556e&union_lens=lensId:0b0aff46_0b9f_169f01d795b_34d9&xId=9mxouyoriCbQjclvBQlXXZWTiYlN5hAf0077JlFkioSJJGdH291FNpFFaMEAQ50y5XWX9WKCQMutKYye0AQVOD&activityId=c6586f8076ae4b238f389599b7493852&src=qhkj_dtkp&item_url=&pid=mm_311310008_407750410_108088500124&dx=y')
