N,K = input().split()
N = int(N)
K = int(K)
s = list(map(int,input().strip().split()))
sum = 0
for i in range(1,k+1):
  sum = sum + i
print(sum)
