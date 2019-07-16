a=int(input())
S=list(map(int,input().split()))
count=0
for i in range(len(S)):
    for j in range(i+1,len(S)):
        for k in range(j+1,len(S)):
            if S[i]>S[j]>S[k]:
                count+=1
print(count)
