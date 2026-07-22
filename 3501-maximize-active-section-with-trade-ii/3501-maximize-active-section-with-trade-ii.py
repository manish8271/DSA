class SparseTable:
    def __init__(self, nums: list[int]):
        self.n = len(nums)
        if self.n == 0:
            return
        log = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(log)]
        self.st[0] = list(nums)
        for i in range(1, log):
            for j in range(self.n - (1 << i) + 1):
                self.st[i][j] = max(self.st[i - 1][j], self.st[i - 1][j + (1 << (i - 1))])

    def query(self, l: int, r: int) -> int:
        if l > r or self.n == 0:
            return 0
        i = (r - l + 1).bit_length() - 1
        return max(self.st[i][l], self.st[i][r - (1 << i) + 1])
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        ones = s.count('1')
        
        zero_groups = []
        zero_group_index = [-1] * n
        
        for i, char in enumerate(s):
            if char == '0':
                if i > 0 and s[i - 1] == '0':
                    zero_groups[-1][1] += 1
                else:
                    zero_groups.append([i, 1])
            zero_group_index[i] = len(zero_groups) - 1

        if not zero_groups:
            return [ones] * len(queries)

        zero_merge_lengths = [
            zero_groups[i][1] + zero_groups[i + 1][1]
            for i in range(len(zero_groups) - 1)
        ]
        
        st = SparseTable(zero_merge_lengths)
        ans = []

        for l, r in queries:
            left = -1 if zero_group_index[l] == -1 else zero_groups[zero_group_index[l]][1] - (l - zero_groups[zero_group_index[l]][0])
            right = -1 if zero_group_index[r] == -1 else r - zero_groups[zero_group_index[r]][0] + 1
            
            end_group = zero_group_index[r] if s[r] == '1' else zero_group_index[r] - 1
            start_adj = zero_group_index[l] + 1
            end_adj = end_group - 1
            
            active_sections = ones
            
            if s[l] == '0' and s[r] == '0' and zero_group_index[l] + 1 == zero_group_index[r]:
                active_sections = max(active_sections, ones + left + right)
            elif start_adj <= end_adj:
                active_sections = max(active_sections, ones + st.query(start_adj, end_adj))

            if s[l] == '0' and zero_group_index[l] + 1 <= end_group:
                active_sections = max(active_sections, ones + left + zero_groups[zero_group_index[l] + 1][1])

            if s[r] == '0' and zero_group_index[l] < zero_group_index[r] - 1:
                active_sections = max(active_sections, ones + right + zero_groups[zero_group_index[r] - 1][1])

            ans.append(active_sections)

        return ans