d=int(input())
l=list(map(int,input().split()))
avg=int(d/2)
l1=l[:avg]
l2=l[avg::]
if ((sum(l1)//len(l1))==(sum(l2)//len(l2))):
    print("yes")
else:
print("no")
