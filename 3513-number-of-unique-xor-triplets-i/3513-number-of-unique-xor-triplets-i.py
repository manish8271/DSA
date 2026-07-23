class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        num = len(nums)
        if num<3:
            return num
        return 1 << num.bit_length()