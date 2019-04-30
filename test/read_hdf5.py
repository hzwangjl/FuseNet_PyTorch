# -*- coding: utf-8 -*-

import h5py

f=h5py.File('./nyu_test.h5')
print(f['rgb_test'].shape)
print(f['depth_test'].shape)
print(f['label_test'].shape)
