#-*- using:utf-8 -*-
import time

#Checkout the difference b/w yield and returns
def Myfunc(x:int):
  for y in range(x):
    yield y*2 #return each single time

def Myfunc2(x:int):
  mylist = []
  for y in range(x):
    mylist.append(y*2)
  return mylist #return everything at once # what if this list's size is 1,000x 1,000?

start = time.time()
for i in Myfunc(1000):
  print(i, end=', ')
elapsed_time = time.time() - start
print ('\n', elapsed_time, 'sec')

# ちなみにイテレータを使うとき, 
# generatorでは中に書いたprint()の, その内容が表示されるのに対し,
# 普通の関数では表示されない.