def bool_return():
  """
    もしfinally節もreturn, break, or continueを持っていれば, 
    tryではなくfinallyの物が優先される.
  """
  try:
    return True
  finally:
    return False

#print(bool_return())

def justbefore():
  """
    If the try statement reaches a break, continue or return statement, 
    the finally clause will execute '''just prior''' to the break, continue or return statement's execution.
  """
  try:
    return True
  finally:
    print('Finally!')

print(justbefore())