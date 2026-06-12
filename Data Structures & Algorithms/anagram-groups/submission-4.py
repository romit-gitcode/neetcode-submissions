class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = {}
        # for word in strs:
        #     sorted_key = "".join(sorted(word))
        #     if(sorted_key not in res):
        #         res[sorted_key] = []
        #     res[sorted_key].append(word)
        # return list(res.values())
        res = {}
        for word in strs:
            count = [0]*26
            for letter in word:
                count[ord(letter)-ord('a')] +=1
            key_tuple = tuple(count)
            if(key_tuple not in res):
                res[key_tuple] = []
            res[key_tuple].append(word)
        return list(res.values())


