from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def get_neighbors(coord):
            row, col = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            res = []
            for i in range(len(delta_row)):
                neighbor_row = row + delta_row[i]
                neighbor_col = col + delta_col[i]
                if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0]):
                    res.append((neighbor_row, neighbor_col))
            return res
    
        visited = set()
        
        def bfs(starting_node):
            queue = deque([starting_node])
            visited.add(starting_node)
            while len(queue) > 0:
                node = queue.popleft()
                for neighbor in get_neighbors(node):
                    r, c = neighbor
                    if neighbor in visited:
                        continue
                    if grid[r][c] == "0":
                        continue
                    # Do stuff with the node if required
                    # ...
                    queue.append(neighbor)
                    visited.add(neighbor)

        number_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    number_of_islands += 1
                    bfs((i, j))
                    
        return number_of_islands

