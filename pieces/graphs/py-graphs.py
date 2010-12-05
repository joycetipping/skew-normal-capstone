# Python modules
import pylab
# My modules
from stats import *

def comparison (n, p):
  # Generate comparison graph

  binomial = binomial_pmf(n, p)
  normal = normal_pdf(n, p)
  sn = sn_pdf(n, p)

  #pylab.vlines(binomial['x'], 0, binomial['y'], color=(0, 0.5, 0, 1))
  pylab.vlines(binomial['x'], 0, binomial['y'])
  pylab.plot(normal['x'], normal['y'], '--')
  pylab.plot(sn['x'], sn['y'])
  pylab.savefig('py-graphs/comparison-n' + str(n) + 'p' + str(p).replace('.', ''), format='png')

comparison(25, 0.1)
