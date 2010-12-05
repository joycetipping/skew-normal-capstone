# Written by Joyce Tipping <joyce@joycetipping.com>
# License: MIT <http://www.opensource.org/licenses/mit-license.php>
#
# This library includes helpful functions for approximating the binomial with the skew normal

import math
from rpy import r
r.library('sn')


def pair (xs, ys): return map(lambda x, y: [x, y], xs, ys)

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Binomial
#
def binomial_pmf (n, p, pairs=False):
  x = r.seq(0, n)
  y = r.dbinom(x, n, p)
  return pair(x, y) if pairs else {'x':x, 'y':y}


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Normal approximation
#
def normal_params (n, p):
  return ( n*p, math.sqrt(n*p*(1.0-p)) )

def normal_pdf (n, p, pairs=False):
  (mu, sigma) = normal_params(n, p)
  x = r.seq(2*mu-n, n, 0.1)
  y = r.dnorm(x, mu, sigma)
  return pair(x, y) if pairs else {'x':x, 'y':y}


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Skew normal approximation
#
def sn_skew (n, p):
  if (p == 0.5): return 0
  else:
    # The left-hand-side is a decreasing function of the skew parameter
    def lhs (skew):
      a = 2.0 / math.pi
      b = skew**2 / (1.0 + skew**2)
      return (1.0 - a*b)**3 / (a * b**3 * (2.0*a - 1.0)**2)

    # The right-hand-side is a constant in n and p
    rhs = n * p * (1.0 - p) / (1.0 - 2.0*p)**2

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

def sn_sigma (n, p):
  skew = sn_skew(n, p)
  a = 2.0 / math.pi
  b = skew**2.0 / (1.0 + skew**2.0)
  return math.sqrt( n*p*(1-p) / (1 - a*b) )

def sn_mu (n, p):
  sigma = sn_sigma(n, p)
  skew  = sn_skew(n,p)
  a = 2.0 / math.pi
  b = skew**2.0 / (1.0 + skew**2.0)
  return n*p - sigma*math.sqrt(a*b)

def sn_params (n, p):
 return ( sn_mu(n, p), sn_sigma(n,p), sn_skew(n, p) )

def sn_pdf (n, p, pairs=False):
  (mu, sigma, skew) = sn_params(n, p)
  x = r.seq(2*mu-n, n, 0.1)
  y = r.dsn(x, mu, sigma, skew)
  return pair(x, y) if pairs else {'x':x, 'y':y}
