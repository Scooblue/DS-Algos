![buysell](https://github.com/user-attachments/assets/54103575-e6d9-468a-b230-13ff5442ddde)


    class Solution:
      def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price
            

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit
        
        return max_profit