class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # base case: length of nums is 0
        if not nums:
            return 0
        
        # initialize an undordered set to track all unique elements in nums
        nums_set = set(nums)

        curr_len, longest = 1, 1

        for num in nums:
            # checking if element is the start of a sequence
            if num-1 not in nums_set:
                start = num

                # update length of current sequence when consecutive elements are found
                while start + 1 in nums_set:
                    curr_len += 1
                    start += 1
            
                # updating longest sequence if needed & reseting curr_len to 1 at end of this sequence
                longest = max(curr_len, longest)
                curr_len = 1
        
        return longest

