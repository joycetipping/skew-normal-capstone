from stats import *

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Approximation Table
#

def build_approximation_table (ns, ps):
  f = open('approx-table/approx-table-data.txt', 'w');
  for p in ps: f.write(' & '.join(table_row(ns, p)) + ' \\\\\n');
  f.close()
    
def table_row (ns, p):
  return map(lambda n: sn_params_pretty(n, p), ns)

def sn_params_pretty (n, p):
  params = map(lambda x: str(round(x, 2)).rjust(6), sn_params(n, p));
  return '(' + params[0] + ', ' + params[1] + ', ' + params[2] + ')';

ns = [25, 50, 100, 200]
ps = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
build_approximation_table(ns, ps);
