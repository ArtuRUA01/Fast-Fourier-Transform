#!/usr/bin/env python
# coding: utf-8

# In[99]:


import numpy as np
import random


# In[100]:


def DFT(x):
    x = np.asarray(x, dtype=float)
    N = len(x)
    f = []
    for i in range(N):
        a = 0
        for j in range(N):
            a += x[j] * np.exp(-2j * np.pi * j * i / N)
        f.append(a)
    return f


# In[101]:


def FFT(x):
    N = len(x)
    X_even = DFT(x[::2])
    X_odd = DFT(x[1::2])
    factor = np.exp(-2j * np.pi * np.arange(N) / N)
    #     print(X_even)
    #     print(X_odd)
    #     print(factor)
    #     print(X_even + factor[:int(N/2)] * X_odd)
    #     print(X_even + factor[int(N/2):N] * X_odd)

    return np.concatenate([X_even + factor[:int(N / 2)] * X_odd, X_even + factor[int(N / 2):N] * X_odd])


# In[102]:
size = int(input('Enter size of array: '))
if size % 2 != 0:
    print('Size must be even number')
    exit()
diapason_min = int(input('Enter min number on diapason: '))
diapason_max = int(input('Enter max number on diapason: '))
x = []
inputfile = 'NumbersFFT.txt'
myfile = open(inputfile, mode='w')

for i in range(size):
    r = random.randint(diapason_min, diapason_max)
    myfile.write(str(r) + '\n')
myfile.close()

myfile = open(inputfile, mode='r')

for i in myfile:
    x.append(int(i))

x = np.array(x)

print(FFT(x))
print(np.fft.fft(x))
myfile.close()
