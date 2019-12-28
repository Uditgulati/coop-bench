import time
import rpy2.robjects
import numpy as np
from rpy2.robjects.packages import importr
from rpy2.robjects.vectors import StrVector

# utils = importr('utils')
# utils.chooseCRANmirror(ind=1)
# utils.install_packages(StrVector(['coop']))

coop = importr('coop')

N = 10**6

a = np.random.randint(100, size=N)
b = np.random.randint(100, size=N)

a1 = rpy2.robjects.FloatVector(range(len(a)))
b1 = rpy2.robjects.FloatVector(range(len(b)))

for i in range(len(a)):
  a1[i] = float(a[i])

for i in range(len(b)):
  b1[i] = float(b[i])

# coop pcor pearson
t1 = time.time()
res = coop.pcor(a1, b1)
t2 = time.time()

print("Time elapsed for pcor: ", t2 - t1)