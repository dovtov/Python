#! python3
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
    #   s = 'abcdefg'
        start = 0
        end = 1
        ret_max = 1
        if len(s) == 0 or len(s) == 1:
            ret_max = len(s)
        else:
            for _ in s:
                if end == len(s):
                    break 
                end_char_idx = s[start:end].find(s[end])
                if end_char_idx >= 0:
                    start += end_char_idx + 1
                    end += 1 
                else:                          
                    end += 1
                if end-start > ret_max:
                    ret_max = end-start
        return ret_max

#s = 'rpatybacdefgy'
#s = 'rpatybacdae'
#s = 'atybacda'
s = 'abcdefg'
#s = 'i'
sol = Solution()
print(s, sol.lengthOfLongestSubstring(s))
