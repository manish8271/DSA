class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_ele_occurence = {char: idx for idx, char in enumerate(s)}
        stack = []
        seen = set()
        for idx, char in enumerate(s):
            if char in seen:
                continue
            while stack and stack[-1]>char and last_ele_occurence[stack[-1]]>idx:
                delete_char = stack.pop()
                seen.remove(delete_char)
            stack.append(char)
            seen.add(char)
        return "".join(stack)
        