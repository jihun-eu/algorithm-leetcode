class Solution:

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        max_row = len(maze)
        max_col = len(maze[0])

        queue = [entrance]
        step = 0
        while queue:
            level_nodes = len(queue)
            for i in range(level_nodes):
                point_x, point_y = queue.pop(0)

                if maze[point_x][point_y] == "+":
                    continue

                if step > 0 and (point_x * point_y == 0 or point_x == max_row - 1 or point_y == max_col - 1):
                    return step
                maze[point_x][point_y] = "+"
                for next_point_x, next_point_y in [(point_x+1, point_y), (point_x, point_y+1), (point_x-1, point_y), (point_x, point_y-1)]:
                    if not(0 <= next_point_x < max_row and 0 <= next_point_y < max_col):
                        continue
                    queue.append([next_point_x, next_point_y])
            step += 1

        return -1
                