class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        preMap = defaultdict(list)

        for crs, pre in prerequisites:
            indegree[crs] += 1
            preMap[pre].append(crs)
        
        queue = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0:
                queue.append(crs)
    
        order = []
        while queue:
            cur = queue.popleft()
            order.append(cur)
            for crs in preMap[cur]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    queue.append(crs)

        return order if len(order) == numCourses else []
