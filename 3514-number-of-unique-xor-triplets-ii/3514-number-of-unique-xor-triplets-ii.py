class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        
        
        has_pair_xor = [False] * 2048
        for i in range(len(unique_nums)):
            for j in range(i, len(unique_nums)):
                has_pair_xor[unique_nums[i] ^ unique_nums[j]] = True
                
        
        pair_xors = [val for val in range(2048) if has_pair_xor[val]]
        
        
        has_triplet_xor = [False] * 2048
        for p in pair_xors:
            for c in unique_nums:
                has_triplet_xor[p ^ c] = True
                
        
        return sum(has_triplet_xor)