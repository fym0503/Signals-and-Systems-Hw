'''
    this is the code written by FYM
    this is the impletetion of the first question using fft package
'''
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.exp(-1*np.pi*x*x)
plt.figure(figsize=(12,16))
plt.suptitle("fft of N=1000  using the fft package by numpy")
x_base=np.array([0.001*i for i in range(0,1000)])
x_scale=np.array([i for i in range(0,1000)])
x=f(x_base)
x_transform=np.fft.fft(x)
ax1=plt.subplot(221)
ax1.set_title("origianl signal")
plt.plot(x_base,f(x_base))
ax2=plt.subplot(222)
ax2.set_title("fft signal")
plt.plot(x_scale,x_transform)
ax3=plt.subplot(223)
ax3.set_title("the recovered signal")
plt.plot(x_base,np.fft.ifft(x_transform))
plt.show()
