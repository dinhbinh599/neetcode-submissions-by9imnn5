class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        result = []
        for s in strs:
            count_char = [0] * 26
            for c in s:
                count_char[ord(c) - ord('a')] += 1
            count_char_tuple = tuple(count_char)
            if count_char_tuple in my_dict:
                my_dict[count_char_tuple].append(s)
            else:
                my_dict[count_char_tuple] = [s]

        return list(my_dict.values())
        
