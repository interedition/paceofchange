## Defactoring in Practice

At a practical level, we have copied the code from Underwood and
Sellers' Pace of Change git repository and restructured their code into
a Jupyter Notebook. Transforming Underwood and Seller's code from a set
of Python scripts into the notebook involved a series of transformations
to their code. The provenance of this effort has been preserved because
we did all of our work in a fork of their version repository, visible
via the git history command.

Underwood and Sellers's wrote their code to make it easy to replicate
their results by running a single command. One of our first tasks was to
trace their code following the path of execution from the initial
command to the output data files. By reading the code that spanned
multiple python scripts, we could obtain a rough idea of how Underwood
and Sellers's analysis of poetry volumes was performed in practice. The
first step of reading their code involved translating their python
scripts into a Jupyter Notebook. Plain text files leave much to be
desired with trying to critically interrogate code, the Jupyter Notebook
format and platform enables a much richer reading experience.
Translating Underwood and Sellers's scripts involved copying snippets of
code from multiple Python (.py) files into a single executable notebook.
For code that was not already authored in a notebook, this requires
significant effort curating and restructuring the code to fit the linear
structure of the notebook while preserving the functionality of
Underwood and Sellers's scripts.

Not all of the code in the git repository was copied into the notebook
for two main reasons. First, not all of the code included in the files
was actually needed to replicate the analysis. The repository includes
additional code, one could call it "cruft", from Underwood and Seller's
exploratory analysis or earlier iterations of their analytical process.
For example, the file SonicScrewdiver.py is never called upon although,
based upon the name, we might hypothesize it is an important catch-all
module for a variety of different functions. Other sections of the code
are commented out and thus never executed (such as binormal\_select
discussed below). As part of the defactoring process, we opted to not
include unused functions or code blocks. Another reason that the code of
Sellers and Underwood was not copied verbatim is because we do not
represent all possible executions paths of the code. Their code included
execution paths that trained multiple models of the data broken into
twenty-year periods, but their final analysis trained a model on the
entire dataset. In this notebook we follow the default option, "full",
which models the entire dataset.

Underwood and Seller's code is stored within four Python files,
replicate.py, parallel\_crossvalidate.py, metafilter.py, and
modelingprocess.py. Through the process of defactoring we have copied
some, but not all, code from the Python text files to a Jupyter
Notebook. This process has transformed the structure and flow of the
code, but not the functionality. Like *refactoring*, the inputs and
outputs and overall functionality remain the same, but our process has
restructured the code to be much more readable as a narrative with our
own expository text intermixed with executable blocks of code.

![Fig.2: Defactoring code from python files to the
notebook](/images/fig_002_defactoring.png)

*Fig.2: Defactoring code from python files to the
notebook*
