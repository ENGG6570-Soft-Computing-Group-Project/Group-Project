import TracePlot as TP

target = [[2, 0], [0, 2]]
robot1 = [[1, 2], [0.5, 2], [0.25, 2], [0.125, 2], [0.0625, 2]]
robot2 = [[2, 2], [2, 1], [2, 0.5], [2, 0.25], [2, 0.125]]
robot3 = [[5, 5], [5, 4], [5, 3], [2, 3.5], [1.5, 1]]
robot_path = [robot1, robot2, robot3]

myPlot = TP.TracePlot(target, robot_path)
a = myPlot.robotPlot
a.show()
