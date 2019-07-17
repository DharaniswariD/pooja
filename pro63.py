a=input()
S=[]
for i in a:
	if i not in S:
		S.append(i)
	else:
		break
print(len(S))
