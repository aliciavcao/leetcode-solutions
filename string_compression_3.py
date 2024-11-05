class Solution:
    def compressedString(self, word: str) -> str:
        compressed = ""
        count = 1
        n = len(word)
        char = word[0]
        for i in range(1,n):
            if word[i] == char and count < 9:
                count += 1
            else:
                compressed += str(count)+ char
                char = word[i]
                count = 1 
        compressed += str(count) + char
        return compressed