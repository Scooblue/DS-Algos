![RomantoInt](https://github.com/user-attachments/assets/98594dc7-554d-4acc-a129-71603165bc6a)

    class Solution:
      def romanToInt(self, s: str) -> int:
        
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer = x = 0

            
        while x < len(s):

            if x+1 < len(s) and (values[s[x]] < values[s[x+1]]):
               integer += (values[s[x+1]] - values[s[x]])
               x+=2
            else:
                integer += values[s[x]]
                x+=1
        
        return integer
