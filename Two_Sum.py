# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#! python3

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """ Create dictionary that holds all passed through values as keys and their index in the i/c list as values """
        mydict = {}
        index = 0
        for num in nums:
            if (target - num) in mydict:
                """ The 2nd needed number to make up the target is already in the dictionary: return indices of both """
                return [mydict[target - num], index]
            else:
                """ Target sum is not found yet: fill in the entries one by one in the dictionary """
                mydict[num] = index
            index += 1

        """ We went through the whole i/c list and dud not find a pair to sum the target: return both indices -1 """
        return [-1, -1]


nums = [2, 7, 11, 15]
target = 9
sol = Solution()
twoIndices = sol.twoSum(nums, target)
if twoIndices[0] == -1:
    print("Target %d cannot be summed up by any 2 elements from the i/c list of numbers :(" % (target))
else:
    print("Target=%d is a sum of nums[%d]=%d and nums[%d]=%d" % (target, twoIndices[0], nums[twoIndices[0]], twoIndices[1], nums[twoIndices[1]]))