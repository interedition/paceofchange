---
redirect_from:
  - "/defactoring/060-how-to-read-the-defactoring-notebook"
title: 'How to Read the Defactoring Notebook'
prev_page:
  url: /defactoring/051_defactoring-code-from-python-files-to-the-notebook
  title: 'Defactoring Code From Python Files to the Notebook'
next_page:
  url: /defactoring/070_defactoring-pace-of-change
  title: 'Defactoring ‘Pace of Change’'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
### How to Read the Defactoring Notebook

One of the advantages to defactoring a function is that it affords us
the ability to insert critical commentary into the code constituting the
function itself. An unfortunate side-effect is that this makes keeping
track of one's place in the code a little more difficult. We have
restructured the code into an executable narrative (when read as a
Jupyter Notebook) for both human and machine readers.

Jupyter Notebooks are divided into a series of cells, *code cells* and
*text cells*. In our defactoring, the code cells contain Python code
mostly written by Underwood and Sellers, but with a few modifications by
us. Code cells can be executed when reading this document using the
Jupyter Platform (as opposed to static document). We have broken up the
code of Underwood and Sellers and inserted text cells, written by us,
which discuss and explain what is happening in the code cells and
underlying computational process. In most cases the expository text is
below the code cell. In the critical examination of the code we will be
using a fair bit of coding language jargon. Although a very deep grasp
of these coding concepts will not be needed, a certain level of coding
literacy (Vee 2013) will facilitate a speedier comprehension of our
narrative.
