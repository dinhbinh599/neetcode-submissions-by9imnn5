class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapCount = {}
        for num in nums:
            if num not in mapCount:
                mapCount[num] = 0

        startOfSequence = []
        res = 0

        for key in mapCount:
            if not key-1 in mapCount:
                startOfSequence.append(key)
        
        for startVal in startOfSequence:
            count = 1
            
            if startVal + 1 in mapCount:
                stop = False
                i = startVal + 1
                count += 1
                while not stop:
                    if i + 1 in mapCount:
                        count += 1
                        i += 1
                    else:
                        stop = True

            if count > res:
                res = count

        return res
