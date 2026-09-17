class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        res = []

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()
        Correct = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if crs in Correct:
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            Correct.add(crs)
            res.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res
