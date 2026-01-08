# https://leetcode.com/problems/shuffle-the-array/description/


class Solution(object):
    def shuffle(self, nums, n):
        x = []
        _range = range(n)
        
        for i in _range:
            x.append(nums[i])
            x.append(nums[i + n])

        return x

        
so = Solution().shuffle([2,5,1,3,4,7], 3)


