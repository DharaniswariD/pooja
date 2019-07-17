N=int(input())
S=list(map(int,input().split()))
for i in S:
    if S.count(i)>1:
        print(i)
        break
else:
print("unique")
