d=str(input())
d=d.lower()
l=len(a)
S=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(0,l):
	if(a[i] in S):
		S.remove(a[i])
if(len(S)==0):
	print("yes")
else:
	print("no")
