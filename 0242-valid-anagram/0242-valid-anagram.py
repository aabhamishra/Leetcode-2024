class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        s_hash = {}
        for char in s:
            s_hash[char] = s_hash.get(char, 0) + 1
        
        for char in t:
            val = s_hash.get(char, 0)
            if val == 0:
                return False
            s_hash[char] = val - 1
        
        return True
        


        
        