__author__ = 'hongtao'
class Solution:
    num2char = [[" "], [""], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"]
                    ,["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], [ "w", "x", "z"]]
    ans = []
    tmp = ""

    def generateAns(self, digit):
        if digit == "":
            self.ans.append(self.tmp)
            return
        for char in self.num2char[int(digit[0])]:
            self.tmp += char
            self.generateAns(digit[1:])
            self.tmp = self.tmp[0:len(self.tmp)-1]

    def letterCombinations(self, digit):
        if digit == "":
            return self.ans
        self.generateAns(digit)
        return self.ans

solution = Solution()
print solution.letterCombinations("3")


