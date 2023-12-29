import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = A
C = np.array([[1, 2], [3, 4], [5, 6]])
D = np.array([[2], [3], [4]])

print(A, B, C, D)
print(A.shape)
print(B.shape)
print(C.shape)
print(D.shape)
'''
(3, 3)
(3, 3)
(3, 2)
(3, 1)
'''

E = A + B
F = A - B
G = np.dot(A, B)
H = -A
I = np.dot(A, D)
J = np.dot(A, C)

print("-" * 20)
print(E)
print("-" * 20)
print(F)
print("-" * 20)
print(G)
print("-" * 20)
print(H)
print("-" * 20)
print(I)
print("-" * 20)
print(J)
print("-" * 20)
