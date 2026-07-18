from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums1 = sorted(nums)
        small_num = nums1[0]
        largest_num = nums1[len(nums)-1]
        ans = gcd(small_num,largest_num)
        return ans
        