from SOM import SOM
import numpy as np
from matplotlib import pyplot as plt

# Training inputs for RGBcolors
colors = np.array(
    [ [1.0,0.647,0.0],
     [0., 0., 0.],
     [0., 0., 1.],
     [0., 0., 0.5],
     [0.125, 0.529, 1.0],

     [0.33, 0.4, 0.67],
     [0.6, 0.5, 1.0],
     [0., 1., 0.],
     [1., 0., 0.],

     [0., 1., 1.],
     [1., 0., 1.],
     [1., 1., 0.],
     [1., 1., 1.],

     [.33, .33, .33],
     [.5, .5, .5],
     [.66, .66, .66]])
color_names = \
    ['orange','black', 'blue', 'darkblue',
     'skyblue','greyblue', 'lilac', 'green',
     'red','cyan', 'violet', 'yellow',
     'white','darkgrey', 'mediumgrey', 'lightgrey']

# Train a 50x50 SOM with 400 iterations
# 50 行，50 列， 3维GRB 输入，训练5 epoch
num_epoch = 25
som = SOM(15, 15, 3, num_epoch)
# som.train(colors)
# The Training of a SOM is basically a map from a 3D space (R,G,B)
# to a 2-d mainfold topo-space via the similarity of the input 3D vector
# to each cell in the SOM grid
som.train_detial(colors)

# Get output grid
# check RGB color here: https://www.easyrgb.com/en/convert.php#inputFORM
image_grid = som.get_centroids()
image_grid_detial = som.get_centroids_detial()

# print(image_grid_detial[num_epoch-1])
# print("#################################")
# print(image_grid[0][0])
# print(image_grid[0][1])
# print(image_grid[1][0])
# print(image_grid[1][1])



# Plot
plt.imshow(image_grid)
titleString = 'Color SOM \n' + 'Epoch =' + str(som.get_ephoch())
plt.title(titleString)

# Map colours to their closest neurons
mapped = som.map_vects(colors)
for i, m in enumerate(mapped):
    plt.text(m[1], m[0], color_names[i], ha='center', va='center',
             bbox=dict(facecolor='white', alpha=0.5, lw=0))
plt.show()

# red color is 1,0,0
# laiplist = som.sorted_bmu_list(image_grid_detial[num_epoch - 1], [1, 0, 0])
# print(laiplist)
# second_bmu_list = SOM.sorted_second_bmu_list(laiplist)
# print("#################################")
# print(second_bmu_list)
# print("the length of the second best match unit is:", len(second_bmu_list))
# print("are they neigobor?", SOM.second_bmu_neightbor_of_bmu(laiplist))
#
# print("#################################")


# helper function to Calculate the error function:
# epoch is a number that in the range of 0 to the num_epoch (max)
# return a float number that represent the error

def calculate_error(epoch):
    error = 0
    for c in range(len(colors)):
        currentColor = colors[c]
        currentColorName = color_names[c]
        detailed_color_list = som.sorted_bmu_list(image_grid_detial[epoch], currentColor)
        if not SOM.second_bmu_neightbor_of_bmu(detailed_color_list):
            error += 1
            # print(currentColorName)
    return (error / 16)


errorlist = []
for i in range(num_epoch):
    errorlist.append(calculate_error(i))

print(errorlist)

# data to be plotted
x = range(1, num_epoch + 1)
y = errorlist

# plotting
plt.rcParams["figure.figsize"] = (3,3)
plt.plot(x, y, color="green", marker='o')
plt.xlabel('Num_epoch', fontsize=18)
plt.ylabel('Error', fontsize=16)
plt.title('Error vs Num_Epoch', fontsize = 18)
plt.show()