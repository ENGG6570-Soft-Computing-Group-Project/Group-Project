import TracePlot
import TaskGenerator
import matplotlib.pyplot as plt
import numpy as np
import BruteForceSolution as BFS
import time


tasklist = TaskGenerator.GenerateTask(5,8)
print("The task list is:")
print(tasklist)
robotList = TaskGenerator.GenerateRobot(5,8)
print("The robot position list is:")
print(robotList)
# Count the Running time of BruteForce Method
start_time = time.time()
Solution = BFS.BruteForceSolution(tasklist,robotList)
print("--- %s seconds ---" % (time.time() - start_time))

# Make the plots
RobotTrace = Solution.GenerateRobotPath()
TracePlot = TracePlot.TracePlot(tasklist, RobotTrace)
# Create a Figure Object, and assign this object to each of the method that can create a subplot
# This is the only way how we can merge subplots into one Figure
# Each of the methods need to return the Figure object!!!
f = plt.figure(num=1, figsize=(15,10))
TracePlot.getRobotTracyPlot(f,1,2,1)
Solution.getDistanceHistogram(f,1,2,2)
plt.savefig('BruteForceMethod.png')
plt.show()