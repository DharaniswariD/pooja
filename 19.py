d=int(input())
f=1
if(d<0):
  print("Does not exist")
elif(d==0):
  print(1)
else:
  for i in range(1,d+1):
    f=f*i
  print(f)
