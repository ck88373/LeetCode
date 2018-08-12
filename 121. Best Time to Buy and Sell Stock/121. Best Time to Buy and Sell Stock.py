class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result_lookup = [0]
        for i in range(1, len(prices)):
            if prices[i] <= prices[i-1]:
                result_lookup.append(result_lookup[i-1])
                continue
            result_lookup.append(max(result_lookup[i-1], prices[i] - min(prices[:i])))
        return result_lookup[-1]


if __name__=="__main__":
    print(Solution().maxProfit([1,2,2,2,21,21,1,4]))
