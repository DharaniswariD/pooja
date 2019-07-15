P,Q=input().split()
P=int(P)
Q=int(Q)
L=[]
for i in range(P+1,Q):
  if(i%2==0):
    S.append(i)
print(*S)
