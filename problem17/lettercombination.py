__author__ = 'hongtao'
class Solution:
    # num2char = [[" "], [""], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"]
    #             ,["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], [ "w", "x", "y", "z"]]
    #
    # def generateAns(self, digit, tmp, ans):
    #     if digit == "":
    #         ans.append(tmp)
    #         return
    #     for char in self.num2char[int(digit[0])]:
    #         tmp += char
    #         self.generateAns(digit[1:], tmp, ans)
    #         tmp = tmp[0:len(tmp)-1]
    #
    # def letterCombinations(self, digit):
    #     ans = []
    #     tmp = ""
    #     if digit == "":
    #         return ans
    #     self.generateAns(digit, tmp, ans)
    #     return ans


    def letterCombinations(self, digit):
        num2char = [[" "], [""], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"]
                    ,["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "z"]]

        if digit == "":
            return []
        stack = []
        struct = {}
        ans = []
        struct["tmp"] = ""
        struct["digit"] = digit
        struct["stage"] = 0
        struct["i"] = 0
        stack.append(struct)
        while len(stack) > 0:
            currentStruct = stack.pop()
            if currentStruct["digit"] == "":
                ans.append(currentStruct["tmp"])
                continue
            if currentStruct["stage"] == 0:
                currentStruct["stage"] = 1
                stack.append(currentStruct)

                for char in num2char[int(currentStruct["digit"][0])]:
                    newStruct = {}
                    newStruct["stage"] = 0
                    newStruct["digit"] = currentStruct["digit"][1:]
                    newStruct["tmp"] = currentStruct["tmp"] + char

                    stack.append(newStruct)
                continue
            else:
                currentStruct["tmp"] = currentStruct["tmp"][0:len(currentStruct["tmp"])-1]

        return ans








solution = Solution()
print solution.letterCombinations("234")


