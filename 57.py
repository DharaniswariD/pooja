d,s=map(str,input().split())
count=0
for i in range(0,len(d)):
    for j in range(0,len(s)):
        if d[i]==s[j]:
            count+=1
if count>=2:
    print("yes")
else:
    print("no")
