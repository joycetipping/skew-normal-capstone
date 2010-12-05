import math

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
    return skew

def calc_sigma (n, p):
  skew = calc_skew(n, p)
  a = 2.0 / math.pi
  b = skew**2.0 / (1.0 + skew**2.0)
  return math.sqrt( n*p*(1-p) / (1 - a*b) )

def calc_mu (n, p):
  sigma = calc_sigma(n, p)
  skew  = calc_skew(n,p)
  a = 2.0 / math.pi
  b = skew**2.0 / (1.0 + skew**2.0)
  return n*p - sigma*a*b

def calc_params (n, p):
 return ( calc_mu(n, p), calc_sigma(n,p), calc_skew(n, p) )
