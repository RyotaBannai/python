# -*- coding: utf-8 -*-
import sys, io, time

class Book:
  def __init__(self, name):
    self._name = name
  def _get_name(self):
    """getter"""
    return self._name
  def _set_name(self, name):
    """setter"""
    self._name = name
  def _delete_name(self):
    """deleter"""
    del self._name
  name = property(_get_name, _set_name, _delete_name, 'This is name property')

class Book2:
  def __init__(self, name):
    self._name = name
  @property
  def name(self):
    """This is name property"""
    return self._name
  @name.setter
  def name(self, name):
    """setter"""
    self._name = name
  @name.deleter
  def name(self):
    """deleter"""
    del self._name
  @property
  def uppercase(self):
    return self._name.upper()
  
if __name__ == "__main__":
  # 標準エラーに書き込み
  print('Error has occured!!', file=sys.stderr)

  # この場合だとファイルを「上書き」
  with open('output.txt', 'w') as f:
    print('hello worlds!', file=f)

  # インメモリストリームにもprintできる
  memfile=io.StringIO()
  print('hello world', file=memfile)
  # インメモリストリームは上書きではなく「追記」
  print('hello world2', file=memfile)
  print(memfile.getvalue())

  # そのままファイルに書き込む
  with open('output.txt', 'w') as f:
    print(memfile.getvalue(), file=f)
  
  # 改行がないと、出力が最後にまとめてされてしまうため、flush=Trueとして、
  # 毎回出力させる
  def count(n):
    for i in range(1, n+1):
      print(i, end='', flush=True)
      time.sleep(1)
  # count(10)

  book = Book('clean code')
  print(book.name)
  
  book2 = Book2('clean code2')
  book2.name = 'hahaha'
  print(book2.uppercase)