
# decorator should come before it's called.
def webmethod(func):
  func.is_webmethod = "hahaha"
  return func

class Myclass():
  @webmethod 
  def my_func(self, arg1, arg2):
    print('im my_func! you passed args {}, {}'.format(arg1, arg2))

if __name__ == "__main__":
  myclass = Myclass()
  print(myclass.my_func.is_webmethod)