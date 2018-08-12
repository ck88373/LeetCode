class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        result_list = [1, 2]
        for i in range(2, n):
            result_list.append(result_list[i-2]+result_list[i-1])
        return result_list[n-1]


if __name__=="__main__":
    print(Solution().climbStairs(4))