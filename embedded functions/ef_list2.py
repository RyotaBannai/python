#!/usr/bin/python
# -*- coding: utf-8 -*-

#callable(): 引数のオブジェクトが呼び出し可能オブジェクトかどうかを判定して、True / False を返却. 実用的には、()をつけて実行することができるオブジェクトであるか. 
# 呼び出し可能オブジェクトの例としては, 関数、クラス、__call__ が実装されたクラスのインスタンスがある.
# callable(sum) >>> True, callable(sum([1,2,3])) >>> False

class callMe(object):
  def __call__(self):
    print("Thanks you for calling me!")

# chr(): 整数を引数にとり、Unicodeのコードポイントがその引数の値である文字を返却
# 引数は0～1,114,111の区間をとり、範囲外の値の場合はValueErrorを起こす.
# 0xを頭につけると16進数で渡せるので扱いやすい.
# chr(0x1F31D) >>> '🌝'

# classmethod() : クラス定義内で利用され ,通常のメソッドをクラスメソッドに変換. -> 主にインスタンス化する方法を, __init__ の他にも定義したい時に使う.
# これにより、メソッドはクラスインスタンスではなく, クラスに対して束縛される.
# 通常はデコレータ@を使って表現されるが, もちろん使わない書き方も可.
# クラスメソッドの第一引数にはクラスオブジェクト自身が暗黙に渡されるため, 慣例として第一引数はclsと書くことが多い.
# https://python.ms/classmethod-and-staticmethod/#%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB
# @staticmethodはインスタンス, クラスの操作はできない. 尚, 普通のメソッドはどちらも操作可能.

# compile(): 引数に渡したソースをコードオブジェクトかASTオブジェクトに変換します。変換結果はexec()で実行したりeval()で評価したりすることができます。
#ASTとは抽象構文木(Abstract Syntax Tree)の略で、Pythonインタプリタがプログラムを解析して生成する内部的なデータ構造を指します。
#compileはいろいろな引数を受け取るのですが、必須の引数はsource, filename, modeの3つです。sourceは文字列、バイト列、ASTオブジェクトのいずれかを渡すことができます。ASTオブジェクトについてはastモジュールを利用して生成するのが一般的です。
#filenameは、sourceの読み出し元のファイル名を渡しますが、ファイルがない場合は'<string>'を使う場合が多いとのことです。modeは、'exec', 'eval', 'single'のいずれかを渡す. 
# mode 引数は、コンパイルされるコードの種類を指定する. source が一連の文から成るなら 'exec' 、単一の式から成るなら 'eval' 、単一の対話的文の場合 'single' です。(後者の場合、評価が None 以外である式文が印字されます)。
# code = compile('print("Hello")', filename='<string>', mode='eval')
# exec(code)
# code = compile('"Hello"', filename='<string>', mode='single')

class cmethod(object):
  def __init__(self, val):
    self.val = val
    
  @classmethod
  def whatever(cls, secondarg):
      return "The first param is..."+cls.__name__+"\nAnd the second one is..."+secondarg
  
  @staticmethod
  def changeVal(self):
    print('You can\'t change the value of class!!')

class cmethod2(object):
  def whatever(cls):
    print(cls.__name__)
  whatever = classmethod(whatever)


if __name__ == "__main__":
  print(('-'*4+'{:^10}'+'-'*4).format('call'))
  callme = callMe()
  print(callable(callMe()))
  callme()
  print(('-'*4+'{:^10}'+'-'*4).format('classmethod'))
  second = cmethod("Hi!!")
  print(second.whatever('anything!'))
  second.changeVal('')
  print(second.val)

  #dict
  # dictionaryはkeyは重複できないので, keyに対して複数のvaluesを指定したいなら, valueをlistにする.
  # 追加が必要なときごとに, dictをscriptingして append() で追加. 
  # defaultdictionryを使えば, 初めて出てきたkeyに対して, 初めからappend()を使用できる.
  
  """
  default_factory を int にすると, defaultdict を(他の言語の bag や multisetのように)要素の数え上げに便利に使うことができる.
  最初に文字が出現したときは, マッピングが存在しないので default_factory 関数が int() を呼んでデフォルトのカウント0を生成する. インクリメント操作が各文字を数え上げる. d['apple'] += 1 を初めから呼び出せる.

  defaultdict を set に設定することで, defaultdict をセットの辞書を作るために利用することができる.
  [('blue', {2, 4}), ('red', {1, 3})]
  """

  """
  dictionaryをupdateするときなど, valueが足りない時がある.
  この場合errorを返す代わりに, default値を入れたい場合もdefaultdictが使える.
  def constant_factory(value):
    return lambda: value
  d = defaultdict(constant_factory('<missing>'))
  d.update(name='John', action='ran')
  '{}.format['name'] 
  >>> 'John'
  '{}.format['name_'] 
  >>> '<missing>'
  """
  keys = {2: 'grape', 1: 'orange', 0: 'apple'}
  fruits = {
    0: {'num':3, 'from': 'Aomori'}, 
    2: {'num':20, 'from': 'Yamanasi'},
    1: {'num':6, 'from': 'California'}, 
    }
  # sorted(key.items(), key = lambda kv:(kv[0], kv[1]))
  inventory = dict([*zip(
    [key[1] for key in sorted(keys.items(), key = lambda kv:(kv[0], kv[1]))], 
    [fruits[data] for data in sorted(fruits)])
    ])
  print(inventory)