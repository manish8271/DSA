class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        digits = "123456789"
        ans = []
        for i in range(2,10):
            for j in range(10-i):
                num = int(digits[j:j+i])
                if low <= num <= high:
                    ans.append(num)
        return ans

        