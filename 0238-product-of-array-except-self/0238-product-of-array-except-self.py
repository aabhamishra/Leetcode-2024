class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # to calculate the product of an array except a given element at each position, we use prefix and suffix arrays.
        # prefix array -> holds product of elements before that element
        # suffix array -> holds product of elements after that element
        # the result is the product of the prefix and siffux array

        # in this code, to say space, res holds the prefix array, and at the end is multiplied by the suffix array to get the right answer. 
        nums_len = len(nums)
        res = [1 for i in range(nums_len)]
        suffix = [1 for i in range(nums_len)]

        for i in range(1, nums_len):
            res[i] = res[i-1] * nums[i-1]
        
        for i in range(nums_len - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
            res[i] *= suffix[i]
        
        return res
        
        

        