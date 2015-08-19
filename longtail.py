#!/usr/bin/env python2

import numpy as np
import pylab as pl
x = [1, 2, 3, 4, 5]# Make an array of x values
y = [1, 4, 9, 16, 25]# Make an array of y values for each x value
# pl.plot(x, y)# use pylab to plot x and y
# pl.savefig('img/a.png')
# pl.show()# show the plot on the screen

import pandas as pd
import pylab as pl
pd.read_csv('./dataset/audio_hot.index',names=['audio', 'hot'],converters={'audio':str,'hot':int}).plot(kind='bar')
pl.savefig('audio_hot.png')

