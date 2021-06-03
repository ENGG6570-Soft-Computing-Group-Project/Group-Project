import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand


class TracePlot:
    def __init__(self, target_list, robot_tracy_list):
        self.target_list = target_list
        self.robot_tracy_list = robot_tracy_list
        self.num_target = len(target_list)
        self.num_robots = len(robot_tracy_list)
        self.num_movements  = len(robot_tracy_list[0])
        self.axisLimits = self.findAxisLimits()
        self.robotPlot = self.plotRobotTracy()
# find the range of x, y axis from the input data
    def findAxisLimits(self):
        xMax = -np.inf
        xMin = np.inf
        yMax = -np.inf
        yMin = np.inf
        for i in range(self.num_target):
            x, y = self.target_list[i]
            if x > xMax:
                xMax = x
            if x < xMin:
                xMin = x
            if y > yMax:
                yMax = y
            if y < yMin:
                yMin = y
        for j in range(self.num_robots):
            for k in range(self.num_movements):
                x,y = self.robot_tracy_list[j][k]
                if x > xMax:
                    xMax = x
                if x < xMin:
                    xMin = x
                if y > yMax:
                    yMax = y
                if y < yMin:
                    yMin = y

        return [xMin-0.08, xMax+0.08, yMin-0.08, yMax+0.08]
    def preparePlot(self):
        plt.axis(self.axisLimits)
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.title("The Trace of Robots")
        x, y = np.asarray(self.target_list).T
        plt.scatter(x, y, color="green", s=100, marker="s")
        return plt
    def plotRobotTracy(self):
        newplt = self.preparePlot()
        cmap = [np.random.rand(self.num_robots,) for _ in range(self.num_robots)]
        for i in range(self.num_robots):
            x0,y0 = self.robot_tracy_list[i][0]
            newplt.plot(x0, y0, color= cmap[i], marker="o", markersize=8)
            x, y = np.asarray(self.robot_tracy_list[i]).T
            plt.plot(x, y, color = cmap[i], marker="o", markersize=3)
        return newplt

    def getNumRobots(self):
        return self.num_robots






