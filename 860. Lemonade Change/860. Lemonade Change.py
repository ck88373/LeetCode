class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        lookup = {5:0,10:0}
        for i in range(len(bills)):
            if bills[i] == 5:
                lookup[5] += 1
            elif bills[i] == 10:
                if lookup[5] == 0:
                    return False
                else:
                    lookup[5] -= 1
                    lookup[10] += 1
            else:
                if lookup[10] >= 1 and lookup[5]>= 1:
                    lookup[5] -= 1
                    lookup[10] -= 1
                elif lookup[5] >= 3:
                    lookup[5] -= 3
                else:
                    return False
        return True


if __name__=="__main__":
    print(Solution().lemonadeChange([5, 5, 10, 20]))