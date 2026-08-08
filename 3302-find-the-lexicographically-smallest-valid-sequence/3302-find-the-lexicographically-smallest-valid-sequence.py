class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        last = [-1] * m
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1
                
        result = []
        j = 0
        used_change = False
        
        for i in range(n):
            if j == m:
                break
                
            if word1[i] == word2[j]:
                result.append(i)
                j += 1
            elif not used_change:
                if j + 1 == m or last[j + 1] > i:
                    used_change = True
                    result.append(i)
                    j += 1
                    
        return result if len(result) == m else []