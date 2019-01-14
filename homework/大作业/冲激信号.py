# -*- coding: utf-8 -*-
# 冲激信号

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
fig = plt.figure(figsize=(6,6))
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right")
n = 0
plt.xticks([])
plt.yticks([])
plt.ylim(0,2)
plt.text(0,0.025,'O',fontdict={'size':16})
plt.text(0.001,1,'1',fontdict={'size':16})
plt.text(0.055,-0.1,r'$\omega$',fontdict={'size':16})
plt.text(0,2,r'$\delta[n]$',fontdict={'size':16})
plt.text(10,-0.05,'n',fontdict={'size':16})
plt.text(-0.0021,1,'^',fontdict={'size':16})
plt.plot([n,n],[0,1],color='black')
plt.show()
