import numpy as np

# a = np.random.randn(5)
# print(a)
# print(a.shape)
# print(a.T)
# print(np.dot(a, a.T))

# a = np.random.randn(5, 1)
# print(a)
# print(a.shape)
# print(a.T)
# print(np.dot(a, a.T))

a = np.random.randn(1, 5)
print(a)
print(a.shape)
print(a.T)
print(np.dot(a, a.T))

assert (a.shape == (1, 5))