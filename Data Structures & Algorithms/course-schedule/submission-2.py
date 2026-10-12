class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = []
        # First create empty adjancy list for all courses
        for i in range(numCourses):
            adjList.append([])

        # now add neighbours for each course
        for (course, pre) in prerequisites:
            adjList[pre].append(course)

        visit = set()
        completed = set()

        def dfs(course):
            if course in visit:
                return False  # Cycle found
            
            if course in completed:
                return True  # Cycle found

            visit.add(course)
            completed.add(course)

            for nextCourse in adjList[course]:
                if not dfs(nextCourse):
                    return False

            visit.remove(course)
            
            return True
                
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True