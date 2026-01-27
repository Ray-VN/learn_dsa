# https://leetcode.com/problems/next-greater-element-i/description/

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        nums2 = {x: i for i, x in enumerate(nums2)}
        for y in nums1:
            if y in nums2:
                nums2.get(y, None)

nums1 = [4,1,2]
nums2 = [1,3,4,2]
so = Solution()
print(so.nextGreaterElement(nums1, nums2))
# Output: [-1,3,-1]