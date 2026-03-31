class Solution:
    def isAnagram(self, first: str, second: str) -> bool:
        if len(first) != len(second):
            return False

        countF, countS = {}, {}

        for i in range(len(first)):
            countF[first[i]] = 1 + countF.get(first[i], 0)
            countS[second[i]] = 1 + countS.get(second[i], 0)
        
        return countF == countS