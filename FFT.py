#!/usr/bin/env python
# coding: utf-8

# In[99]:


import numpy as np


# In[100]:


def DFT(x):
    x = np.asarray(x, dtype = float)
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
    
    return np.concatenate([X_even + factor[:int(N/2)] * X_odd, X_even + factor[int(N/2):N] * X_odd])


# In[102]:


x = np.array([4,2,1,4,6,3,5,2])
print(FFT(x))
print(np.fft.fft(x))


# In[ ]:




