import numpy as np
import fourier
#Define Function
def f(x):
    return np.sin(2*np.pi*x)


#Get the Sampled Frequency:
# sampling rate:sr
# sampling time:st
def gsf(sr,st):
    ts = 1.0/sr
    t = np.arange(0,st,ts)
    y = np.round(f(t),3)
    return y
def DFT(x):
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)
def FFT(x):
        x = np.asarray(x, dtype=complex)
        N = x.shape[0]
        x_odd = np.arange(int(N/2), dtype=complex)
        x_even = np.arange(int(N/2), dtype=complex)
        k = np.exp(-2j*np.pi/N)
        l=1
        for i in range(0,int(N/2)):
            x_odd[i]=x[2*i+1]
            x_even[i]=x[2*i]
        if N<=16:
            return DFT(x)
        else:
            x_even = FFT(x_even)
            x_odd =  FFT(x_odd)
            for i in range(int(N/2)):
                x[i]=x_even[i]+l*x_odd[i]
                x[i+int(N/2)]=x_even[i] - l*x_odd[i]
                l = l*k
            return x
x1 = [0,1,2,3,4,5,6,7]
x = [ 0.0 , 0.195 ,0.383,0.556,0.707 ,0.831, 0.924,0.981 ,1.0, 0.981,0.924  ,0.831 , 0.707 , 0.556 , 0.383 , 0.195 , 0.0   , -0.195, -0.383 ,-0.556,-0.707, -0.831 ,-0.924 ,-0.981, -1.0,   -0.981, -0.924, -0.831, -0.707, -0.556,-0.383, -0.195]
print(DFT(x1))
print(FFT(x1))
print(fourier.dft_fourier(x1))
print(np.shape(fourier.fft_fourier(x1)))
