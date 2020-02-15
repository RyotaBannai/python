# -*- coding: utf-8 -*-

class Dog(object):
  def __init__(self, name, blood, sex, secret):
    self.name = name
    self.blood = blood
    self.sex = sex
    self.__secret = secret

if __name__ == "__main__":
  # eval(): evaluate statemet, so you can't pass assignment. assignemnt is for exec()
  print(eval("2**3"))
  exec("import math; x=math.pi; print(format(x, '*^11.5f'))") # exec only evaluates Python scripts, thus exec function returns None.

  #compileした結果を, eval()に渡して, compileされたpython scriptの変数に後から埋め込むことができる.
  #evalで, globals, localsを渡すことでスコープを制御することができる.
  code = "doubled = x*2; print(doubled)"
  result = compile(code, '<string>', mode='exec')
  strx = 'x'
  exec(result, {strx:10})

  logic = lambda x: x%3==0 #you can pass function as well.
  filtered = list(filter(logic, range(1,10)))
  print(filtered)

  #exec returns None, so you can't filter iterable object like this way below.
  logic2 = compile("lambda x: x%3==0", '<string>', mode='exec')
  filtered2 = list(filter(exec(logic2), range(1,10)))

  #frozenset is immutable so can't be changed by .add(), .discard()
  fset = frozenset((1, 3, 3, 4, 4, 5))
  print(fset | {10,9,8}) #>>> result becomes frozenset as well.
  print(fset & {1,3,10})

  data = dict(name='Pochi', blood='-A', sex='male', secret='he is lovely.')
  my_dog = Dog(**data)
  print(getattr(my_dog, 'name'))
  print(getattr(my_dog, '_Dog__secret')) #You shouldn't get class private variable

  # globals() returns global variables. global scope is not where the file excutes file, but where variables are declared.
  import g_variables as gv
  x = 'This is called from main.'
  gv.my_print_globals('x') 
  # if you don't define x at not this file, but g_variables, the system returns ERROR,
  # since that means that there is no global variable named 'x'.
  gv.my_print_globals('__name__')
  print(globals())