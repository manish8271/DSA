import math
class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        '''
        Approach
        Step 1: Sort by value, track original -> sorted mapping
        Step 2: Build jump[i][0] using two pointers
        Step 3: Build higher levels
        Step 4: Answer queries
        '''
        sorted_pairs = sorted((val,i) for i, val in enumerate(nums))
        sorted_vals = [val for val, _ in sorted_pairs]
        index_map = [0]*n
        for sorted_idx, (_, orig_idx) in enumerate(sorted_pairs):
            index_map[orig_idx] = sorted_idx
        
        max_level = n.bit_length() + 1
        jump = [[0]*max_level for _ in range(n)]

        right = 0
        for i in range(n):
            while right + 1 < n and sorted_vals[right+1]-sorted_vals[i] <= maxDiff:
                right += 1
            jump[i][0] = right
        
        for level in range(1, max_level):
            for i in range(n):
                jump[i][level] = jump[jump[i][level-1]][level-1]
        def min_jumps(start, end):
            if start == end:
                return 0
            if jump[start][max_level-1]< end:
                return -1
            jumps = 0
            for level in range(max_level - 1, -1, -1):
                if jump[start][level]<end:
                    start = jump[start][level]
                    jumps += (1 << level)
            return jumps + 1
        ans = []
        for u,v in queries:
            su,sv = index_map[u],index_map[v]
            if su > sv:
                su, sv = sv, su
            ans.append(min_jumps(su,sv))
        return ans