n,p,q,r=map(int,input().split())
S=list(map(int,input().split()))
z=[]
for i in range(0,len(S)):
  for j in range(i,len(S)):
    for k in range(j,len(S)):
      z.append(p*S[i]+q*S[j]+r*S[k])
print(max(z))
