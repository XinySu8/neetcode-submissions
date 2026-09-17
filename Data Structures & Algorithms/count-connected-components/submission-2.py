class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        ans = 0
        visit = [False] * n


        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for nei in adj[node]:
                if visit[nei] == False:
                    visit[nei] = True
                    dfs(nei)
        
        for i in range(n):
            if visit[i] == False:
                visit[i] = True
                dfs(i)
                ans += 1
        return ans

        #唯一没有写成功的就是判断什么时候哦component（ans）应该 +1