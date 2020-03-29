import math
n = int(input())
x_arr = list(map(int, input().split()))

#Mean
mean_sum = 0
for i in range(n):
    mean_sum+=x_arr[i]

mean = mean_sum/n
# print(mean)

#Squared Distance
squared_distance_sum = 0
for i in range(n):
    squared_distance_sum += (x_arr[i]-mean)**2

sd = math.sqrt(squared_distance_sum/n)

print(round(sd,1))
