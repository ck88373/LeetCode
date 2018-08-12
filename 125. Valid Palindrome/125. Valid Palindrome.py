class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = "".join([i for i in s if i.isalnum() or i.isalpha()]).lower()
        return new_s == new_s[::-1]


if __name__=="__main__":
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))

