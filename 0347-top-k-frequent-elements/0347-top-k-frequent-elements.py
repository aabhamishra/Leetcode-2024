class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # initialize a frequency map: [number --> its frequency]
        freq_map = {}

        # populate frequency map
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        bucket = [[] for i in range(len(nums) + 1)]

        for key,val in freq_map.items():
            bucket[val].append(key)

        res = []
        res_len = 0

        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i] != []:
                for num in bucket[i]:
                    res.append(num)
                    res_len+=1
            
            if res_len >= k:
                break
        
        return res[0:k]
            
        

            
        