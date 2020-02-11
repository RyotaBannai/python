def f(a, L=[]):
  L.append(a)
  return L

#print(f(1))
#print(f(2))
#print(f(3))

# [1]
# [1, 2]
# [1, 2, 3]

# もし後続の関数呼び出しでデフォルト値を呼び出したくない場合は, 
# 呼び出しのつど初期化する. 
def f2(a, L=None):
  if L is None:
    L=[]
  L.append(a)
  return L

print(f2(1))
print(f2(2))
print(f2(3))