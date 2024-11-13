class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_to_index = {}
 
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in num_to_index:
                return(i, num_to_index[needed])
            num_to_index[nums[i]] = i
        
        return [0,0]
            
        
        idx = 0
        for num in nums:
            if target - num in index_to_name:
                return(idx, )
        