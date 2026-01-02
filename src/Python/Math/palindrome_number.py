# Given an integer x, return true if x is a palindrome, and false otherwise.


# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


class Solution(object):
    def isPalindrome(self, x):
        
        x = str(x)
        my_list = []
        for i in x:
            my_list.append(i)

        left, right = 0, len(my_list) - 1

        while left < right:
            my_list[left], my_list[right] = my_list[right], my_list[left]
            left += 1
            right -= 1

        if x == "".join(my_list): 
            return True
        return False

so = Solution()
x = -121
print(so.isPalindrome(x))