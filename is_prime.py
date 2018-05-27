def is_prime(x):
  if x == 0 or x == 1:
    return False
  elif x == 2:
    return True
  else:
    for n in range(2,x):
      if x % n == 0:
        print(x, "is divisable by", n )
        print(x, "is not prime")
        return False
      else:
        print(x, "is not divisable by", n )
    print(x, "is prime")
    return True

is_prime(197)