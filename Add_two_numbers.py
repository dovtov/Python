#You are given two non-empty linked lists representing two non-negative integers. 
#The digits are stored in reverse order and each of their nodes contain a single digit. 
#Add the two numbers and return it as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#Example
#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.

#!/usr/bin/python3.6

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, L1, L2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        print("Adding 2 linked lists:")
        cur_node = L1
        while True:
            print("-> %d " % (cur_node.val), end='', flush=True)
            if cur_node.next == None:
                print("\n")
                break
            else:
                cur_node = cur_node.next                    
        print(" and")
        cur_node = L2
        while True:
            print("-> %d " % (cur_node.val), end='', flush=True)
            if cur_node.next == None:
                print("\n")
                break
            else:
                cur_node = cur_node.next                 
        
        
        # Assume that at least one, root node, exists in each Lined List
        carryover = 0
        next_carryover = 0
        ret_node_val = L1.val + L2.val 
        if ret_node_val > 9:
            ret_node_val -= 10 
            carryover = 1
        ret_linked_list = ListNode(ret_node_val)
        ret_prev_node = ret_linked_list

        while True:
            if L1.next == None and L2.next == None:
                # Both Linked Lists ended: check if a carryover 1 left after the last addition
                # then add an aditional node with value 1
                if carryover == 1:
                    ret_node = ListNode(1)
                    ret_prev_node.next = ret_node
                # Return resulting Linked List 
                break

            # At least one of Linked Lists still continues:        
            if L1.next == None:
                val1 = 0
            else:
                L1 = L1.next
                val1 = L1.val

            if L2.next == None:
                val2 = 0
            else:
                L2 = L2.next
                val2 = L2.val
                

            ret_node_val = val1 + val2 + carryover
            if ret_node_val > 9:
                ret_node_val -= 10 
                next_carryover = 1
            else:
                next_carryover = 0

            ret_node = ListNode(ret_node_val)
            ret_prev_node.next = ret_node
            ret_prev_node = ret_node
            carryover = next_carryover

        return (ret_linked_list)



# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
L1 = ListNode(2)
L1.next = ListNode(4)
L1.next.next = ListNode(3)
L2 = ListNode(5)
L2.next = ListNode(6)
L2.next.next = ListNode(4)

sol = Solution()
ret_linked_list = sol.addTwoNumbers(L1, L2)

ret_node = ret_linked_list
print("The sum is:")
while True:
    print("-> %d " % (ret_node.val), end='', flush=True)
    if ret_node.next == None:
        print("\n")
        break
    else:
        ret_node = ret_node.next                     
