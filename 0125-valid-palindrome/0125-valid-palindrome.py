class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        start = 0
        end = len(s) - 1
        
        while start < end:
            while start < end and not s[start].isalpha() and not s[start].isnumeric():
                start += 1
            
            while start < end and not s[end].isalpha() and not s[end].isnumeric():
                end -= 1
            
            if not start <= end:
                return False
            
            if s[start].lower() != s[end].lower():
                print(start, " ", end)
                return False
            
            start += 1
            end -= 1
        
        return True
            

            
