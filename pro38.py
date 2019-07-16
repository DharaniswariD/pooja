n,k = map(int,input().split())
S = list(map(int,input().split()))
count= 0
for i in S:
    if(i+k <=5):
        count+=1
print(count//3)
