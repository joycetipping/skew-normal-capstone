Skew Normal Capstone
====================

This is my undergraduate capstone on the skew-normal approximation of the
binomial distribution. The paper I am explicating is "A Note on Improved
Approximation of the Binomial Distribution by the Skew-Normal Distribution," by
Chiang, et al.

Intro to the Skew Normal Approximation
--------------------------------------

The normal distribution is a good approximation of the binomial when either n
is very large or p is close to 0.5. However, when neither of those conditions
are met, the binomial is skewed. The skew-normal distribution introduces a
third parameter, lambda, that attempts to capture this asymmetry.

For more juicy details, read the paper ...

About This Repository
---------------------

Before I dive into explaining this repository, here's a list of the things
you're most likely looking for. All paths are relative to the repository.

- *A pdf of my final paper*: ``skew-normal-approx.pdf`` (actually a symlink)
- *The tex file for my final paper*: Run ``pieces/paper/build`` (important! see below) and then look for ``pieces/paper/output.tex``
- *Stats library*: ``pieces/calculations/stats.py`` (requires you have python and rpy installed)

``project/``
~~~~~~~~~~~

The home of my project.

- ``proposal.pdf``: My capstone proposal.
- ``paper/``: The pieces of my final paper. I keep each section of my paper in its own tex file. These files (``intro.tex``, ``properties.tex``, ``method-of-moments.tex``, ``mabs.tex``,
  ``conclusion.tex``) are stitched together last minute into ``output.tex`` and run through the latex compiler.
- ``calculations/``: Everything calculation related. ``stats.py`` is my stats library for the skew-normal approximation. ``flot_data.py`` and ``approx_table.py`` generate the data for
  the float graphs and approximation table and store them in ``flot/json/`` and ``approx-table/``, respecitvely. The html files that generate the flot graphs are also in ``flot/``.
- ``images/``: Figures and graphs

``papers/``
~~~~~~~~~~~

My collection of academic papers relating to the skew-normal. (Not all of them
are used in my capstone.)

``beamer/``
~~~~~~~~~~~

My beamer presentations. Right now, it contains only an introduction to my
capstone project. Eventually, it will also contain my final presentation.


License
-------

All of my original work is licensed under the `MIT license
<http://www.opensource.org/licenses/mit-license.php>`_.
