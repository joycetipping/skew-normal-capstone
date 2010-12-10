# Written by Joyce Tipping <joyce@joycetipping.com>
# License: MIT <http://www.opensource.org/licenses/mit-license.php>
#
# This library provides helpful functions for approximating the binomial with the skew normal

from __future__ import division
from rpy import r
import math
r.library('sn')


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Binomial
#
def binomial_pmf (n, p, pairs=False):
  # Given n and p, returns a binomial pmf in two arrays of xs and ys, respectively
  # If pairs is True, it returns the pmf as an array of points
  xs = r.seq(0, n)
  ys = r.dbinom(xs, n, p)
  return pair(xs, ys) if pairs else {'xs':xs, 'ys':ys}


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Normal Approximation
#
def normal_pdf (n, p, pairs=False):
  # Given bin(n, p), returns an approximating normal pdf in two arrays of xs and ys, respectively
  # If pairs is True, it returns the pdf as an array of points
  (mu, sigma) = normal_params(n, p)
  xs = r.seq(-n/2, 1.5*n, 0.1)
  ys = r.dnorm(xs, mu, sigma)
  return pair(xs, ys) if pairs else {'xs':xs, 'ys':ys}

def normal_params (n, p):
  # Given n and p, returns the parameters of the normal approximation as a tuple (mu, sigma)
  return (n*p, math.sqrt( n*p*(1-p) ))


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Skew-normal Approximation
#
def sn_pdf (n, p, pairs=False):
  # Given bin(n, p), returns an approximating skew-normal pdf in two arrays of xs and ys, respectively
  # If pairs is True, it returns the pdf as an array of points
  (mu, sigma, skew) = sn_params(n, p)
  xs = r.seq(-n/2, 1.5*n, 0.1)
  ys = r.dsn(xs, mu, sigma, skew)
  return pair(xs, ys) if pairs else {'xs':xs, 'ys':ys}

def sn_restriction_least_n (p):
  # Given p, finds the least viable n
  return int(math.ceil( (1-2*p)**2 / (p*(1-p)) ))

def sn_restriction_p_range (n):
  # Given n, finds the upper and lower bound of viable p's
  a = 1/2
  b = 1/2 * math.sqrt(n/(n+4))
  return (a-b, a+b)

def sn_params (n, p):
  # Given bin(n, p), returns the parameters of the skew-normal approximation as a tuple (mu, sigma, skew)
 return ( sn_mu(n, p), sn_sigma(n,p), sn_skew(n, p) )

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
    while (lhs(right_bound) > rhs): right_bound *= 2

    # Calculate the skew (to within 0.00001) by repeatedly bisecting our range
    skew = (right_bound + left_bound) / 2
    diff = rhs - lhs(skew)
    while (math.fabs(diff) > 0.00001):
      if (diff > 0):
        right_bound = skew
        skew = (right_bound + left_bound) / 2
      else:
        left_bound = skew
        skew = (right_bound + left_bound) / 2
      diff = rhs - lhs(skew)

    # Determine the sign from (1 - 2p)
    if (1 - 2*p < 0): skew *= -1
    return skew

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


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# MABS
#
def mabs_sn (n, p):
  # Given bin(n, p), finds the MABS of the skew normal approximation
  (mu, sigma, skew) = sn_params(n, p)
  def diff (k): return r.pbinom(k, n, p) - r.psn(k+0.5, mu, sigma, skew)
  return max(map(diff, range(n+1)))

def mabs_normal (n, p):
  # Given bin(n, p), finds the MABS of the normal approximation
  (mu, sigma) = normal_params(n, p)
  def diff (k): return r.pbinom(k, n, p) - r.pnorm(k+0.5, mu, sigma)
  return max(map(diff, range(n+1)))


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# General helper functions
#

# Takes two equal length arrays (xs and ys) and returns an array of pairs (points)
def pair (xs, ys): return map(lambda x, y: [x, y], xs, ys)
