import pandas as pd
import numpy as np

from hashlib import sha1
from scipy import stats

a = np.random.random(20)

p = pd.Series(a)

n = np.array(p)

s = stats.normaltest(n)

print(sha1(np.sum(s)).hexdigest())