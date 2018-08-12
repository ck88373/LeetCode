class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        import heapq
        self.myheap = nums
        heapq.heapify(self.myheap)
        self.myk = k
        size = len(nums)
        while size > k:
            heapq.heappop(self.myheap)
            size -= 1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # print("push:%d"%val)
        import heapq
        if len(self.myheap) < self.myk:
            heapq.heappush(self.myheap, val)
        elif val > self.myheap[0]:
            heapq.heapreplace(self.myheap, val)
        return self.myheap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

["KthLargest","add","add","add","add","add"]
[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]

if __name__=="__main__":
    a = KthLargest(3,[4,5,8,2])
    x = [3],[5],[10],[9],[4]
    for i in x:
        print(a.add(i[0]))
