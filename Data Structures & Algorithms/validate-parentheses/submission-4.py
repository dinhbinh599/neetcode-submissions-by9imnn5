class Solution:
    def isValid(self, s: str) -> bool:
        bracket = []
        matchingBracket = {')':'(', '}': '{', ']' : '['}
        for st in s:
            if st == '(' or st == '{' or st == '[':
                bracket.append(st)
            elif st in matchingBracket:
                if len(bracket) == 0 or matchingBracket[st] != bracket.pop():
                    return False

        return len(bracket) == 0
                