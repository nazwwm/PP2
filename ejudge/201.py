n = int(input())
s = 0
arr = list(map(int, input().split()))
for i in range(4):
    s+=arr[i]
print(s)