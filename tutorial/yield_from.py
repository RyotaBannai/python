#-*- using:utf-8 -*-

def MyfuncInc(x:int):
  for y in range(x):
    yield y-1

def MyfuncDec(x:int):
  for y in range(x):
    yield y+1

def MyBoth(g1, g2):
  yield from g1
  yield from g2

for i in MyBoth(MyfuncInc(5), MyfuncDec(5)):
  print(i, end=', ')