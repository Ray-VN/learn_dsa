class Solution(object):
    def containsDuplicate(self, nums):
        count1 = len(nums)
        count2 = len(set(nums))
        return True if count1 > count2 else False
        