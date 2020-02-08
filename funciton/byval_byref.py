#-*- using:utf-8 -*-

# Python では関数を呼び出す時に引数を指定すると参照渡しが使用される.
# ただし, 関数内で, stringやintなどのimmutableなオブジェクトには値を代入できないため, そうしようとする時, 別の保管場所に新しい値を保存した上でその場所を参照するようになる.

def showid(val):
  print(id(val))

def f(n1:int, n2:int):
  print(id(n1))
  n1 = n1+1
  n2 = n2+1
  print(id(n1))

#Checkout there are two different ids
v1, v2 = 10, 20
f(v1, v2)

#print('v1 の値は: ',v1)
#print('v2 の値は: ',v2)

#both of them refer the same id
#print('-'*40)
#print(showid(v1))
#print(id(v1))


def f2(n3):
  n3[0] = 2
#Mutable => list, dict
v3 = [0, 1]

f2(v3)
print(v3)

