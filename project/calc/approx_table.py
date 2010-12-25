# Written by Joyce Tipping <joyce@joycetipping.com>
# License: MIT <http://www.opensource.org/licenses/mit-license.php>

from stats import *

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Approximation Table
#

def build_approximation_table (ns, ps):
  f = open('approx-table/approx-table-data.txt', 'w')
  f.write('{ r r | ' + 'r@{}r@{,\\;}r@{,\\;}r@{}l '*len(ns) + '}\n')
  f.write('\\hline \\hline\n')
  f.write('& & ' + '\\multicolumn{5}{c}{} & '*2 + '\\multicolumn{5}{c}{$n$}' + ' & \\multicolumn{5}{c}{}'*2 + '\\\\\n')
  f.write('\\multirow{' + str(len(ps) + 1) + '}{*}{$p$} & & ' + ' & '.join(map(lambda n: '\\multicolumn{5}{c}{' + str(n) + '}', ns)) + ' \\\\\n\\hline\n');
  for p in ps: f.write('& ' + '{0:.2f}'.format(p) + ' & ' + ' & '.join(table_row(ns, p)) + ' \\\\\n');
  f.close()
    
def table_row (ns, p):
  return map(lambda n: sn_params_pretty(n, p), ns)

def sn_params_pretty (n, p):
  params = map(lambda x: '{0:.2f}'.format(x), sn_params(n, p));
  return '( & ' + params[0] + ' & ' + params[1] + ' & ' + params[2] + ' & )';

ns = [25, 50, 100, 250, 500]
ps = r.seq(0.05, 0.95, 0.05)
build_approximation_table(ns, ps);
