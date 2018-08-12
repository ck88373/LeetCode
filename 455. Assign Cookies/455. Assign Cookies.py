class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count = 0
        m = -1
        for i in range(len(g)):
            for j in range(m+1, len(s)):
                if s[j] >= g[i]:
                    count += 1
                    m = j
                    break
        return count


if __name__=="__main__":
    print(Solution().findContentChildren([1,2,3,8, 9, 11], [1,1, 4, 11, 8]))
