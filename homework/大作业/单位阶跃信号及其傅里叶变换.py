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
