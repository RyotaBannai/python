x = 'Variable a is in globals.py file.'

def my_print_globals(key: str)-> None:
  print(globals()[key])