def add(num1,num2):
  """ Adding two numbers without using the + or the ++ operators"""
  if(num2==0):
    return num1
  return add((num1^num2),(num1&num2)<<1)

if __name__ == '__main__': 
  print add(4,5)
