"""
Program to open .npy files
"""
import numpy as np
print("\nTrace_Array:-")
data=np.load("trace_array.npy")
print(data)
print(data.shape)
print("\nTextin_Array:-")
data=np.load("textin_array.npy")
print(data)
print(data.shape)
print("\nTextout_Array:-")
data=np.load("textout_array.npy")
print(data)
print(data.shape)
