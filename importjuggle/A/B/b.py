from ...C.D.d import D

class B(object):
  def __init__(self):
    print('class B')

def main():
  B()
  # print(d.D().mySum(1,2))
  print(D.mySum(1,2))