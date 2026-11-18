import matplotlib.pyplot as plt
import numpy as np
#准备模拟数据
time = np.linspace(0,24,25)#时间从0到24，共25个点
concentration = 100*np.exp(-0.15*time)#用一个指数衰减函数模拟
#开始画图
plt.figure(figsize=(8,5))
plt.plot(time, concentration, marker='o', color='blue', label='Drug Concentration')
#加点标签更好看
plt.title('Drug Concentration Decay Curve', fontsize=14)
plt.xlabel('Time(h)',fontsize=12)
plt.ylabel('Concentrarion(mg/L)',fontsize=12)
plt.grid(True)
plt.legend()

plt.show()