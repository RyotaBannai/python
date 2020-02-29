import io
from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


class readPDF(object):
  def __init__(self, url):
    self.url = url
    print(self.url) 

  def __enter__(self):
    laparams = LAParams()
    self.rsrcmgr = PDFResourceManager()
    # four items below need to be closed at end
    self.pdfFile = urlopen(self.url)
    self.retstr = io.StringIO()
    self.device = TextConverter(self.rsrcmgr, self.retstr, codec='utf-8', laparams=laparams)
    self.fp = io.BytesIO(self.pdfFile.read())  #get a file-like binary object
    return self
  
  def convert_to_text(self):
    interpreter = PDFPageInterpreter(self.rsrcmgr, self.device)
    pagenos = set()
    args = dict(maxpages=0, password="", caching=True, check_extractable=True)
    for page in PDFPage.get_pages(self.fp, pagenos, **args):
      interpreter.process_page(page)
    stri = self.retstr.getvalue()
    return stri

  def __exit__(self, type, value, traceback):
    self.pdfFile.close()
    self.retstr.close()
    self.device.close()
    self.fp.close()

if __name__ == "__main__":
  with readPDF('http://www.pythonscraping.com/pages/warandpeace/chapter1.pdf') as PDF:
    print(PDF.convert_to_text())
  