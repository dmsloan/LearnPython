def is_prime(x):
  if x == 0 or x == 1:
    return False
  elif x == 2:
    return True
  else:
    for n in range(2,x):
      if x % n == 0:
        return False
        print("not")
      else:
        return True
        print("yes")

is_prime(3)