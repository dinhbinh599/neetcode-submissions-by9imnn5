class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)
        isBigger = None
        l = 0
        res = 1
        
        for r in range(len(arr) - 1):
            if arr[r] == arr[r+1]:
                l = r + 1
                isBigger = None
                continue
                
            valid, newIsBigger = self.isValidTurbulence(isBigger, arr[r], arr[r+1])
            if not valid:
                l = r
                # After resetting l, we need to recalculate the state for the new start
                _, newIsBigger = self.isValidTurbulence(None, arr[r], arr[r+1])
            isBigger = newIsBigger
            res = max(res, r - l + 2)

        return res


    def isValidTurbulence(self, isBigger: Optional[bool], firstVal: int, secondVal: int) -> (bool, Optional[bool]):
        if isBigger == None:
            return (True, firstVal > secondVal)
        elif isBigger:
            return (firstVal < secondVal, False)
        else: # isBigger is False (meaning previous was smaller)
            return (firstVal > secondVal, True)