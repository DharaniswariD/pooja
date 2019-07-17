p=input()
q=input()
import sys
if len(p)>len(q):
  print(1)
  sys.exit(0)
S=[]
s=''
for i in range(len(p)):
  if p[i] not in S:
    s+=p[i]
    S.append(p[i])
c=0
c=len(p)//len(s)
d=1
for i in range(2,c+1):
  if c%i==0:
    d+=1
print(d)
