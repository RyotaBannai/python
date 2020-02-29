from urllib.request import urlopen
import pprint

if __name__ == "__main__":
  txtPage = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
  pprint.pprint(str(txtPage.read(), 'utf-8'))