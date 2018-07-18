# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# Example 1:
# Input: "()"
# Output: true
# Example 2:
# Input: "()[]{}"
# Output: true
# Example 3:
# Input: "(]"
# Output: false
# Example 4:
# Input: "([)]"
# Output: false
# Example 5:
# Input: "{[]}"
# Output: true

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        node = ListNode(s[0])
        pairs = 0
        idx = 1
        while idx < len(s):
            if not self.isMatch(node.val, s[idx]):
                print("!match: node.val=%c,s[%d]=%c" % (node.val,idx,s[idx]))
                new_node = ListNode(s[idx])
                new_node.prev = node
                node.next = new_node
                node = new_node
                idx += 1
            else: # consequetive matching pair found - prev_idx goes back 1 position
                print("+match: node.val=%c,s[%d]=%c" % (node.val,idx,s[idx]))
                pairs += 1
                if node.prev == None: # reached the beginning: re-starting the list
                    if idx < len(s) - 1:
                        idx += 1           # advance to the next character to start new list
                        node = ListNode(s[idx])
                    else: 
                        break # that's it: the whole list is traversed
                else:
                    node = node.prev
                    node.next = None
                    idx += 1

        return pairs == len(s)/2

    def isMatch(self,char1, char2):
        if (char1 == '[' and char2 == ']') or \
           (char1 == '(' and char2 == ')') or \
           (char1 == '{' and char2 == '}'):
           return True
        else:
            return False

# Definition for doubly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None

sol = Solution()
#    0123456789
s = "([])"
print(sol.isValid(s))