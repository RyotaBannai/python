from urllib.request import urlopen
from urllib.error import HTTPError # for can't find page
from urllib.error import URLError # for can't even reach out to page
from bs4 import BeautifulSoup as BS
import sys

def getHtml(url: str):
  """
    check out whether url is available or not.
    if it's aivailable, then check if tag exists.
  """
  try: 
	  html = urlopen(url)
  except (HTTPError, URLError):
	  return None
	  #return nullm break, or run Plan B
  
  try:
    html = BS(html, 'html5lib')
    return html.div
  except AttributeError:
    return None
    # return sys.exc_info()
    # return isinstance(tag, Exception)

if __name__ == "__main__":
  url = 'http://pythonscraping.com/pages/page1.html'
  tag = getHtml(url)
  if tag is not None:
    print(tag)
  else:
    print('An error has occured')
  