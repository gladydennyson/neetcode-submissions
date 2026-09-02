class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) > n -1 :
            return False
        graph = {i: [] for i in range(n)}
        visited = set()

        for u, v in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        
            
            
        def dfs(root, par):
            if root in visited:
                return False
            visited.add(root)

            for neighbor in graph[root]:
                if neighbor == par:
                    continue
                if not dfs(neighbor, root): 
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n  