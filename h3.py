d=int(input())
b=list(map(int,input().split()))
S=[]
for i in range(0,d):
  if(b[i]==i):
    S.append(i)
S.sort()
if(len(S)==0):
  print('-1')
else:
print(*S)
