from statistics import median

n = int(input())
arr = list(map(int, input().split()))

# print(int(median(arr[:n//2])))
# print(int(median(arr)))
# print(int(median(arr[(n+1)//2:])))
arr.sort()
mid_val = round(n/2)

left_sum = 0
for i in range(1, mid_val-1):
    left_sum += arr[i]
print(left_sum//2)

print(int(median(arr)))


right_sum = 0
for i in range(mid_val+2, n-1):
    right_sum += arr[i]
    # print(arr[i])
print(right_sum//2)