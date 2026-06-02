class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        preMap = defaultdict(list)

        node = set()
        for pre, crs in prerequisites:
            indegree[crs]+=1
            preMap[pre].append(crs)
            node.add(pre)
            node.add(crs)
        
        queue = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)

        finish = 0
        while queue:
            cur = queue.popleft()
            finish += 1
            for crs in preMap[cur]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    queue.append(crs)
        return finish == numCourses

