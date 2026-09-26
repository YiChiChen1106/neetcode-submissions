class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count

        

        