def scope_test():
  def do_local():
    spam = 'local spam'
  
  def do_nonlocal():
    nonlocal spam
    spam = 'nonlocal spam'
  
  def do_global():
    global spam
    spam = 'global spam'

  spam = 'test spam'
  do_local() # the scope is only inside do_local function.
  print('1 ',spam)
  do_nonlocal() # the scope is scope_test function.
  print('2 ',spam)
  do_global() # the scope is module level. no.3 print only refers scope_test function.
  print('3 ',spam)

scope_test()
print('4 ', spam) # the scope is module level.