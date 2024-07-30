![image](https://github.com/user-attachments/assets/295816d4-2bdd-444e-a6e4-e3bc80d6bad6)

    class Solution(object):
      def findClosestNumber(self, nums):
        closest = nums[0]
      
        for x in nums:
            abs_x = abs(x)
            abs_closest = abs(closest)
            if abs_x < abs_closest or (abs_x == abs_closest and x > closest):
                closest = x

        return closest
