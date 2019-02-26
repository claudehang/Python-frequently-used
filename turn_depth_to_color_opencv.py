import cv2
import numpy as np

def depth_map_to_image(depth_map_name):
    depth_map = cv2.imread(depth_map_name)
    depth_map = np.ascontiguousarray(depth_map, dtype=np.float32)
    img = cv2.normalize(depth_map, depth_map, 0, 1, cv2.NORM_MINMAX)
    img = np.array(img * 255, dtype=np.uint8)
    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    img = cv2.applyColorMap(img, cv2.COLORMAP_JET)
    return img

depth_map_name = '171.png'
color_depth_map = depth_map_to_image(depth_map_name)

cv2.imwrite('171_color.png', color_depth_map)

# for more details visit
# https://www.learnopencv.com/applycolormap-for-pseudocoloring-in-opencv-c-python/
