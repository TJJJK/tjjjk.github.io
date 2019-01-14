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

