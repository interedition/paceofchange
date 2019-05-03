---
redirect_from:
  - "/defactoring/051-defactoring-code-from-python-files-to-the-notebook"
title: 'Defactoring Code From Python Files to the Notebook'
prev_page:
  url: /defactoring/050_defactoring-in-practice
  title: 'Defactoring in Practice'
next_page:
  url: /defactoring/060_how-to-read-the-defactoring-notebook
  title: 'How to Read the Defactoring Notebook'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
### Defactoring code from python files to the notebook

In order for the code to execute seamlessly within the notebook, we had
to make minor changes and tweaks to the code. These changes fall into 4
categories:

-   *defactoring functions* - This is the most significant of the
    changes. When we defactor a function we take the function's code and
    move it to the global namespace. This has the effect of eliminating
    the function and just making it part of the main execution path.

-   *defactoring definitions* - Not all functions can be fully
    defactored. Functions that are called more than once or those that
    are short have been kept as re-usable functions. Defactoring
    Definition cells define the functions above the code cells that use
    them (preventing errors).

-   *defactoring namespace* - Because we have defactored some of the
    functions and their function calls some of the variables in the
    namespace need to be mapped to each other. This happens, for
    instance, when the return value of a defactored function needs to be
    stored in a differently named variable so the rest of the code can
    access it (resolving the fact we have moved a function's internal
    variables into a global namespace).

-   *defactoring inspections* - When we want to inspect the state of the
    process, we insert an inspection cell that prints the values of the
    variables of interest. These allow us the ability to inspect the
    state of the process as it is running; essentially debugging
    intermediate states.

-   *defactoring import* - Because the code is reliant upon external and
    third-party functions, we need to import that code into the global
    namespace. This cell contains all of those imports.
