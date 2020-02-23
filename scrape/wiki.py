from urllib.request import urlopen
from urllib.error import HTTPError # for can't find page
from urllib.error import URLError
from bs4 import BeautifulSoup as BS
from scrapetest import *
import re
from collections import defaultdict

def getWHtml(url):
  try:
    return urlopen('https://en.wikipedia.org{}'.format(url))
  except (HTTPError, URLError):
    return None

def getLinksOnWiki(html):
  try:
    bs = BS(html, 'html5lib')
    return bs.find('div', {'id': 'bodyContent'}).find_all(
      'a', href=re.compile(r'^(/wiki/)((?!:).)*$') ) # (?!:)match all except :
  except AttributeError:
    return None

if __name__ == "__main__":
  url = '/wiki/Kevin_Bacon'

  # もしクローラを実装したい場合は、ここからwhileなど回帰文にしたり、
  # 関数として外に出して、再起的に呼び出す.
  html = getWHtml(url)
  tags = getLinksOnWiki(html)
  if html and tags:
    d = defaultdict(list)
    for l in tags:
      if 'href' in l.attrs: # there is a tag without no href 
        d['links'].append(l.attrs['href'])
    print(d)
  else:
    print('An error has occured')
  