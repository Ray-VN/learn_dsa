# https://leetcode.com/problems/valid-anagram/submissions/

class Solution(object):
    def isAnagram(self, s, t):
        a = {}

        if len(s) != len(t):
            return False
        for x in s:
            if x in a:
                a[x] += 1   
            else:
                a[x] = 1
        for y in t:
            if a.get(y, 0) > 0:
                a[y] -= 1   
            else:
                return False

        return True

s = "rat" 
t = "car"
so = Solution()
print(so.isAnagram(s, t))