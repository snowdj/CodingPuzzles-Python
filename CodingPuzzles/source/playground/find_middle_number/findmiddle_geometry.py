import sys

user_input = input("please give three integers, separate by space:")
print("your input is: {0}".format(user_input))
nums = user_input.split()
print(nums)

mid = nums[0]
if (nums[0] < nums[1] and nums[1] < nums[2]) or (nums[0] > nums[1] and nums[1] > nums[2]):
    mid = nums[1]
elif nums[0] < nums[1] and nums[1] > nums[2]:
    mid = nums[0] if nums[0] > nums[2] else nums[2]
elif nums[0] > nums[1] and nums[1] < nums[2]:
    mid = nums[0] if nums[0] < nums[2] else nums[2]
elif nums[0] == nums[1] or nums[0] == nums[2]:
    mid = nums[0]
else:
    # nums[1] == num[2]
    mid = nums[1]

print("middle = {0}".format(mid))
