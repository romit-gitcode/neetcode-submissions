class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False

        count_s1, count_s2 = {}, {}
        for i in range(len(s)):
            count_s1[s[i]] = 1 + count_s1.get(s[i], 0)
            count_s2[t[i]] = 1 + count_s2.get(t[i], 0)
        return count_s1 == count_s2

    