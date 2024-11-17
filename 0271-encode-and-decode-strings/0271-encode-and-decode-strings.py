class Solution:

    # the encode function separates the strings by adding the length of each string and "#" as a delimiter before each string in the econded version.
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            s_len = len(s)
            res = res + str(s_len) + "#" + s
        print(res)
        return res

    # the decode function goes over the encoded string.
    # when it encounters a number, it will keep track to find the length of the next word
    # once it reaches the '#' character, the algorithm understands that this is the start of the word
    # it then passess over the encoded string using the word length to keep track. 
    # finally, when it has the whole word, that word is added to the decoded list of strings.
    def decode(self, s: str) -> List[str]:
        res = []
        curr = 0
        word_len = 0

        while curr < len(s):
            if s[curr].isdigit():
                word_len = 10*word_len + int(s[curr])
                curr+=1
            elif s[curr] == '#':
                curr +=1
                word = ""
                while word_len > 0:
                    word = word + s[curr]
                    word_len -= 1
                    curr+=1
                res.append(word)
        
        return res