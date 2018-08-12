class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # def bi2ten(bi_str):
        #     length = len(bi_str)
        #     sum = 0
        #     a = length
        #     for i in range(length):
        #         sum += int(bi_str[i])*2**(a-i-1)
        #     return sum
        #
        # def ten2bi(ten):
        #     re = []
        #     a = ten
        #     while 1:
        #         a, b = divmod(a, 2)
        #         re.append(str(b))
        #         if a == 1:
        #             re.append(str(a))
        #             break
        #         elif a == 0:
        #             break
        #     return ''.join(re[::-1])
        # result = ten2bi(bi2ten(a)+bi2ten(b))
        # return result

        # if a == b == "0":
        #     return "0"
        return bin(int(a, 2) + int(b, 2)).split("0b")[-1]


if __name__ == "__main__":
    print(Solution().addBinary("0", '0'))