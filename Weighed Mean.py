#weighed Mean
n=int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))

sum_of_w_elem = 0
for i in range(n):
    sum_of_w_elem=sum_of_w_elem+w[i]

# print(sum_of_w_elem)
sum_of_numerator = 0
for j in range(n):
    sum_of_numerator += w[j]*x[j]

# print(sum_of_numerator)

weighed_mean = sum_of_numerator/sum_of_w_elem

print("{:.1f}".format(weighed_mean))