n=int(input())
ar=list(map(int,input().strip().split()))
c=0
b=0
for i in range(n):
    if ar[i]%2!=0:
        c=c+1
    if i%2!=0:
        if ar[i]%2!=0:
            b=b+1
if c==b:
    print(True)
else:
    print(False)