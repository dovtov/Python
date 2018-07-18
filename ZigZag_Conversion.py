#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows 
#like this: (you may want to display this pattern in a fixed font for better legibility)
#P   A   H   N    0   4   8    12
#A P L S I I G    1 3 5 7 9 11 13
#Y   I   R        2   6  10
#And then read line by line: "PAHNAPLSIIGYIR"
#Write the code that will take a string and make this conversion given a number of rows:
#Input: s = "PAYPALISHIRING", numRows = 4
#Output:    "PINALSIGYAHRPI"
#Explanation:
#P     I    N    0     6       12    
#A   L S  I G    1   5 7    11 13    
#Y A   H R       2 4   8 10    
#P     I         3     9       
#4 rows: 0 6 12; 1 5 7 11 13,  2 4 8 10; 3 9
    # i = prev idx of current row loop (init to 0):
    # 1-3-5 char in each row: i*(numRows*2 - 2) + (row-1) : numRows=4:0-6-12
    #                                                       numRows=5:0-8-16
    #                                                       numRows=6:0-10-20
    # 2-4-6 char in 2nd row: numRows - row + 3 : 4->4 ; 5->6 ; 6->8
    #                 2-4-6 char in 3nd row: i+ numRows + row - 3 : 4->4 ; 5->6 ; 6->8
    #                         6th char in 2nd row: i+ numRows*3 - 2 : 4->4 ; 5->6 ; 6->8
# 5 Rows
# P       H        0       8           16
# A     S I        1     7 9        15 17
# Y   I   R        2   6   10    14
# P L     I G      3 5     11 13
# A       N        4       12
#5 rows: 0 8; 1 7 9,  2 6 10, 3 5 11 13; 4 12

# 6 Rows
#P         R    0         10             20
#A       I I    1       9 11          19 21
#Y     H   N    2     8   12       18
#P   S     G    3   7     13    17
#A I            4 6       14 16
#L              5         15
#6 rows: 0 10;  1 9 11,  2 8 12, 3 7 13, 4 6;  5

# rows 2nd/4rd char on 2nd row      2nd/4rd char on 3nd row
# 4    :5   :11                     :4  :10
# 5    :7   :15                     :6  :14
# 6    :9   :19                     :8  :18

#3 rows: numRows+1
#4 rows: numRows+2
#5 rows: numRows+3
#6 rows: numRows+4

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #print("Input=%s (%d) %d rows" % (s, len(s), numRows))
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1
        #print(L)
        for x in s:
            L[index] += x
            #print("index=%d,step=%d,L=%s" % (index,step,L))
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)

sol = Solution()
L = sol.convert("PAYPALISHIRING", 5)
print(L)

# Input=PAYPALISHIRING (14) 5 rows
# ['', '', '', '', '']
# index=0,step=1,L=['P', '', '', '', '']
# index=1,step=1,L=['P', 'A', '', '', '']
# index=2,step=1,L=['P', 'A', 'Y', '', '']
# index=3,step=1,L=['P', 'A', 'Y', 'P', '']
# index=4,step=1,L=['P', 'A', 'Y', 'P', 'A']
# index=3,step=-1,L=['P', 'A', 'Y', 'PL', 'A']
# index=2,step=-1,L=['P', 'A', 'YI', 'PL', 'A']
# index=1,step=-1,L=['P', 'AS', 'YI', 'PL', 'A']
# index=0,step=-1,L=['PH', 'AS', 'YI', 'PL', 'A']
# index=1,step=1,L=['PH', 'ASI', 'YI', 'PL', 'A']
# index=2,step=1,L=['PH', 'ASI', 'YIR', 'PL', 'A']
# index=3,step=1,L=['PH', 'ASI', 'YIR', 'PLI', 'A']
# index=4,step=1,L=['PH', 'ASI', 'YIR', 'PLI', 'AN']
# index=3,step=-1,L=['PH', 'ASI', 'YIR', 'PLIG', 'AN']
# PHASIYIRPLIGAN
