# Given a string s, find the longest palindromic substring in s. 
# You may assume that the maximum length of s is 1000.
# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
# Input: "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = 1
        strlen = len(s) 
        pal_dict = {}
        lpal = 'no palindrom substring'
        if strlen == 0:
            lpal = 'String is empty'
        elif strlen == 1:
            lpal = s
        else:
            # First loop - to look for symmetrical characters around a character, 
            # i.e. odd number of characters palindroms
            for i in range(1, strlen-1):
                left = i-1
                right = i+1
                end_range = min(i, strlen-1-i)
                for j in range(0, end_range):
                    if s[left] == s[right]:
                        pal_dict[right-left] = s[left:right+1]
                    else:
                        break
                    left -= 1
                    right +=1

            # Second loop - to look for symmetrical characters that are next to each other, 
            # i.e. even number of characters palindroms
            for i in range(1, strlen):
                left = i-1
                right = i
                end_range = min(i, strlen-i)
                for j in range(0, end_range):
                    if s[left] == s[right]:
                        pal_dict[right-left] = s[left:right+1]
                    else:
                        break
                    left -= 1
                    right +=1

        if pal_dict:
            lpal = pal_dict[max(pal_dict.keys())]
        else:
            lpal = s[strlen-1]
        return lpal

sol = Solution()
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

#s = 'abctuta'
#s = 'abctut'
#s = 'tutabc'
#s = 'notton'
#s = 'babad'
#s = 'aba'
#s = 'cbbd'
#s = 'abcdee'
#s = 'a'
#s = 'abcda'
#s = 'ccc'
lp = sol.longestPalindrome(s)
print(lp)
