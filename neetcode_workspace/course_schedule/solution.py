class Solution:
    # Time: O(?)
    # Space: O(?)
    def can_finish(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
        # TODO: Implement can_finish

        reMap = {i: [] for i in range(num_courses)}
        for crs, pre in prerequisites:
            reMap[crs].append(pre)
        
        # Store all courses along the current DFS path
        visiting = set()
        
        def dfs(crs):
            if crs in visiting:
                return False
            
            if reMap[crs] == []:
                return True
            
            for neighbor in reMap[crs]:
                visiting.add(crs)
                if not dfs(neighbor):
                    return False
                visiting.remove(crs)
                reMap[crs] = []
                    
            return True
        
        #print('reMap: ', reMap)
        for c in range(num_courses):
            if not dfs(c):
                return False
        return True
