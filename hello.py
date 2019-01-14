# -*- coding: utf-8 -*-
# 连续时间实指数信号

# 导入模块
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
# 绘图
fig = plt.figure()# 创建画布
ax = axisartist.Subplot(fig, 111)# 创建绘图区对象ax
fig.add_axes(ax)# 将绘图区对象添加到画布中
ax.axis[:].set_visible(False)# 通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis["x"] = ax.new_floating_axis(0,-0.8)# 添加新的坐标轴
ax.axis["x"].set_axisline_style("->", size = 1.0)# 给x轴加上箭头
ax.axis["y"] = ax.new_floating_axis(1,0)# 添加y轴
ax.axis["y"].set_axisline_style("-|>", size = 1.0)#y轴加箭头
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right") # 设置x、y轴上刻度显示方向
t = np.arange(-5,5,0.1)# array([-5,-4.9,-4.8,...,4.8,4.9,5])
s = 0.5
y = np.e**(s*t)
s = -0.5
y_1 = np.e**(s*t)
s = 0
y_2 = np.e**(s*t)
plt.title(r'$x(t)=Ce^{st},s=\sigma+jw_0$',fontsize=10)# 设置标题（函数名称）
plt.xticks([])
plt.yticks([])# 设置样式
plt.ylim(-0.8,10)# 设置坐标轴范围
plt.text(0,-1.5,'0',fontdict={'size':16})# 0点位置
plt.text(5.5,-1.5,'t',fontdict={'size':16})# 字幕t的位置
plt.text(4,7,r'$\sigma>0$',fontdict={'size':16})# 当sigma>0时
plt.text(-5.5,7,r'$\sigma<0$',fontdict={'size':16})# 当sigma<0时
plt.text(0,1.3,'C',fontdict={'size':16})# c点坐标
plt.plot(t,y,'r')# 画图y
plt.plot(t,y_1,'b')# 画y2
plt.plot(t,y_2,'c')# 画y3
plt.show()


# -*- coding: utf-8 -*-
# 单位阶跃信号及其傅里叶变换

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
font = {'family':'SimHei'}
matplotlib.rc('font',**font)
matplotlib.rcParams['axes.unicode_minus']=False
fig = plt.figure()
# 第一个图
plt.subplot(1,2,1)# 画布分为一列两行，取第一个
ax = plt.gca()
plt.title(r'$u(t)=1$')
# 移动脊柱
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

t = np.arange(-10,10,0.1)# array([-10,-9.9,-9.8,...,9.8,9.9,10])
y=0*(t<0)+1*(t>=0)# 采样信号
# 坐标标识
plt.text(0,-0.08,'O',fontdict={'size':16})
plt.text(10,-0.08,'t',fontdict={'size':16})
plt.text(1,1.4,'u(t)',fontdict={'size':16})

plt.xticks([])
plt.yticks([])
plt.ylim(0,1.5)
plt.plot(t,y,'b')
# 傅里叶变化
plt.subplot(1,2,2)
ax = plt.gca()
# 移动脊柱
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', -0.5))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
# 设置画布
plt.xticks([])
plt.yticks([])

# 坐标标识
plt.text(0,-0.5,'O',fontdict={'size':16})
plt.text(0.75,-0.5,r'$\omega$',fontdict={'size':16})
plt.text(0,1,'u(t)',fontdict={'size':16})
t = np.arange(-1,1,0.1)
y=0*(t<0)+1*(t>=0)# 采样信号
plt.xlim(-0.75,0.75)
plt.ylim(-2,1)
plt.plot(t,np.fft.fft(y),'b')# 输出傅里叶变换后信号
plt.show()

# -*- coding: utf-8 -*-
#具有初始相位的正弦信号

# 导入模块
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
# 绘图
fig = plt.figure()# 创建画布
ax = axisartist.Subplot(fig, 111)# 创建绘图区对象ax
fig.add_axes(ax)# 将绘图区对象添加到画布中
ax.axis[:].set_visible(False)# 通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis["x"] = ax.new_floating_axis(0,0)# 添加新的坐标轴
ax.axis["x"].set_axisline_style("->", size = 1.0)# 给x轴加上箭头
ax.axis["y"] = ax.new_floating_axis(1,0)# 添加y轴
ax.axis["y"].set_axisline_style("-|>", size = 1.0)#y轴加箭头
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right") # 设置x、y轴上刻度显示方向
t = np.arange(-10,10,0.01)
y = np.cos(t-1)# 函数
plt.title(r'$x(t)=A\cos(wt+\phi)$',fontsize=10)
plt.xticks([])
plt.yticks([])
plt.ylim(-2,2)
# 标识
plt.text(-2.5,np.cos(-1),r'$A\cos\phi$',fontdict={'size':14})
plt.text(0,-0.15,'O',fontdict={'size':14})
plt.text(0.15,1.90,'x(t)',fontdict={'size':14})
plt.text(10,-0.15,'t',fontdict={'size':14})
plt.text(1.2,0.96,'<-------------->',fontdict={'size':14})
plt.text(np.pi,1.1,r'$T_0=\frac{2\pi}{\omega_0}$',fontdict={'size':14})
dy = 0.4
plt.errorbar(1,1,yerr=dy,fmt='o')
plt.errorbar(1+2*np.pi,1,yerr=dy,fmt='o')
plt.plot(t,y,'b')
plt.show()

# -*- coding: utf-8 -*-
# 符号函数及其傅里叶变换

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

t = np.arange(-10,10,0.1)
y=-1*(t<0)+1*(t>=0)
plt.text(0,-0.08,'O',fontdict={'size':16})
plt.text(11,-0.15,'t',fontdict={'size':16})
plt.text(-0.05,1.7,'sgn(t)',fontdict={'size':16})
plt.text(-1,1,'1',fontdict={'size':16})
plt.text(0.7,-1,'-1',fontdict={'size':16})
plt.xticks([])
plt.yticks([])
plt.ylim(-2,2)
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
t = np.arange(-10,10,0.1)
y=-1*(t<0)+1*(t>=0)
plt.text(0,-0.08,'O',fontdict={'size':16})
plt.text(2,0.01,r'$\omega$',fontdict={'size':16})
plt.text(0,1,'sgn(t)',fontdict={'size':16})
plt.xticks([])
plt.yticks([])
plt.xlim(-2,2)
plt.ylim(-2,1)
plt.plot(t,np.fft.fft(y),'b')
plt.show()

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
