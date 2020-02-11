def standard_arg(arg):
  print(arg)

def pos_only_arg(arg, /):
  print(arg)

def kwd_only_arg(*, arg):
  print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
  print(pos_only, standard, kwd_only)

#print(standard_arg(1))
#print(pos_only_arg(arg=1)) // >>> an error
#print(kwd_only_arg(1)) // >>> an error
print(combined_example(1, standard=2, kwd_only=3)) #standard のみpositonalでもkeywordどちらでも可能.

print('-'*40)
def f(name, /, **args):
  print ('Positional-only name', name)
  for w in args:
    print('Keyword-only '+w, args[w])

print(f(1, **{'name':2}))