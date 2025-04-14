class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = [[] for course in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            courses[prerequisite].append(course)
            indegree[course] += 1

        queue = deque([])
        
        for course in range(len(indegree)):
            if indegree[course] == 0:
                queue.append(course)
        
        sortedTopology = []

        while queue:
            course = queue.popleft()
            
            sortedTopology.append(course)
            for nextCourse in courses[course]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)
        
        if len(sortedTopology) != numCourses:
            sortedTopology.clear()
        
        return sortedTopology