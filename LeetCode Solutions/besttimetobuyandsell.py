from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> bool:
        #initialize sell price to first element
        sell = prices[0]
        #initialize max_profit
        max_profit = 0
        #iterate through the array
        for price in prices:
            #if the current element is less than current sell price
            if price < sell:
                sell = price
            #calculate profit
            profit = price - sell
            #if current profit is greater than max_profit
            if profit > max_profit:
                #assign max profit to larger nujber
                max_profit = profit
        #return max_profit
        return max_profit

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([7,6,4,3,1]))