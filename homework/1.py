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
plt.plot(t,y)
plt.show()
