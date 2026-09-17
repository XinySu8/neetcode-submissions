class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #就是找让他们形成环的那条edge/deges
        n = len(edges)
        redun = []
        adj = [[] for _ in range(n + 1)]

        
        def dfs(cur, par):
            if cur in visited:
                return True
            visited.add(cur)
            for nei in adj[cur]:
                if nei == par:
                    continue
                if dfs(nei, cur):
                    return True
            return False
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = set()
            if dfs(u, -1):
                return [u, v]
        return []