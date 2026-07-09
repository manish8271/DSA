class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        g = [0] * n
        cnt = 0
        for i in range(1,n):
            if nums[i]-nums[i-1]>maxDiff:
                cnt += 1
            g[i] = cnt
        return [g[u]==g[v] for u,v in queries]