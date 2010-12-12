# Python modules
import pylab
# My modules
from stats import *

def comparison (n, p):
  # Generate comparison graph

  binomial = binomial_pmf(n, p)
  normal = normal_pdf(n, p)
  sn = sn_pdf(n, p)

  #pylab.vlines(binomial['xs'], 0, binomial['ys'], color=(0, 0.5, 0, 1))
  pylab.vlines(binomial['xs'], 0, binomial['ys'])
  pylab.plot(normal['xs'], normal['ys'], '--')
  pylab.plot(sn['xs'], sn['ys'])
  pylab.savefig('py-graphs/comparison-n' + str(n) + 'p' + str(p).replace('.', ''), format='png')

comparison(25, 0.1)
