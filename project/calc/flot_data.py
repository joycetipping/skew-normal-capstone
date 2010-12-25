# Written by Joyce Tipping <joyce@joycetipping.com>
# License: MIT <http://www.opensource.org/licenses/mit-license.php>

# Python modules
import json
# My modules
from stats import *

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Skew-normal Restriction Graphs
#
def sn_restriction_p_range_graph ():
  # Builds data for the "fixed n, viable p range" graph and writes it to an
  # appropriately named json file

  def range_pt (n):
    range = sn_restriction_p_range(n)
    return [n, range[0], range[1]]
  ns = r.seq(0, 50)
  p_range_bars = map(range_pt, ns)
  p_top_points = map(lambda range_pt: [range_pt[0], range_pt[1]], p_range_bars)
  p_bottom_points = map(lambda range_pt: [range_pt[0], range_pt[2]], p_range_bars)

  f = open('flot/data/restriction-p-range.js', 'w');
  f.write('var p_range_bars = ' + json.dumps(p_range_bars) + ';\n')
  f.write('var p_top_points = ' + json.dumps(p_top_points) + ';\n')
  f.write('var p_bottom_points = ' + json.dumps(p_bottom_points) + ';\n')
  f.close()

def sn_restriction_least_n_graph ():
  # Builds data for the "fixed p, least n" graph and writes it to an
  # appropriately named json file

  ps = r.seq(0.01, 0.5, 0.01)
  points = map(lambda p: [p, sn_restriction_least_n(p)], ps)

  f = open('flot/data/restriction-least-n.js', 'w')
  f.write('var least_n_points = ' + json.dumps(points) + ';\n')
  f.close()

def compile_sn_restriction_data ():
  sn_restriction_p_range_graph()
  sn_restriction_least_n_graph()

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Comparison Graphs
#
def comparison_graph (n, p):
  # Builds data for one comparison graph (binomial, normal, and skew-normal)
  # and writes it to an appropriately-named json file

  (binomial, normal, sn) = frame( binomial_pmf(n, p, pairs=True),
                                  normal_pdf(n, p, pairs=True),
                                  sn_pdf(n, p, pairs=True) )
  np = 'n' + str(n) + 'p' + str(p).replace('.', '')
  f = open('flot/data/comparison-' + np + '.js', 'w')
  f.write('binomial.' + np + ' = ' + json.dumps(binomial) + ';\n')
  f.write('normal.' + np + ' = ' + json.dumps(normal) + ';\n')
  f.write('sn.' + np + ' = ' + json.dumps(sn) + ';\n')
  f.close()

def frame (*args):
  # Chops off the tails where all three graphs are less than 0.001
  tmp = map(lambda list: filter(lambda point: point[1] > 0.001, list), args)
  left = right = 0
  for i, v in enumerate(tmp):
    if v[0][0] < left: left = v[0][0]
    if v[-1][0] > right: right = v[-1][0]
  return map(lambda list: filter(lambda point: left < point[0] < right, list), args)

def compile_comparison_data ():
  # Set ns and ps
  ns = [25, 50, 100]
  ps = [0.05, 0.1, 0.2]

  # Write some necessary headers
  f = open('flot/data/comparison-headers.js', 'w')
  f.write('var binomial = {}; var normal = {}; var sn = {};\n')
  f.write('var ns = ' + json.dumps(map(str, ns)) + ';\n')
  f.write('var ps = ' + json.dumps(map(str, ps)) + ';\n')
  f.close()

  # Write our graphs
  map(lambda n: map(lambda p: comparison_graph(n, p), ps), ns)

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# MABS
#
def mabs_fixed_n_graph (n):
  # Builds data for one mabs graph with fixed n and varying p, and writes it to
  # an appropriately-named file

  least_p = sn_restriction_p_range(n)[0]
  ps = r.seq(least_p + 0.01, 0.5, 0.01)
  sn_mabs_points = map(lambda p: [p, mabs_sn(n, p)], ps)
  normal_mabs_points = map(lambda p: [p, mabs_normal(n, p)], ps)

  f = open('flot/data/mabs-n' + str(n) + '.js', 'w')
  f.write('sn.n' + str(n) + ' = ' + json.dumps(sn_mabs_points) + ';\n')
  f.write('normal.n' + str(n) + ' = ' + json.dumps(normal_mabs_points) + ';\n')
  f.close()
  return

def mabs_fixed_p_graph (p):
  # Builds data for one mabs graph with fixed p and varying n, and write it to
  # an appropriately-named file

  least_n = sn_restriction_least_n(p)
  ns = r.seq(least_n, 200, 5)
  sn_mabs_points = map(lambda n: [n, mabs_sn(n, p)], ns)
  normal_mabs_points = map(lambda n: [n, mabs_normal(n, p)], ns)

  str_p = str(p).replace('.', '')
  f = open('flot/data/mabs-p' + str_p + '.js', 'w')
  f.write('sn.p' + str_p + ' = ' + json.dumps(sn_mabs_points) + ';\n')
  f.write('normal.p' + str_p + ' = ' + json.dumps(normal_mabs_points) + ';\n')
  f.close()
  return

def compile_mabs_data ():
  # Set our ns
  ns = [25, 100]
  ps = [0.05, 0.1]

  # Write some necessary headers
  f = open('flot/data/mabs-headers.js', 'w')
  f.write('var normal = {}; var sn = {};\n')
  f.write('var ns = ' + json.dumps(map(str, ns)) + ';\n')
  f.write('var ps = ' + json.dumps(map(lambda p: str(p).replace('.', ''), ps)) + ';\n')
  f.close()

  # Write our graphs
  map(lambda n: mabs_fixed_n_graph(n), ns)
  map(lambda p: mabs_fixed_p_graph(p), ps)


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Action, baby!
#
compile_comparison_data()
compile_mabs_data()
compile_sn_restriction_data()
