d=int(input())
fact=1
if(d<0):
  print("invalid")
elif(d==0):
  print(1)
else:
  for i in range(1,d+1):
    fact=fact*i
  print(fact)
