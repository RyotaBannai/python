from urllib.request import urlopen
from urllib.error import HTTPError # for can't find page
from urllib.error import URLError # for can't even reach out to page
from bs4 import BeautifulSoup as BS
import sys

__all__ = ['getHtml']

def getHtml(url):
  """
    check out whether url is available or not.
    if it's aivailable, then check if tag exists.
  """
  try:
    return urlopen(url)
  except (HTTPError, URLError):
    return None
    #return nullm break, or run Plan B

def extractTag(html): 
  try:
    html = BS(html, 'html5lib')
    return html.div
  except AttributeError:
    return None
    # return sys.exc_info()
    # return isinstance(tag, Exception)

def extractTagByClass(html): 
  try:
    html = BS(html, 'html5lib')
    #return html.find_all('span', {'class': 'green'}) # get by attributes.
    #return html.find_all('', {'class': {'green', 'red'}}) 
    return html.find_all(class_ = ['green', 'red'])  # get by keywords

    # keyword => AND filter ex, .find_all(id='red', class_='text')
    # attribute => OR filter ex, .find_all('', {'id': 'red', 'class': 'text') 
  except AttributeError:
    return None
    
if __name__ == "__main__":
  #url = 'http://pythonscraping.com/pages/page1.html'
  url = 'https://www.pythonscraping.com/pages/warandpeace.html'
  html = getHtml(url)
  #tags = extractTag(html)
  tags = extractTagByClass(html)
  if html and tags: # If either of them returns None, then it's an error.
    #print(tags)
    for tag in tags:
      print(tag.get_text(), end=", ")
  else:
    print('An error has occured')
  