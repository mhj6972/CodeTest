import math
def isPrime(n):
  if n<2:
    return False
  else:
    for i in range(2,int(math.sqrt(n))+1):
      if n % i == 0:
        return False

  return True

answer = []
while True:
  n = int(input())
  if n==0: break
  answer.append(n)
      
for j in answer:
  for i in range(3,j):
    # print(isPrime(i), i , j)
    if isPrime(i) and isPrime(j-i):
      print(f'{j} = {i} + {j-i}')
      break
    # else:
    #   print("Goldbach's conjecture is wrong.")
