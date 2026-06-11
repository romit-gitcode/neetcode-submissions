class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A=[]
        for index, num in enumerate(nums, 0):
            A.append([num, index])
        A.sort()

        i, j = 0, len(A)-1
        while i<j:
            if(A[i][0] + A[j][0]== target):
                return sorted([A[i][1], A[j][1]])
            elif (A[i][0]+A[j][0] > target):
                j-=1
            else:
                i+=1
        return []