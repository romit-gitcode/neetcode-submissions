class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # str_key = {}
        # for word in strs:
        #     sorted_key = "".join(sorted(word))
        #     if sorted_key not in str_key:
        #         str_key[sorted_key] = []
        #     str_key[sorted_key].append(word)
        # return list(str_key.values())

        # Soution 2:
        res = {}
        for word in strs:
            count_freq = [0]*26
            for letter in word:
                count_freq[ord(letter)- ord("a")] +=1
            key_tuple = tuple(count_freq)
            if key_tuple not in res:
                res[key_tuple] = []
            res[key_tuple].append(word)
        return list(res.values())

