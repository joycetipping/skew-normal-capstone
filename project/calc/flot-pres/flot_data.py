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

  binomial = binomial_pmf(n, p, pairs=True)
  normal   = normal_approx_pdf(n, p, pairs=True)
  sn       = sn_approx_pdf(n, p, pairs=True)

  np = 'n' + str(n) + 'p' + str(p).replace('.', '')
  f = open('data/comparison-' + np + '.js', 'w')
  f.write('binomial.' + np + ' = ' + json.dumps(binomial) + ';\n')
  f.write('normal.' + np + ' = ' + json.dumps(normal) + ';\n')
  f.write('sn.' + np + ' = ' + json.dumps(sn) + ';\n')
  f.close()

def compile_comparison_data ():
  # Set ns and ps
  ns = [25, 500]
  ps = [0.05, 0.5, 0.95]

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
def write_std_sn_graph (skew):
  # Builds data for a standard skew-normal graph and writes it to an
  # appropriately-named json file

  str_skew = str(skew) if skew > 0 else 'neg' + str(-skew)
  std_sn_pdf = sn_pdf(0, 1, skew, pairs=True)

  f = open('data/properties-sn-skew' + str_skew + '.js', 'w')
  f.write('std_sn.skew' + str_skew + ' = ' + json.dumps(std_sn_pdf) + ';\n')

def write_half_normal_graphs ():
  # Builds data for the positive and negative half normal graphs and writes
  # them to an appropriately-named json file
  std_normal_pdf = normal_pdf(0,1, pairs=True)

  # To get the positive (negative) half normal, we select only points with positive (negative) x values and double the y values
  #positive_half_normal = [[0, 0]] + map(lambda point: [point[0], 2*point[1]], filter(lambda point: point[0] > 0, std_normal_pdf))
  #negative_half_normal = map(lambda point: [point[0], 2*point[1]], filter(lambda point: point[0] < 0, std_normal_pdf)) + [[0, 0]]
  positive_half_normal = map(lambda point: [point[0], 2*point[1]] if point[0] > 0 else [point[0], 0], std_normal_pdf)
  negative_half_normal = map(lambda point: [point[0], 2*point[1]] if point[0] < 0 else [point[0], 0], std_normal_pdf)

  f = open('data/properties-half-normal.js', 'w')
  f.write('var positive_half_normal = ' + json.dumps(positive_half_normal) + ';\n')
  f.write('var negative_half_normal = ' + json.dumps(negative_half_normal) + ';\n')
  f.close()

def compile_property_graphs_data ():
  # Set skews
  skews = [-1000, -10, -5, -2, 2, 5, 10, 1000]

  # Write some necessary headers
  f = open('data/properties-headers.js', 'w')
  f.write('var std_sn = {};\n')
  f.write('var skews = ' + json.dumps(map(str, skews)) + ';\n')
  f.close()

  # Write our graphs
  map(lambda skew: write_std_sn_graph(skew), skews)
  write_half_normal_graphs()

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Action, baby!
#
compile_comparison_data()
compile_property_graphs_data()
