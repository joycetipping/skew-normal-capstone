# Written by Joyce Tipping <joyce@joycetipping.com>
# License: MIT <http://www.opensource.org/licenses/mit-license.php>

from __future__ import division
import math

def lhs (skew):
  # The left-hand-side is a decreasing function of the skew parameter
  a = 2 / math.pi
  b = skew**2 / (1 + skew**2)
  return (1 - a*b)**3 / (a * b**3 * (2*a - 1)**2)

def rhs (n, p):
  # The right-hand-side is a constant in n and p
  return n * p * (1 - p) / (1 - 2*p)**2

def sn_skew (n, p):
  if (p == 0.5): return 0
  else:
    rhs = n * p * (1 - p) / (1 - 2*p)**2

    # Find upper and lower bounds (a, b)
    a = b = 1
    while (lhs(a) < rhs): a /= 2
    while (lhs(b) > rhs): b += 1

    # Calculate the skew (to within 0.00001) by repeatedly bisecting our range
    error = 0.01
    skew = (a + b) / 2
    skew_too_big   = lhs(skew) < rhs - error
    skew_too_small = lhs(skew) > rhs + error
    while (skew_too_big or skew_too_small):
      if (skew_too_big):
        b = skew
        skew = (a + b) / 2
      elif (skew_too_small):
        a = skew
        skew = (a + b) / 2
      skew_too_big   = lhs(skew) < rhs - error
      skew_too_small = lhs(skew) > rhs + error
      print '{0:.2f} & {1:.3f} & {2:.4f} & {3:.4f} & {4} & {5}'.format(a, b, skew, lhs(skew), skew_too_big, skew_too_small)

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
