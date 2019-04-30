# -*- coding: utf-8 -*-
import h5py
import numpy as np
from PIL import Image

f=h5py.File("nyu_test.h5", "w")

images = []
depths = []
labels = []

for i in range(1,6):
    image = Image.open('images/'+str(i)+'.jpg')
    image = image.resize((320, 240))
    r,g,b = image.split()
    r = np.array(r)
    g = np.array(g)
    b = np.array(b)
    image = np.array([r,g,b])
    images.append(image)

    depth = Image.open('depths/'+str(i)+'.png')
    depth = depth.resize((320, 240))
    depth = np.array(depth)
    depth = np.array([depth])
    depths.append(depth)


    label = Image.open('labels/'+str(i)+'.png')
    label = label.resize((320, 240))
    label = np.asarray(label)
    labels.append(label)

f['rgb_test'] = images
f['depth_test'] = depths
f['label_test'] = labels

f.close()
