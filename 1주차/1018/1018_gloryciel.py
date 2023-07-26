K,N = input().split()
K=int(K);N=int(N)

own=[]
for i in range(0,K):
    tmp = int(input())
    own.append(tmp)

left = 1;right = max(own)
while(left<=right):
    mid = (left+right)//2
    cnt = 0
    for x in own:
        cnt=cnt+(x//mid)
    if(cnt>=N):
        left=mid+1
    else:
        right = mid-1
print(right)
