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

- *A pdf of my final paper*: Run ``project/paper/build`` and then open ``skew-normal-approx.pdf`` (actually a symlink; the hard copy is in ``project/paper/output.pdf``)
- *The tex file for my final paper*: Run ``project/paper/build`` and then open ``project/paper/output.tex``
- *Stats library*: ``project/calculations/stats.py`` (requires python and rpy)

Now for a more in-deph look. Here are the top-level directories and an
explanation of their contents.

``project/``
~~~~~~~~~~~~

The home of my project.

- ``proposal.pdf``: My capstone proposal.
- ``paper/``: The pieces of my final paper. I keep each section of my paper in its own tex file; these are stitched together last minute using bash and run through the latex compiler.
- ``calculations/``: Everything calculation related. My stats library, ``stats.py``, contains many useful functions for deriving a skew-normal approximation. The rest of the files all
  generate specific graphs or data for my paper.
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
