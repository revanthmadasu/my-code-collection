# https://leetcode.com/problems/flood-fill/submissions/
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        m = len(image)
        n = len(image[0])
        positions = [(sr,sc)]
        cur_pos = 0
        while(cur_pos < len(positions)):
            position = positions[cur_pos]
            cur_row = position[0]
            cur_col = position[1]
            # print(f'current position: {cur_pos}, length: {len(positions)}, coordinates: {position}, pixelColor: {image[position[0]][position[1]]}')
            if cur_row+1 < m and image[cur_row+1][cur_col] == image[position[0]][position[1]] and image[position[0]][position[1]] != newColor:
                # print(f'Block1: row:{cur_row+1}, col: {cur_col}')
                positions.append((cur_row+1, cur_col))
            if cur_col+1 < n and image[cur_row][cur_col+1] == image[position[0]][position[1]] and image[position[0]][position[1]] != newColor:
                # print(f'Block2: row:{cur_row}, col: {cur_col+1}')
                positions.append((cur_row, cur_col+1))
            if cur_row-1 >= 0 and image[cur_row-1][cur_col] == image[position[0]][position[1]] and image[position[0]][position[1]] != newColor:
                # print(f'Block3: row:{cur_row-1}, col: {cur_col}')
                positions.append((cur_row-1, cur_col))
            if cur_col-1 >= 0 and image[cur_row][cur_col-1] == image[position[0]][position[1]] and image[position[0]][position[1]] != newColor:
                # print(f'Block4: row:{cur_row}, col: {cur_col-1}')
                positions.append((cur_row, cur_col-1))
            image[position[0]][position[1]] = newColor
            positions.pop(0)
            # cur_pos += 1
        return image
mySol = Solution()
print(mySol.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
