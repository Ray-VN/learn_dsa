

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        temp = {}
        new = {}
        for item in magazine:
            temp[item] = temp.get(item, 0) + 1

        for x in ransomNote:
            new[x] = new.get(x, 0) + 1
            if x not in magazine or new.get(x, 0) > temp.get(x, 0):
                return False
        return True
    
ransomNote = "aa"
magazine = "ab"
so = Solution()
print(so.canConstruct(ransomNote, magazine))