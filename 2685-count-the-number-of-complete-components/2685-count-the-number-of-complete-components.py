class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            nodes = 1
            edge_count = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    cnt_nodes, cnt_edges = dfs(nei)
                    nodes += cnt_nodes
                    edge_count += cnt_edges

            return nodes, edge_count

        complete = 0

        for i in range(n):
            if not visited[i]:
                nodes, edge_count = dfs(i)
                edge_count //= 2  # Each edge is counted twice

                if edge_count == nodes * (nodes - 1) // 2:
                    complete += 1

        return complete