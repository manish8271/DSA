class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        MAX_K = 10**6 + 1
        
        freq = Counter(s)
        
        half_counts = [0] * 26
        mid_char = ""
        
        for ch, count in freq.items():
            idx = ord(ch) - ord('a')
            half_counts[idx] = count // 2
            if count % 2 == 1:
                mid_char = ch
                
        def nCr(n: int, r: int) -> int:
            if r < 0 or r > n:
                return 0
            if r == 0 or r == n:
                return 1
            if r > n - r:
                r = n - r
            res = 1
            for i in range(1, r + 1):
                res = res * (n - i + 1) // i
                if res >= MAX_K:
                    return MAX_K
            return res

        def count_arrangements(counts: list[int]) -> int:
            total = sum(counts)
            ways = 1
            for count in counts:
                if count > 0:
                    ways *= nCr(total, count)
                    if ways >= MAX_K:
                        return MAX_K
                    total -= count
            return ways

        if count_arrangements(half_counts) < k:
            return ""

        left_half = []
        half_len = sum(half_counts)
        
        for _ in range(half_len):
            for i in range(26):
                if half_counts[i] == 0:
                    continue
                
                half_counts[i] -= 1
                ways = count_arrangements(half_counts)
                
                if ways >= k:
                    left_half.append(chr(i + ord('a')))
                    break
                else:
                    k -= ways
                    half_counts[i] += 1
                    
        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]