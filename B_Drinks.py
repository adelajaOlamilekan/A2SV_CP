n = int(input())

nums = input().split(" ")
size_n = len(nums)

result = 0

for num in nums:
    result += int(num)

final_result = round(result/size_n,12)

print("%.12f" % final_result)
