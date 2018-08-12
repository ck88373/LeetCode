class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []
        for num_hour in range(0, 12):
            for num_min in range(0, 60):
                if bin(num_hour).count("1") + bin(num_min).count("1") == num:
                    result.append("%d:%02d" % (num_hour, num_min))
        return result


if __name__=="__main__":
    print(Solution().readBinaryWatch(2))
