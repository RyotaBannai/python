from bs4 import BeautifulSoup as BS
from scrapetest import *
import re
  
def getChildren(html):
  try:
    html = BS(html, 'html5lib')
    return html.find('table', {'id':'giftList'}) # 可能な限り、属性を付けてSpecificに.
  except AttributeError:
    return None

def getGiftImg(html):
  try:
    html = BS(html, 'html5lib')
    return html.find_all('img', 
       {'src': re.compile(r'\.\./img/gifts/img.*\.jpg')}) # . matches . as character.
  except AttributeError:
    return None

if __name__ == "__main__":
  url = 'http://www.pythonscraping.com/pages/page3.html'
  html = getHtml(url)
  #tags = getChildren(html)
  tags = getGiftImg(html)

  if html and tags and False:
    for child in tags.children: 
      # find_all だとリストが返させれるから、.chidrenメソッドをそのまま呼び出せないことに注意.
      print(child)

    print(len((list(tags.children)))) #>>> 2
    print(len(list(tags.descendants))) #>>> 87

  if html and tags and False:
    for bro in tags.tr.next_siblings:
      print(bro) 
      # trタグを前から順に取得. 上のは tbodyを一気に取得.　
      # タイトル行はnextからなので含まれない.

  if html and tags:
    for img in tags:
      print(img.attrs['src']) # access to attributes
  else:
    print('An error has occured')
  