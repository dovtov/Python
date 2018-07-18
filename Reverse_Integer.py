class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
         if x > 2**31 or x < -2**31:
            return 0
        if x >= 0:
            sign = 1
        else:
            sign = -1
            x *= -1
        reversed = 0
        while (x/10) > 0 :
            reversed = reversed*10 + x%10
            if reversed > 2**31:
                return 0
            x //= 10
        
        return reversed*sign      

