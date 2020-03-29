# Enter your code here. Read input from STDIN. Print output to STDOUT
from scipy import stats
n=int(input())
arr = list(map(int, input().split()))

# mean
sum=0
for i in range(n):
    sum+=arr[i]

m=sum/n
mean=round(m,1)
print(mean)

#median
med=arr.sort()
x1=n//2
x2=x1-1

medi=(arr[x1]+arr[x2])/2
median=round(medi,1)
#print(median)

#mode using scipy
print(int(stats.mode(arr)[0]))
