"""
 any useful reusable library can be this subdirectry.
"""
import sys, os, pathlib
import pprint

class BB(object):
  def __init__(self):
    print('class BB')

if __name__ == "__main__":
  osdir = os.path.dirname(os.__file__)
  print(os.__file__)
  print('*'*40)
  #print(sys.path)
  print('*'*40)
  print(__package__) # shows dot module path to this module.