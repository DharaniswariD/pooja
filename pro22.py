n=int(input())
a=list(map(int,input().split()))
S=[]
d=0
for i in range(0,n-2):
  for j in range(i,n,2):
    d=d+a[j]
  S.append(d)
  d=0
S.sort()
print(S[-1])
