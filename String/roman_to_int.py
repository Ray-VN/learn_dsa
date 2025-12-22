class Solution(object):
    def romanToInt(self ,s):
        total = 0
        i = 0
        def value(c):
            if c == "I": return 1
            elif c == "V": return 5
            elif c == "X": return 10
            elif c == "L": return 50
            elif c == "C": return 100
            elif c == "D": return 500
            elif c == "M": return 1000
            else: return 0

        while i < len(s):
            if (value(s[i]) == 1 and value(s[i+1]) in (5, 10)) or (value(s[i]) == 10 and value(s[i+1]) in (50, 100)) or (value(s[i]) == 100 and value(s[i+1]) in (500, 1000)):
                total += value(s[i+1]) - value(s[i])
                i += 2
            else:
                total += value(s[i])
                i += 1
        return total
s = "MCMXCIV"
so = Solution()
print(so.romanToInt(s))