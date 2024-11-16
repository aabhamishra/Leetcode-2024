class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        if len(strs) == 0:
            return [[""]]

        sorted_map = {}

        for s in strs:
            sorted_s = "".join(sorted(s))

            group = sorted_map.get(sorted_s, [])
            group.append(s)
            sorted_map[sorted_s] = group
        
        res = []
        for group in sorted_map.values():
            res.append(group)
        
        return res
                