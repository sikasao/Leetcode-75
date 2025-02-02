def mergeAlternately(word1: str, word2: str) -> str:
        res = ""
        len1 = len(word1)
        len2 = len(word2)
        for i in range(max(len1, len2)):
            if i < len1:
                res += word1[i]
            if i < len2:
                res += word2[i]
        
        return res
    
word1 = "abc"
word2 = "pqr"
print(mergeAlternately(word1, word2))