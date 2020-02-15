#!/usr/bin/python
# -*- coding: utf-8 -*-

def test_all():
  return True if all( [ 1==1, 2==2, 3==3 ] ) else False

def test_any():
  #三項演算子
  return True if any( [ 1==2, 2==3, 3==4, 4==4 ] ) else False

def ternary_op_elif(x:int) -> str:
  #三項演算子でelif
  return 'x is 1' if x==1 else 'x is x' if x==2 else 'x is neither 1 nor 2' 

# ascii(): repr()と同じように可能であればeval()で評価すると引数と同様のオブジェクトになる文字列を, そうでない場合# は、<>で囲まれたオブジェクトの情報を返却. 
# repr()との違いは非ASCII文字が\x \u \U を使ってユニコードのコードポイントとしてエスケープされるということ.  
# ascii("日本語") >>> "'\\u65e5\\u672c\\u8a9e'" eval("'\\u65e5\\u672c\\u8a9e'") >>> '日本語'

# bool(): 偽になる値の False, None, ,''(空文字列), 0, 0.0, [], {} など.
# オブジェクトの真偽値のデフォルトは真なので、__bool__()や__len__()を実装していないクラスのインスタンスをbool()に渡すと、返り値はTrue

class c(object):
  def __len__(self):
    return False

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
#filenameは、sourceの読み出し元のファイル名を渡しますが、ファイルがない場合は'<string>'を使う場合が多いとのことです。modeは、'exec', 'eval', 'single'のいずれかを渡します。

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
  print("test_all()>",test_all())
  print("test_any()>", test_any())
  print("ternary_op_elif()>", ternary_op_elif(1))
  print(('-'*4+'{:^10}'+'-'*4).format('bool'))
  print(bool(c()))
  print(('-'*4+'{:^10}'+'-'*4).format('call'))
  callme = callMe()
  print(callable(callMe()))
  callme()
  print(('-'*4+'{:^10}'+'-'*4).format('classmethod'))
  second = cmethod("Hi!!")
  print(second.whatever('anything!'))
  second.changeVal('')
  print(second.val)