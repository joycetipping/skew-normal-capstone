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
  ns = [25, 500]
  ps = [0.05, 0.5]

  # Write some necessary headers
  f = open('data/comparison-headers.js', 'w')
  f.write('var binomial = {}; var normal = {}; var sn = {};\n')
  f.write('var ns = ' + json.dumps(map(str, ns)) + ';\n')
  f.write('var ps = ' + json.dumps(map(str, ps)) + ';\n')
  f.close()

  # Write our graphs
  map(lambda n: map(lambda p: write_comparison_graph(n, p), ps), ns)

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Property Graphs:
#
def write_property_graph (mu, sigma, skew):
  str_skew = str(skew) if skew > 0 else 'neg' + str(-skew)
  sn_graph = frame( sn_pdf(mu, sigma, skew, pairs=True) )
  #sn_graph = sn_pdf(mu, sigma, skew, pairs=True)

  f = open('data/properties-skew' + str_skew + '.js', 'w')
  f.write('std_sn.skew' + str_skew + ' = ' + json.dumps(sn_graph) + ';\n')

def compile_property_graphs_data ():
  skews = [-1000, -100, -10, -5, -3, -2, -1, 1, 2, 3, 5, 10, 100, 1000]

  # Write some necessary headers
  f = open('data/properties-headers.js', 'w')
  f.write('var std_sn = {};\n')
  f.write('var skews = ' + json.dumps(map(str, skews)) + ';\n')
  f.close()

  # Write our graphs
  map(lambda skew: write_property_graph(0, 1, skew), skews)

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Common helpers
#
def frame (*args):
  # Chops off the tails where all three graphs are less than 0.00001
  tmp = map(lambda list: filter(lambda point: point[1] > 0.001, list), args)
  left = right = 0
  for i, v in enumerate(tmp):
    if v[0][0] < left: left = v[0][0]
    if v[-1][0] > right: right = v[-1][0]
  return map(lambda list: filter(lambda point: left < point[0] < right, list), args)

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Action, baby!
#
compile_comparison_data()
compile_property_graphs_data()
