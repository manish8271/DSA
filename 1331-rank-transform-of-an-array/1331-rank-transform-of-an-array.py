class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        temp = sorted(list(set(arr)))
        pos_map = {}
        for rank, num in enumerate(temp,1):
            pos_map[num] = rank
        return [pos_map[num] for num in arr]