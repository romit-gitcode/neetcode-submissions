class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        original= []
        for i, num in enumerate(nums, 0):
            original.append([num, i])
        original.sort()
        
        j=len(original)-1
        k=0
        for i in range(len(original)):
            if(original[k][0]+ original[j][0] == target):
                return sorted([original[k][1], original[j][1]])
            elif original[k][0]+ original[j][0] < target:
                k+=1
            else:
                j-=1
        return []
        # A = []
        # for index, num in enumerate(nums, 0):
        #     A.append([num, index])
        # # print(A)
                
        # A.sort()
        # i, j = 0, len(A)-1
        # while i<j:
        #     if(A[i][0]+A[j][0] == target):
        #         return sorted([A[i][1], A[j][1]])
        #     elif A[i][0] + A[j][0] > target:
        #         j-=1
        #     else:
        #         i+=1
        # return []
