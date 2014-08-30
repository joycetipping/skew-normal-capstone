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

For more juicy details, read the paper or presentation ...

About This Repository
---------------------

All paths are relative to the repository.

Chances are, you're looking for my paper, presentation, or stats library. I've
symlinked these into the ``quick-links`` folder:

- *A pdf of my paper*: ``quick-links/paper.pdf``
- *A pdf of my presentation*: ``quick-links/presentation.pdf``
- *Stats library*: ``quick-links/stats.py`` (requires python and rpy)

If you're interested in looking at the tex source code for either my paper or
presentation, here's where you can find them:

- *The tex file for my paper*: ``project/paper/paper.tex``
- *The tex file for my presentation*: ``project/paper/presentation.tex``

Now for a more in-deph look. Here are the top-level directories and an
explanation of their contents.

``project/``
~~~~~~~~~~~~

The home of my project.

- ``bibliography.bib``: The BibTeX file shared between my paper and presentation.
- ``calc/``: Everything calculation related. My stats library, ``stats.py``, contains many useful functions for deriving a skew-normal approximation.
- ``flyer/``: The materials for my flyer, which I put together using Inkscape.
- ``images/``: Figures and graphs.
- ``paper/``: The pieces of my paper. I keep each section of my paper in its own tex file; these are stitched together last minute using bash and run through the latex compiler.
- ``pre-talk/``: An introductory talk to my capstone that I put together ages ago for my capstone seminar class.
- ``presentation/``: The pieces of my presentation. As with my paper, I keep each section in its own tex file and concatenate them just before compilation.
- ``proposal.pdf``: My capstone proposal.
- ``support/``: The supporting R packages and TeX style files for my project.

``articles/``
~~~~~~~~~~~~~

My collection of academic papers relating to the skew-normal. (Not all of them
are used in my capstone.)

``quick-links/``
~~~~~~~~~~~~~~~~

Symlinks to the resources I imagine people will be most interested in.


License
-------

All of my original work is licensed under the `MIT license
<http://www.opensource.org/licenses/mit-license.php>`_.
