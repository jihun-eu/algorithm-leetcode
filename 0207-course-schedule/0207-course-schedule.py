class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisiteMap = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            prerequisiteMap[course].append(prerequisite)

        visited = [False] * numCourses
        def isCycle(course: int) -> bool:
            nonlocal prerequisiteMap, visited
            if not prerequisiteMap[course]: return False

            if visited[course]: return True
            visited[course] = True

            for prerequisite in prerequisiteMap[course]:
                if isCycle(prerequisite): return True
            
            prerequisiteMap[course].clear()
            return False


        for course in range(numCourses):
            if isCycle(course): return False
            visited = [False] * numCourses
        
        return True