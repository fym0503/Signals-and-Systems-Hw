'''
    this is the code written by FYM
    this is the impletetion of the second question without using fft package
'''
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.exp(-1*np.pi*x*x)
def imagine_generator(n):
    return np.array([-1*np.sin(k*2*np.pi/1001*n) for k in range(-500,501)] )
def real_generator(n):
    return np.array([np.cos(k*2*np.pi/1001*n) for k in range(-500,501)])
plt.figure(figsize=(12,16))
plt.suptitle("fft of N=1001 without using the fft package by numpy")
x_base=np.array([0.001*i for i in range(-500,501)])
x_scale=np.array([i for i in range(-500,501)])
x=f(x_base)
x_transform_re=np.array([np.sum(x*real_generator(n)) for n in range(-500,501)])
x_transform_im=np.array([np.sum(x*imagine_generator(n)) for n in range(-500,501)])
x_recover_re=np.array([0.001*np.sum(x_transform_re*real_generator(n))+0.001*np.sum(x_transform_im*imagine_generator(n)) for n in range(-500,501)])
x_recover_im=np.array([-0.001*np.sum(x_transform_re*imagine_generator(n))-0.001*np.sum(x_transform_im*real_generator(n))for n in range(-500,501)])
ax1=plt.subplot(221)
ax1.set_title("origianl signal")
plt.plot(x_base,f(x_base))
ax2=plt.subplot(222)
ax2.set_title("the magnititude of fft signal")
plt.plot(x_scale,np.sqrt(x_transform_im*x_transform_im+x_transform_re*x_transform_re))
ax3=plt.subplot(223)
ax3.set_title("the phase of fft signal")
plt.plot(x_scale,np.arctan(x_transform_im/x_transform_re))
ax4=plt.subplot(224)
ax4.set_title("the magnititude of recovered signal")
plt.plot(x_base,np.sqrt(x_recover_re*x_recover_re+x_recover_im*x_recover_im))

plt.show()