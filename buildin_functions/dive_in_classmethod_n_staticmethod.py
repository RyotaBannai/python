#!/usr/bin/python
# -*- coding: utf-8 -*-

class A(object):
  def foo(self, x):
    print "executing foo(%s, %s)" % (self, x)

  @classmethod
  def class_foo(cls, x):
    print "executing class_foo(%s, %s)" % (cls, x)

  @staticmethod
  def static_foo(x):
    print "executing static_foo(%s)" % x    

if __name__ == "__main__":
  a = A()
  a.foo('hi')
  a.class_foo('hii')
  a.static_foo('hiii')

  # A.foo(1) 　
  # 普通の関数に定義したメソッドはクラスから直接呼び出そうとするとエラーになるのに対し, 
  # クラスメソッドは直接呼び出せる.
  A.class_foo(1)

  # With staticmethods, neither self (the object instance) nor cls (the class) is implicitly passed as the first argument. They behave like plain functions except that you can call them from an instance or the class.

  # -> Staticmethods are used to group functions which have some logical connection with a class to the class.
  A.static_foo(11)
  # 使い所としては, class変数などの呼び出しで, selfやclsなどのboundが必要がない処理. クラスの外に出しても良いが, classに関係のある処理であるし, moduleのnamespace無いにバインドされてしまう点や, codingの"見た目"が悪いのでstaticmethodとしてクラスの中に入れておくことが良い癖である.

  # a.foo を呼び出したときに, a(インスタンスオブジェクト)は, メソッドfooにboundされるのに対して, 
  # (つまり, 引数として渡される)
  # a.class_foo を呼び出したときには, メソッドclass_foo にboundされ無い.
  # (代わりに, クラスAがclass_fooにboundされる)

  #a is bound to foo. That is what is meant by the term "bound" below:

  #print(a.foo)
  # <bound method A.foo of <__main__.A object at 0xb7d52f0c>>
  #With a.class_foo, a is not bound to class_foo, rather the class A is bound to class_foo.

  #print(a.class_foo)
  # <bound method type.class_foo of <class '__main__.A'>>

  
  ###  More Discussion ###
  """
  https://stackoverflow.com/questions/136097/difference-between-staticmethod-and-classmethod
  
  You might want to move a function into a class because it logically belongs with the class. In the Python source code (e.g. multiprocessing,turtle,dist-packages), it is used to "hide" single-underscore "private" functions from the module namespace. Its use, though, is highly concentrated in just a few modules -- perhaps an indication that it is mainly a stylistic thing. Though I could not find any example of this, @staticmethod might help organize your code by being overridable by subclasses. Without it you'd have variants of the function floating around in the module namespace. 

  Static methods are an organization/stylistic feature. Sometimes a module have many classes, and some helper functions are logically tied to a a given class and not to the others, so it makes sense not to "pollute" the module with many "free functions", and it is better to use a static method than relying on the poor style of mixing classes and function defs together in code just to show they are "related"

  One more use for @staticmethod - you can use it to remove cruft. I am implementing a programming language in Python - library-defined functions use a static execute method, where user-defined functions require instance arguments (i.e. the function body). This decorator eliminates "unused parameter self" warnings in PyCharm inspector. 
  """