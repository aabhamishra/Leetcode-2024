class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
                
        option_map = {}
        option_lists = {}

        for s in strs:
            s_map = {}
            for char in s:
                s_map[char] = s_map.get(char, 0) + 1
            option_map[s] = s_map
        
        for s in strs:
            mapped = 0
            for option in option_lists:
                if option_map[s] == option_map[option]:
                    option_lists[option].append(s)
                    mapped = 1
                    break
            if mapped == 0:
                option_lists[s] = [s]
        
        return list(option_lists.values())

            

                