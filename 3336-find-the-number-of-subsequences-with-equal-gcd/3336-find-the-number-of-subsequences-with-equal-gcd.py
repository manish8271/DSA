class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        @cache
        def dp(idx, gcd1, gcd2):
            if idx == n:
                return 1 if gcd1 == gcd2 and gcd1 > 0 else 0
            
            ans = dp(idx + 1, gcd1, gcd2)
            
            new_gcd1 = nums[idx] if gcd1 == 0 else math.gcd(gcd1, nums[idx])
            ans = (ans + dp(idx + 1, new_gcd1, gcd2)) % MOD
            
            new_gcd2 = nums[idx] if gcd2 == 0 else math.gcd(gcd2, nums[idx])
            ans = (ans + dp(idx + 1, gcd1, new_gcd2)) % MOD
            
            return ans

        return dp(0, 0, 0)