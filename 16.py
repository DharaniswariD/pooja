x,y=input().split()
x=int(x)
y=int(y)
S=[]
for z in range(x+1,y):
  if(z>1):
    for i in range(2,z):
      if(z%i==0):
        break
    else:
      S.append(z)
print(*S)
