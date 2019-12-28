import os
import time
import numpy as np
import rpy2.robjects


N = 10**6

a = np.random.randint(100, size=N).tolist()
b = np.random.randint(100, size=N).tolist()

a1 = rpy2.robjects.FloatVector(range(len(a)))
b1 = rpy2.robjects.FloatVector(range(len(b)))

for i in range(len(a)):
  a1[i] = float(a[i])

for i in range(len(b)):
  b1[i] = float(b[i])

R_cor_test = rpy2.robjects.r['cor.test']

# Pearson
t1 = time.time()
res = R_cor_test(a1, b1)
t2 = time.time()

print("Time elapsed for R_cor_test pearson: ", t2 - t1)