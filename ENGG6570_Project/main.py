import TracePlot
import TaskGenerator
import numpy as np
import BruteForceSolution as BFS

tasklist = TaskGenerator.GenerateTask(5,5)
print("The task list is:")
print(tasklist)
robotList = TaskGenerator.GenerateRobot(5,5)
print("The robot position list is:")
print(robotList)
Solution = BFS.BruteForceSolution(tasklist,robotList)
RobotTrace = Solution.GenerateRobotPath()
RobotMoveCode = Solution.sorted_arrangement_dist_list[0][0]
print(RobotMoveCode)
Solution.getDistanceHistogram()
myPlot = TracePlot.TracePlot(tasklist, RobotTrace)
print(myPlot.num_robots)
print(myPlot.num_target)
print(myPlot.num_movements)
a = myPlot.robotPlot
a.show()