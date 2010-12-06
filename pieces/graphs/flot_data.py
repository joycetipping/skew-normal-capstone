# Python modules
import json
# My modules
from stats import *

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Comparison Graphs
#
def comparison_graph (n, p):
  # Builds data for one comparison graph (binomial, normal, and skew-normal)
  # and writes it to an appropriately-named json file

  (binomial, normal, sn) = frame( binomial_pmf(n, p, pairs=True),
                                  normal_pdf(n, p, pairs=True),
                                  sn_pdf(n, p, pairs=True) )
  def np (): return 'n' + str(n) + 'p' + str(p).replace('.', '')
  f = open('flot/json/comparison-' + np() + '.json', 'w')
  f.write('binomial.' + np() + ' = ' + json.dumps(binomial) + '\n')
  f.write('normal.' + np() + ' = ' + json.dumps(normal) + '\n')
  f.write('sn.' + np() + ' = ' + json.dumps(sn) + '\n')
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
  ps = [0.05, 0.1, 0.2, 0.3]

  # Write some necessary headers
  f = open('flot/json/comparison-headers.js', 'w')
  f.write('var binomial = {}; var normal = {}; var sn = {};\n')
  f.write('var ns = ' + json.dumps(map(str, ns)) + ';\n')
  f.write('var ps = ' + json.dumps(map(str, ps)) + ';\n')
  f.close()

  # Write our graphs
  map(lambda n: map(lambda p: comparison_graph(n, p), ps), ns)

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# MABS
#
def mabs_graph (n):
  # Builds data for one mabs graph and writes it to an appropriately-named file

  ps = r.seq(sn_p_range(n)[0] + 0.01, 0.5, 0.01)
  sn_points = map(lambda p: [p, mabs_sn(n, p)], ps)
  normal_points = map(lambda p: [p, mabs_normal(n, p)], ps)

  f = open('flot/json/mabs-n' + str(n) + '.json', 'w')
  f.write('sn.n' + str(n) + ' = ' + json.dumps(sn_points) + '\n')
  f.write('normal.n' + str(n) + ' = ' + json.dumps(normal_points) + '\n')
  f.close()
  return

def compile_mabs_data ():
  # Set our ns
  ns = [25, 50, 100, 200]

  # Write some necessary headers
  f = open('flot/json/mabs-headers.js', 'w')
  f.write('var normal = {}; var sn = {};\n')
  f.write('var ns = ' + json.dumps(map(str, ns)) + ';\n')
  f.close()

  # Write our graphs
  map(lambda n: mabs_graph(n), ns)


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Action, baby!
#
compile_comparison_data()
compile_mabs_data()
