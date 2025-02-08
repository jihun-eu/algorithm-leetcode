class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        precourses = [[] for course in range(numCourses)]
        visited = [False] * numCourses

        for course, prerequisite in prerequisites:
            precourses[course].append(prerequisite)

        def isCycle(course: int) -> bool:
            nonlocal precourses, visited
            if not precourses[course]: return False

            if visited[course]: return True
            visited[course] = True
            
            for prerequisite in precourses[course]:
                if isCycle(prerequisite): return True

            # course is acyclic
            precourses[course].clear()
            
            return False

        for course in range(numCourses):
            visited = [False] * numCourses
            if isCycle(course): return False
        
        return True