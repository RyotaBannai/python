def test_all():
  if all( [ 1==1, 2==2, 3==3 ] ):
    return True
  else: return  False 

def test_any():
  if any( [ 1==2, 2==3, 3==4, 4==4 ] ):
    return True
  else: return False
  
if __name__ == "__main__":
  print(test_all())
  print(test_any())