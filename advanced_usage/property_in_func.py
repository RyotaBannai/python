import time


# decorator should come before it's called.
def webmethod(fn):
  fn.is_webmethod = "hahaha"
  return fn
class Myclass():
  @webmethod 
  def my_func(self, arg1, arg2):
    print('im my_func! you passed args {}, {}'.format(arg1, arg2))


def print_separator(fn):
  def my_print(rng: int = 1, target_fn = fn):
    print('the target function <{}> is being called...'.format(target_fn.__name__))
    target_fn(rng)
    print('\nthe target function has finished running...')
  return my_print

@print_separator
def my_nothn_special_fn(rng):
  for n in range(rng):
    print(n, end='', flush=True)
    time.sleep(1)

# abuse of using attributes. usually fn can't have attr this way.
def FakeObj():
  def test():
    print("foo")
  FakeObj.test = test
  return FakeObj


if __name__ == "__main__":
  myclass = Myclass()
  # print(myclass.my_func.is_webmethod)

  # x = FakeObj()
  # x.test()
  my_nothn_special_fn(2)
