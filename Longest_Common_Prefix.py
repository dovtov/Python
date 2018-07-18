# Write a function to find the longest common prefix string 
# amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
# All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        min_str_len = min(len(s) for s in strs) 
        if min_str_len == 0:
            return ""
        for ichr in range(min_str_len):
            char = strs[0][ichr]
            for istr in range(1,len(strs)):
                if strs[istr][ichr] != char:
                    if ichr == 0:
                        return ""
                    else:
                        return strs[0][0:ichr]
        return strs[0][0:min_str_len]