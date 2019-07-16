from itertools import combinations
string,num=map(int,input().split())
d=len(str(string))
S=list(combinations(str(string),d-num))
S=(sorted(S))
b="".join(S[0])
print(b)
