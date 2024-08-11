"""class Solution(object):
    def nearestExit(self, maze, entrance):
        
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        
        #if len(maze) <= 1 or len(maze[0]) <= 1:
            #return -1
        visited = []  
        queue = [entrance]  
        steps = 0
        minus = -1
        allmin = 0
        while queue:
            node = queue.pop(0) 
            #print("node",node)
            #print("queue",queue)
            #print("visited",visited)
            if node not in visited:
                visited.append(node)
                if (node[0] == 0 or node[0] == len(maze)-1 or node[1] == 0 or node[1] == len(maze[0])-1) and node !=entrance:
                    #print(node)
                    return steps
                else:
                    #print(node)
                    #steps += 1
                    #print("steps",steps)
                    minus = -1
                    if node[0]-1 >= 0:
                        neighbor = [node[0]-1, node[1]]
                        if maze[neighbor[0]][neighbor[1]] == '.':
                            queue.append(neighbor)
                            minus += 1   
                    if node[1]+1 < len(maze[0]):
                        neighbor = [node[0],node[1]+1]
                        if maze[neighbor[0]][neighbor[1]] == '.':
                            queue.append(neighbor)
                            minus += 1
                    if node[0]+1 < len(maze):
                        neighbor = [node[0]+1,node[1]]
                        if maze[neighbor[0]][neighbor[1]] == '.':
                            queue.append(neighbor)
                            minus += 1
                    if node[1]-1 >= 0:
                        neighbor = [node[0],node[1]-1]
                        if maze[neighbor[0]][neighbor[1]] == '.':
                            queue.append(neighbor)
                            minus += 1
                    print("steps",steps)
                    print("minus", minus)
                    if minus > 0:
                        #steps -= minus-1
                        allmin += minus-1
                    print("queue",queue)
                    print("visited",visited)
                    print("allmin",allmin)
                    print("---")
                steps += 1
                    

        return -1
        """
"""
class Solution(object):
    def nearestExit(self, maze, entrance):
        visited = set()
        queue = [(entrance[0], entrance[1], 0)]
        while queue:
            x, y, steps = queue.pop(0)
            visited.add((x, y))
            if steps > 0 and (x != entrance[0] or y != entrance[1]) and (x == 0 or x == len(maze) - 1 or y == 0 or y == len(maze[0]) - 1):
                return steps
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == '.' and (nx, ny) not in visited:
                    queue.append((nx, ny, steps + 1))
        return -1
"""
from collections import deque
class Solution(object):
    def nearestExit(self, maze, entrance):
        rows, cols = len(maze), len(maze[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'  # Marking the entrance as visited

        while queue:
            x, y, steps = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '.':
                    if nx == 0 or nx == rows - 1 or ny == 0 or ny == cols - 1:
                        return steps + 1  # Found an exit

                    maze[nx][ny] = '+'  # Mark as visited
                    queue.append((nx, ny, steps + 1))

        return -1  # No exit found
