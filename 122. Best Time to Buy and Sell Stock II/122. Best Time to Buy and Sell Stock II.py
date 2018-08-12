class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                result += prices[i]-prices[i-1]
        return result


if __name__=="__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]))
