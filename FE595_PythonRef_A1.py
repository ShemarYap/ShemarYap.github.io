# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 12:15:30 2019

@author: StevensUser
"""

import numpy as np
import matplotlib as plt

degree_range = (0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360)

# This tuple represents the angles of one period in a sin/cos graph

period = np.array(degree_range)* np.pi/180

# The numpy library accepts radians for the np.sin and np.cos functions
# The period object shows this conversion from degrees to rads

x1 = np.cos(period)
x2 = np.sin(period)

sincos = plt.pyplot.figure()
SCgraph = sincos.add_subplot(222)


SCgraph.scatter(period,x1, label = 'Cosine')
SCgraph.scatter(period,x2, label = 'Sine')
plt.pyplot.legend(loc = 'lower left', bbox_to_anchor =(1,0))
