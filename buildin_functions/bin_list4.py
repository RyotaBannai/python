# -*- coding: utf-8 -*-

class Dog(object):
  def __init__(self, name, blood, sex, secret):
    self.name = name
    self.blood = blood
    self.sex = sex
    self.__secret = secret

if __name__ == "__main__":
  #hasattr(): オブジェクトに判定したい要素があるかどうか調べる.
  data = dict(name='Pochi', blood='-A', sex='male', secret='he is lovely.')
  my_dog = Dog(**data)
  print(hasattr(my_dog, '_Dog__secret')) #private variable is also checkable!

  print(hash(my_dog))
  print(id(my_dog)) #オブジェクトの識別値を返す >>> CPythonの実装では、id値はメモリ上のアドレス値になる

  #help() : information of object. you can use for any object.
  #print(help(Dog))

  #input()ユーザーからの入力をサポート。パスワードの入力を対話的に行いたい場合はgetpassモジュールがよい。

  # 第2引数に基数を渡すことができる
  # # 2進数
  print(int('01001', 2)) # >>> 9

  # 引数に渡すオブジェクトに__int__()や__trunc__()が定義されていた場合、それらの実行結果がint()の結果として返却される.
  
  # __int__()を実装
  class MyInt(object):
    def __int__(self):
      return 42

  #__trunc__()を実装
  class MyFloat(float):
   def __trunc__(self):
     import math
     return math.ceil(self)
  print(int(MyInt())) #>>>42
  print(int(MyFloat(3.1415))) #>>>3

  #isinstance() : 指定したオブジェクトが、あるクラスのインスタンスかどうかを判定しTrue/Falseを返却します。
  # 親クラスや先祖クラスが比較対象の場合も同様に真を返します。
  print(isinstance(1, int))

  class Newint(int): pass
  print(isinstance(Newint(1), int))
  from abc import ABC
  class MyABC(ABC): pass
  print(isinstance(MyABC(), ABC))
  print(issubclass(MyABC, ABC))

  class DEF: pass

  # 仮想クラスに登録すると、DEFはMyABCの子クラスとして認識される
  MyABC.register(DEF)
  print(isinstance(DEF(), MyABC))

  # 第２引数はクラスオブジェクトのタプルを渡すこともできます。その場合、要素のいずれかが対象の親(先祖)クラスであればTrueとなります。

  #iter() returns iterable object-> you can pass lambda and function or anything.
  from collections import defaultdict
  d = defaultdict(int)
  def counter():
    global d
    d['n'] += 1
    return d['n']
  
  #generator with yieldを使えば、iter()は必要ない.　listを返す関数とか.
  for c in iter(counter, 5): #set sentinel
    print(c)