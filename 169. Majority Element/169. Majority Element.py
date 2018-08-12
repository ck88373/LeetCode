class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = {}
        for i in nums:
            if i in lookup:
                lookup[i] += 1
            else:
                lookup[i] = 1
        return sorted(lookup.items(), key=lambda x: x[1], reverse=True)[0][0]


if __name__=="__main__":
    print(Solution().majorityElement([1,2,2,2,21,21,1,4]))
