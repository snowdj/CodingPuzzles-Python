import sys
import time

user_input = input("please give three integers, separate by space:")
print("your input is: {0}".format(user_input))
nums = user_input.split()
print(nums)

start_time = time.clock()

sum = 0
for i in nums:
  sum += int(i)

avg = sum / float(len(nums))

# find which number is closet to avg
min_dis = sys.maxsize * 1.0
min_pos = 0
for (p, i) in enumerate(nums):
  dis = abs(int(i) - avg)
  if dis < min_dis:
    min_dis = dis
    min_pos = p

print("middle = {0}".format(nums[min_pos]))

print("--- %s seconds ---" % (time.clock() - start_time))
