# Written by Joyce Tipping <joyce@joycetipping.com>
# License: MIT <http://www.opensource.org/licenses/mit-license.php>
#
# This library provides helpful functions for approximating the binomial with the skew normal

from __future__ import division
from rpy import r
import math
r.library('sn')

def sn_skew (n, p):
  # Given n and p, finds the skew parameter, lambda

  if (p == 0.5): return 0
  else:
    # The left-hand-side is a decreasing function of the skew parameter
    def lhs (skew):
      a = 2 / math.pi
      b = skew**2 / (1 + skew**2)
      return (1 - a*b)**3 / (a * b**3 * (2*a - 1)**2)

    # The right-hand-side is a constant in n and p
    rhs = n * p * (1 - p) / (1 - 2*p)**2

    # Find upper and lower bounds
    left_bound = right_bound = 1
    while (lhs(left_bound)  < rhs): left_bound  /= 2
    while (lhs(right_bound) > rhs): right_bound += 1

    print "rhs", rhs

    # Calculate the skew (to within 0.00001) by repeatedly bisecting our range
    error = 0.01
    skew = (right_bound + left_bound) / 2
    too_big = lhs(skew) < rhs - error
    too_small = lhs(skew) > rhs + error
    while (too_big or too_small):
      if (too_big):
        right_bound = skew
        skew = (right_bound + left_bound) / 2
      elif (too_small):
        left_bound = skew
        skew = (right_bound + left_bound) / 2
      too_big = lhs(skew) < rhs - error
      too_small = lhs(skew) > rhs + error
      print '{0:.2f} & {1:.3f} & {2:.4f} & {3:.4f} & {4} & {5}'.format(left_bound, right_bound, skew, lhs(skew), too_big, too_small)

    # Determine the sign from (1 - 2p)
    if (1 - 2*p < 0): skew *= -1
    return skew

sn_skew(25, 0.1)

def sn_sigma (n, p):
  # Given n and p, finds the scale parameter, sigma
  skew = sn_skew(n, p)
  a = 2 / math.pi
  b = skew**2 / (1 + skew**2)
  return math.sqrt( n*p*(1-p) / (1 - a*b) )

def sn_mu (n, p):
  # Given n and p, finds the location parameter, mu
  sigma = sn_sigma(n, p)
  skew  = sn_skew(n,p)
  c = math.sqrt( 2 / math.pi )
  d = skew / math.sqrt(1 + skew**2)
  return n*p - sigma*c*d
