class Solution:
    def isAnagram(self, first: str, second: str) -> bool:
        if len(first) != len(second):
            return False

        firstList = [s for s in first]
        for s in second:
            if s in firstList:
                firstList.remove(s)

        return len(firstList) == 0