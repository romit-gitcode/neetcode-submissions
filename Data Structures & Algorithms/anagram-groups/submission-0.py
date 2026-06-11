class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_key = {}
        for word in strs:
            sorted_key = "".join(sorted(word))
            if sorted_key not in str_key:
                str_key[sorted_key] = []
            str_key[sorted_key].append(word)
        return list(str_key.values())