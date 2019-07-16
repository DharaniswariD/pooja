d,s=input().split()
d=int(d)
s=int(s)
P=[]
for c in range(d+1,s):
  sum=0
  temp=c
  while(temp!=0):
    s=temp%10
    sum+=s**3
    temp//=10
  if(c==sum):
    P.append(c)
print(*P)
