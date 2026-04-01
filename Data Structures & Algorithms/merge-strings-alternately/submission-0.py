class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        L=0
        R=0
        result=""
        len_word1=len(word1)-1
        len_word2=len(word2)-1
        while L<=len_word1 and R<=len_word2:
            result += word1[L]
            result += word2[R]
            L+=1
            R+=1
        if L<=len_word1:
            print(word1[L:])
            result += word1[L:]
        elif R<=len_word2:
            print(word2[R:])
            result += word2[R:]

        return result 