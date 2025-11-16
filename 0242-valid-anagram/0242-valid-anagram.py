class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        s_map = {}

        for char in s:
            s_map[char] = s_map.get(char, 0) + 1
        
        for char in t:
            if char not in s_map:
                return False
            if s_map.get(char, 0) == 0:
                return False
            s_map[char] = s_map[char] - 1
        
        return True
            