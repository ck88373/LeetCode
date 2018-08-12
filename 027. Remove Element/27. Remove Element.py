class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = "*"
        nums.sort()
        try:
            return nums.index("*")
        except:
            return len(nums)


if __name__=="__main__":
    print(Solution().removeElement([1,4,5,6,6,5,4,5], 6))
