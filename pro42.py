N,K=map(int,input().split())
S=list(map(int,input().split()))
if K==1:
    print(min(S))
elif K==2:
    print(max(S[0],S[N-1]))
else:
print(max(S))
