#!/sgoinfre/goinfre/Perso/42-ai/anaconda3/bin/python
import numpy as np
M = np.random.randint(10, size=(4,4))
N = np.random.randint(10, size=(4,4))

R = np.dot(M,N)
for r in R:
    print(r)
