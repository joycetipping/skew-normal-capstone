# Written by Joyce Tipping <joyce@joycetipping.com>
# License: MIT <http://www.opensource.org/licenses/mit-license.php>

import json
import sys
sys.path.append('..')
from stats import *

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Comparison Graphs
#
def comparison_graph (n, p):
  # Builds data for one comparison graph (binomial, normal, and skew-normal)
  # and writes it to an appropriately-named json file

  [binomial, normal, sn] = frame( binomial_pmf(n, p, pairs=True),
                                  normal_approx_pdf(n, p, pairs=True),
                                  sn_approx_pdf(n, p, pairs=True) )
  np = 'n' + str(n) + 'p' + str(p).replace('.', '')
  f = open('check.js', 'w')
  f.write('binomial = ' + json.dumps(binomial) + ';\n')
  f.write('normal = ' + json.dumps(normal) + ';\n')
  f.write('sn = ' + json.dumps(sn) + ';\n')
  f.close()

def frame (*args):
  # Chops off the tails where all three graphs are less than 0.001
  tmp = map(lambda list: filter(lambda point: point[1] > 0.001, list), args)
  left = right = 0
  for i, v in enumerate(tmp):
    if v[0][0] < left: left = v[0][0]
    if v[-1][0] > right: right = v[-1][0]
  return map(lambda list: filter(lambda point: left < point[0] < right, list), args)

comparison_graph(25, 0.05)
