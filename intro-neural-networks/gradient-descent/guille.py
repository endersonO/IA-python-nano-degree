import numpy as np
w1 = input("W1 :")
w2 = input("W2 :")
b = input("b :")
y=w1*0.4+w2*0.6+b
yy=1/(1+np.exp(-y))
print(y)
print(yy)