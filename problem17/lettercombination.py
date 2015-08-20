__author__ = 'hongtao'
class Solution:
    num2char = [[" "], [""], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"]
                ,["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], [ "w", "x", "y", "z"]]

    def generateAns(self, digit, tmp, ans):
        if digit == "":
            ans.append(tmp)
            return
        for char in self.num2char[int(digit[0])]:
            tmp += char
            self.generateAns(digit[1:], tmp, ans)
            tmp = tmp[0:len(tmp)-1]

    def letterCombinations(self, digit):
        ans = []
        tmp = ""
        if digit == "":
            return ans
        self.generateAns(digit, tmp, ans)
        return ans


    # def letterCombinations(self, digit):
    #     num2char = [[" "], [""], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"]
    #                 ,["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "z"]]
    #     ans = []
    #
    #     i = 0
    #     while i < len(digit):


solution = Solution()
print solution.letterCombinations("23")


