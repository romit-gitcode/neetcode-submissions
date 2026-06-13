class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for n in nums:
            if n not in hashMap:
                hashMap[n] = 1
            else:
                hashMap[n] +=1
        
        res = []
        for key, cnt in hashMap.items():
            res.append([cnt, key])
        res.sort()
        
        ans = []
        for i in range(len(res) - k, len(res)):
            ans.append(res[i][1])
        return ans
        
