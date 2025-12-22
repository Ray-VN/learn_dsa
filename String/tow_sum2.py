##################
# Version 1
##################
# class Solution(object):
#     def twoSum(self, nums, target):
#         count = 0
#         range_ = range(len(nums))
#         for i in range_: # 0 - 3
#             for y in range_:
#                 if count == y:
#                     continue
#                 if target == nums[count]+nums[y]:
#                     return [count, y]
#                     # print(f"{nums[count]} + {nums[y]} = {nums[count]+nums[y]}")
#             count += 1

##################
# Version 2
##################

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            need = target - num

            if need in seen:
                return [i, seen[need]]
            seen[num]=i
            

# 11 - 2 = 9:0
# 11 - 7 = 4:1
# 11 - 4 = 7
2, 
target = 11
nums = [2,7, 4, 11,15]

so = Solution()

print(so.twoSum(nums, target))



# 2 7, 2 11, 2 15
# 7 2, 7 11, 7 15
# 11 2, 11 7, 11 15
# 15 2, 15 7, 15 11


# 2 7, 2 11, 2 15, 7 11, 7 15,  15 11