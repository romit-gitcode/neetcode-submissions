class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ele_dict = {}
        for ele in nums:
            if ele in ele_dict:
                return True
            else:
                ele_dict[ele] = 1
        return False

            
  
         