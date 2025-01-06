class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        image_m = len(image)
        image_n = len(image[0])

        path = [(sr, sc)]
        originColor = image[sr][sc]

        if originColor == color:
            return image

        while path:
            point_r, point_c = path.pop()
            image[point_r][point_c] = color
            for r, c in [(point_r+1, point_c), (point_r, point_c+1), (point_r-1, point_c), (point_r, point_c-1)]:
                if not(0 <= r < image_m) or not(0 <= c < image_n):
                    continue
                if image[r][c] != originColor:
                    continue
                path.append((r, c))
        
        return image
                
            