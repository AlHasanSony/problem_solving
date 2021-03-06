
# problem link - https://leetcode.com/problems/flood-fill/


DIRECTION = [[-1, 0], [1, 0], [0, 1], [0, -1]]
import collections

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        # number of island
       
        oldColor = image[sr][sc]
        # check if oldColor is already painted
        if oldColor != newColor:
            self.bfs(image, sr, sc, oldColor, newColor)

        return image

    def bfs(self, image, r, c, old, new):
        image[r][c] = new

        rows = len(image)
        cols = len(image[0])
        queue = collections.deque([(r, c)])

        while queue:
            x, y = queue.popleft()

            for d_x, d_y in DIRECTION:
                new_x, new_y = x + d_x, y + d_y

                # boundary check
                if 0 <= new_x < rows and \
                    0 <= new_y < cols and \
                    image[new_x][new_y] == old:
                    # change color
                    image[new_x][new_y] = new
                    queue.append((new_x, new_y))

    def floodFill_dfs(self, image, sr, sc, newColor):
        rows = len(image)
        cols = len(image[0])
        oldColor = image[sr][sc]
        # check if oldColor is already painted
        if oldColor != newColor:            
            self.dfs(image, sr, sc, rows, cols, oldColor, newColor)
        return image

    def dfs(self, image, r, c, rows, cols, color, new_color):
        # base step
        if r < 0 or r >= rows or \
           c < 0 or c >= cols or \
           image[r][c] != color:
           return 

        # do your stuff
        image[r][c] = new_color
        
        # recursive step
        self.dfs(image, r-1, c, rows, cols, color, new_color)
        self.dfs(image, r+1, c, rows, cols, color, new_color)
        self.dfs(image, r, c-1, rows, cols, color, new_color)
        self.dfs(image, r, c+1, rows, cols, color, new_color) 
        
        

#dfs