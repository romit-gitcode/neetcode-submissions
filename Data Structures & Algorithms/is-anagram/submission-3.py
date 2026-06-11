class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        ana_dict = {}
        
        for x in s:
            if x in ana_dict:
                ana_dict[x] += 1
            else:
                ana_dict[x] = 1
        
        for y in t:
            if y in ana_dict:
                ana_dict[y] -= 1
                if ana_dict[y] < 0:
                    return False
            else:
                return False
        
        return True

        