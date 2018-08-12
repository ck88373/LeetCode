class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for i in nums1:
            index = nums2.index(i)
            find_larger = -1
            for j in nums2[index:]:
                if j > i:
                    find_larger = j
                    break
            result.append(find_larger)
        return result


if __name__=="__main__":
    print(Solution().nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))