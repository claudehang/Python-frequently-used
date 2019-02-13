import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import numpy as np
import pandas as pd

# define some random data that emulates your indeded code:
NCURVES = 13
np.random.seed(101)
curves = [np.random.random(20) for i in range(NCURVES)]
values = range(NCURVES)

fig = plt.figure()
ax = fig.add_subplot(111)
# replace the next line
#jet = colors.Colormap('jet')
# with
jet = cm = plt.get_cmap('jet')
cNorm  = colors.Normalize(vmin=0, vmax=values[-1])
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)
print(scalarMap.get_clim())

lines = []


label_13_palette = {'void': [0.0, 0.0, 0.0],
                    'bed': [0.0, 0.0, 1.0],
                    'books': [0.9137, 0.3490, 0.1882],
                    'ceil': [0.0, 0.8549, 0.0],
                    'chair': [0.5843, 0, 0.9412],
                    'floor': [0.8706, 0.9451, 0.0941],
                    'furn': [1.0, 0.8078, 0.8078],
                    'objs': [0.0, 0.8784, 0.8980],
                    'paint': [0.4157, 0.5333, 0.8000],
                    'sofa': [0.4588, 0.1137, 0.1608],
                    'table': [0.9412, 0.1373, 0.9216],
                    'tv': [0.0, 0.6549, 0.6118],
                    'wall': [0.9765, 0.5451, 0.0],
                    'window': [0.8824, 0.8980, 0.7608]}

label_names = [x[0] for x in label_13_palette.items()]
label_rgb = [x[1] for x in label_13_palette.items()]
label_rgb_int = [[round(channel*255) for channel in class_val] for class_val in label_rgb]
label_13_palette_int = dict(zip(label_names, label_rgb_int))

df_palette = pd.DataFrame.from_dict(label_13_palette_int,
                                    orient='index',
                                    columns=['r', 'g', 'b'])
df_palette = df_palette.rename_axis("name")
df_palette.to_csv('sunrgbd_13_label_color_mapping.csv')




for idx in range(len(curves)):
    line = curves[idx]
    colorVal = scalarMap.to_rgba(values[idx])
    print(colorVal)
    my_palette.append([int(255*x) for x in colorVal[:-1]])
    colorText = (
        'color: (%4.2f,%4.2f,%4.2f)'%(colorVal[0],colorVal[1],colorVal[2])
        )
    retLine, = ax.plot(line,
                       color=colorVal,
                       label=colorText)
    lines.append(retLine)
#added this to get the legend to work
handles,labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')
ax.grid()
plt.show()
print(my_palette)