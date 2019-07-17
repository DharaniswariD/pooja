a=int(input())
S=list(map(int,input().split()))
b=[]
for j in S:
    if S.count(j)>1:
        b.append(j)
c=set(b)
if(len(c)==0):
    print("unique")
else:
print(*c)
