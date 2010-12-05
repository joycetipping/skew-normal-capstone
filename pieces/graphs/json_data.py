# Python modules
import json
# My modules
from stats import *

def comparison (n, p):
  # Send comparison data to a json file
  binomial = binomial_pmf(n, p, pairs=True)
  normal = normal_pdf(n, p, pairs=True)
  sn = sn_pdf(n, p, pairs=True)

  def np (): return 'n' + str(n) + 'p' + str(p).replace('.', '')
  f = open('flot/json/comparison-' + np() + '.json', 'w')
  f.write('binomial.' + np() + ' = ' + json.dumps(binomial) + '\n')
  f.write('normal.' + np() + ' = ' + json.dumps(normal) + '\n')
  f.write('sn.' + np() + ' = ' + json.dumps(sn) + '\n')

def write_head (ns, ps):
  f = open('flot/json/head.js', 'w')
  f.write('var binomial = {}; var normal = {}; var sn = {};\n')
  f.write('var ns = ' + json.dumps(map(str, ns)) + ';\n')
  f.write('var ps = ' + json.dumps(map(str, ps)) + ';\n')

ns = [25]
ps = [0.05, 0.1, 0.2, 0.3]
write_head(ns, ps)
map(lambda n: map(lambda p: comparison(n, p), ps), ns)
