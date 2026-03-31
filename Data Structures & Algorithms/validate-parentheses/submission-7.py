class Solution:
    def isValid(self, s: str) -> bool:
        matchingPair = {')':'(', '}': '{', ']': '['}
        bracketStack = []
        for c in s:
            if c in matchingPair:
                if not bracketStack or bracketStack[-1] != matchingPair[c]:
                    return False
                bracketStack.pop()
            else:
                bracketStack.append(c)

        return not bracketStack
        