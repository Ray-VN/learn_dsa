
##############
# Method 1
##############
# class Solution(object):
#     def majorityElement(self, nums):
#         sum_list = {}
#         key_value, temp_max_value = 0, 0
#         for num in nums:
#             if num in sum_list:
#                 sum_list[num]+=1
#             else:
#                 sum_list[num]=1

#         for value in sum_list:
#             if sum_list[value] > temp_max_value:
#                 key_value = value
#                 temp_max_value = sum_list[value]
#         return key_value
    
# nums = [3,2,3]
# so = Solution()
# print(so.majorityElement(nums))


##############
# Method 2
##############
# class Solution(object):
#     def majorityElement(self, nums):
#         count = {}
#         max_count = 0
#         result = None
        
#         for num in nums:
#             count[num] = count.get(num, 0) + 1
#             if count[num] > max_count:
#                 max_count = count[num]
#                 result = num
                
#         return result

# nums = [3,2,3]
# so = Solution()
# print(so.majorityElement(nums))


##############
# Method 3
##############
class Solution(object):
    def majorityElement(self, nums):
        count = {}
        max_count = 0
        result = None
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if max_count < count[num]:
                max_count = count[num]
                result = num
        return result
    
nums = [3,2,3]
so = Solution()
print(so.majorityElement(nums))

