'''
    Problem: https://leetcode.com/problems/robot-room-cleaner/
    Concepts: Backtracking
    performance: 77.59% runtime, 78.07% memory
'''
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(x, y, d):
            robot.clean()
            visited.add((x, y))

            for i in range(4):
                new_d = (d + i) % 4
                new_x = x + directions[new_d][0]
                new_y = y + directions[new_d][1]

                if (new_x, new_y) not in visited and robot.move():
                    backtrack(new_x, new_y, new_d)
                    go_back()

                robot.turnRight()

        backtrack(0, 0, 0)
# class Solution:
#     def cleanRoom(self, robot):
#         """
#         :type robot: Robot
#         :rtype: None
#         """
#         # 0 - up, 1 - right, 2 - down, 3: left
#         self.curDir = 1
#         self.x, self.y = 0, 0
#         posDict = dict()
#         def changeToDir(toDir):
#             while(self.curDir != toDir):
#                 robot.turnRight()
#                 self.curDir = (self.curDir+1)%4
#             print(f'direction change to {self.curDir}')
#         def onMove():
#             if self.curDir == 0:
#                 self.y -= 1
#             elif self.curDir == 1:
#                 self.x += 1
#             elif self.curDir == 2:
#                 self.y += 1
#             else:
#                 self.x -= 1
#             print(f'moving to {self.x}, {self.y}')
            
#         def dfs():
#             x,y = self.x, self.y
#             if (x,y) not in posDict:
#                 posDict[(x,y)] = []
#             print(f'cleaning at {x},{y}')
#             robot.clean()
#             for direction in [0,1,2,3]:
#                 if direction not in posDict[(x,y)]:
#                     print(f'direction changing from {self.curDir} to {direction}. visited directions: {posDict[(x,y)]}')
#                     changeToDir(direction)
#                     if robot.move():
#                         print(f'')
#                         posDict[(x,y)].append(direction)
#                         onMove()
#                         dfs()
#         dfs()
#         print(f'{posDict}')
        