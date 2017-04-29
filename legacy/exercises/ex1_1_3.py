import ad
import uncertainties

from pyprimes import nth_prime
from hashlib import sha1

a = nth_prime(70)

u = uncertainties.ufloat(a,5)

s = ad.math.sin(u.nominal_value)

print(sha1(str(s)).hexdigest())

