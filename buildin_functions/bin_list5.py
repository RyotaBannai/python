# -*- coding: utf-8 -*-

import string

month_list = ['Juanuary', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'Octorber', 'November', 'December']
target_items = ['August', 'March', 'December', 'June']

def return_num_from_month_name(month_name: str) -> int:
  global month_list
  return [ i+1 for i, s in enumerate(month_list) if month_name == s][0]

return_num_from_month_name2 = lambda s: month_list.index(s) + 1

def return_base_name(value: str) -> int:
  value_type = 10
  chr_set = set(value)
  if chr_set.issubset(set(['0','1'])): value_type = 2
  elif chr_set.issubset(set(string.octdigits)): value_type = 8
  elif chr_set.issubset(set(string.hexdigits)) or value.startswith('0x'): value_type = 16
  else : 
    pass
  return value_type

def convert_to_base10(base: int, value:str ) -> int:
  """
   b binary
   o octo
   x hex 
   X hex with Cap
  """
  if base == 2: return format(int(value, base),'d')
  elif base == 8: return format(int(value, base),'d')
  elif base == 16: return format(int(value, base),'d')
  else: 
    pass

def convert_from_d_to_uni(value: int) -> str:
  value = int(value)
  if value < 0 or 1114111 < value : return 'The value passed is out of range.'
  else:
    return chr(value) # <--> ord()

if __name__ == "__main__":

  mapped_item = map(return_num_from_month_name, target_items)
  mappped_item2 = map(return_num_from_month_name2, target_items)

  # sort by key
  myDict = {2:'Hi', 1:'Hello', 3:'Bye!'}
  sorted_by_value = sorted(myDict.items(), key=lambda x : x[1])
  sorted_by_value = dict(sorted_by_value)

  # 整数を引数にとり、Unicodeのコードポイントがその引数の値である文字を返却
  # 引数は0～1,114,111の区間をとり、範囲外の値の場合はValueError
  
  s = '1F31D'
  t = return_base_name(s)
  d = convert_to_base10(t, s)
  whatsupp = convert_from_d_to_uni(32)
  print(whatsupp)