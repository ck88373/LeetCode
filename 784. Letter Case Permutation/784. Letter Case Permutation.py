class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = []
        self.checkit(S, 0, result, '')
        return result

    def checkit(self, string, index, result, path):
        if index == len(string):
            result.append(path)
            return
        if string[index].isalpha():
            self.checkit(string, index+1, result, path+string[index].upper())
            self.checkit(string, index+1, result, path+string[index].lower())
        else:
            self.checkit(string, index+1, result, path+string[index])


if __name__=="__main__":
    print(Solution().letterCasePermutation("a1b2"))





