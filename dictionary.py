import random
import requests
import re
from pykakasi import kakasi
from bs4 import BeautifulSoup
kakasi = kakasi()

def scrape(q):
    url = "https://dictionary.goo.ne.jp/word/"+q
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    #print(soup.prettify())　#htmlの表示
    strings = []
    items = soup.find_all("meta")
    for item in items:
        inf = item.get("content")
        if inf is None:
            continue
        if "noindex" in inf:
            return 0
        if "意味" in inf:
            strings.append(inf)
    #print(strings[0])
    ans = []
    ans = strings[0].split("。")
    return ans[2]

def change(str):
    a = ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","お","ん"]

    p = re.compile('[ァ-ン]+')
    if p.fullmatch(str) != None:
        kakasi.setMode("K","H")
        conv = kakasi.getConverter()
        str = conv.do(str)

    p = re.compile(r'^[\u4E00-\u9FD0]+$')
    if p.fullmatch(str) != None:
        kakasi.setMode("J","H")
        conv = kakasi.getConverter()
        str = conv.do(str)

    b = list(str)
    i = random.randint(0,len(b)-1)
    b[i] = random.choice(a)
    s = ''.join(b)
    return s

a = 0

q1 = input("調べたい日本語をひらがなで入力して下さい＞")
while(a != ("もうええわ" or "いいかげんにしろ")):
    q3 = 0
    count = 0
    while(q3==0):
        q2 = change(q1)
        if(q2==0):
            break
        q3 = scrape(q2)
        count += 1
        if(count > 10000):
            break

    if q3 == 0:
        print("みつかりませんでした。")
    else:
        print(q3)
    a = input(">")
    if("?" in a ):
        print(q2)
    elif("？" in a):
        print(q2)

print("ありがとうございました")
