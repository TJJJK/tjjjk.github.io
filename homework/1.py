# -*- coding: utf-8 -*-
# 抽样函数及其傅里叶变换

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import mpl_toolkits.axisartist as axisartist
font = {'family':'SimHei'}
matplotlib.rc('font',**font)
matplotlib.rcParams['axes.unicode_minus']=False
fig = plt.figure()
# 第一个图
plt.subplot(1,2,1)# 画布分为一列两行，取第一个
matplotlib.rcParams['axes.unicode_minus']=False
fig = plt.figure()
# 第一个图
plt.subplot(1,2,1)
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
t = np.arange(-16,16,0.1)
y = np.sin(t)/t
plt.title(r'$Sa(t)=\frac{\sin(t)}{t}$',fontsize=14)
plt.text(0,-0.06,'O',fontdict={'size':16})
plt.text(16.5,-0.06,'t',fontdict={'size':14})
plt.xticks([])
plt.yticks([])
plt.plot(t,y,'b')
plt.show()

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
t = np.arange(-11,11,0.1)
y = np.sin(t)/t
plt.title(r'$Sa(t)=\frac{\sin(t)}{t}$',fontsize=14)
plt.text(0,-0.06,'O',fontdict={'size':16})
plt.text(11,-2,r'$\omega_0$',fontdict={'size':14})
plt.plot(t,np.fft.fft(y),'b')# 傅里叶变换
plt.show()

