import numpy as np

from hashlib import sha1

a = [1337, 31337]

n = np.array(a)

n = n / 2 +20 * 0.2

print(sha1(np.sum(n)).hexdigest())