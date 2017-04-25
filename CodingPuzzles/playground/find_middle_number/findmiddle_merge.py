import sys

user_input = input("please give three integers, separate by space:")
print("your input is: {0}".format(user_input))
nums = user_input.split()
print(nums)

left = nums[0]
nums.pop(0)

if nums[0] > nums[1]:
    nums[0], nums[1] = nums[1], nums[0]

mid = left
if left < nums[0]:
    mid = nums[0]
elif left > nums[1]:
    mid = nums[1]
else:
    mid = left

print("middle = {0}".format(mid))
