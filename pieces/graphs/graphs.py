import math
import json
from rpy import r

def calc_skew (n, p):
  if (p == 0.5): return 0
  else:
    # The left-hand-side is a decreasing function of the skew parameter
    def lhs (skew):
      a = 2.0 / math.pi
      b = skew**2.0 / (1.0 + skew**2.0)
      return (1.0 - a*b)**3.0 / (a * b**3.0 * (2.0*a - 1.0)**2.0)

    # The right-hand-side is a constant in n and p
    rhs = n * p * (1.0 - p) / (1.0 - 2.0*p)**2.0

    # Find upper and lower bounds
    left_bound = right_bound = 1
    while (lhs(left_bound)  < rhs): left_bound  /= 2.0
    while (lhs(right_bound) > rhs): right_bound *= 2.0

    # Calculate the skew (to within 0.00001) by repeatedly bisecting our range
    skew = (right_bound + left_bound) / 2.0
    diff = rhs - lhs(skew)
    while (math.fabs(diff) > 0.00001):
      if (diff > 0):
        right_bound = skew
        skew = (right_bound + left_bound) / 2.0
      else:
        left_bound = skew
        skew = (right_bound + left_bound) / 2.0
      diff = rhs - lhs(skew)

    # Determine the sign from (1 - 2p)
    if (1.0 - 2.0*p < 0): skew *= -1.0

    #print 'Constant:', rhs
    #print 'lhs     :', lhs(skew)
    #print 'Skew', skew
    #print
    return skew

ns = [25, 50, 75, 100]
ps = [0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9]
#map(lambda x: map(lambda y: calc_skew(x, y), ps), ns)

binomial = r.dbinom(r.seq(1,10), 10, 0.2)
print binomial
