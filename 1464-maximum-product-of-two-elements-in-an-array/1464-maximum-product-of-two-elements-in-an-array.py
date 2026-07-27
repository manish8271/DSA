class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i,j = 0,0
        for num in nums:
            if num>i:
                j = i
                i = num
            elif num > j:
                j = num
        return (i-1)*(j-1)