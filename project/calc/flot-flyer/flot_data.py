# Written by Joyce Tipping <joyce@joycetipping.com>
# License: MIT <http://www.opensource.org/licenses/mit-license.php>

import json
import sys
sys.path.append('..')
from stats import *


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Comparison Graphs
#
def write_comparison_graph (n, p):
  # Builds data for one comparison graph (binomial, normal, and skew-normal)
  # and writes it to an appropriately-named json file

  (binomial, normal, sn) = ( binomial_pmf(n, p, pairs=True),
                             normal_approx_pdf(n, p, pairs=True),
                             sn_approx_pdf(n, p, pairs=True) )
  np = 'n' + str(n) + 'p' + str(p).replace('.', '')
  f = open('data/comparison-' + np + '.js', 'w')
  f.write('binomial.' + np + ' = ' + json.dumps(binomial) + ';\n')
  f.write('normal.' + np + ' = ' + json.dumps(normal) + ';\n')
  f.write('sn.' + np + ' = ' + json.dumps(sn) + ';\n')
  f.close()

def compile_comparison_data ():
  # Set ns and ps
  ns = [25]
  ps = [0.05]

  # Write some necessary headers
  f = open('data/comparison-headers.js', 'w')
  f.write('var binomial = {}; var normal = {}; var sn = {};\n')
  f.write('var ns = ' + json.dumps(map(str, ns)) + ';\n')
  f.write('var ps = ' + json.dumps(map(str, ps)) + ';\n')
  f.close()

  # Write our graphs
  map(lambda n: map(lambda p: write_comparison_graph(n, p), ps), ns)

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Action, baby!
#
compile_comparison_data()
