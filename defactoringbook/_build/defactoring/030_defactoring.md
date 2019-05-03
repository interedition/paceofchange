---
redirect_from:
  - "/defactoring/030-defactoring"
title: 'Defactoring'
prev_page:
  url: /defactoring/021_hinsen-s-layers-of-scientific-software
  title: 'Hinsen&#39;s Layers of Scientific Software'
next_page:
  url: /defactoring/040_pace-of-change
  title: 'Pace of Change'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Defactoring

We introduce an experimental technique called *defactoring* to address
the challenges of critically reading and evaluating code. We expand on
ideas of Braithwaite (2013) who considered defactoring as the process of
de-modularizing software to reduce its flexibility in the interest of
improving design choices. This is counter intuitive to software
engineering where best practices prefer increased generalization,
flexibility, and modularization. Refactoring and software engineering
best practices emphasize writing code that can be managed according to
the organizational labor practices of software production and
object-oriented design, breaking blocks of code into independent units
that can be written and re-used by teams of developers (cf. for instance
Metz and Owen 2016). While these best practices make sense for code
intended for the first three layers of software the fourth layer,
bespoke code, might better have a different style with less emphasis on
abstraction and modularity because such code becomes harder to read as a
narrative.

Here we are interested in elucidating what a process of defactoring code
looks like for the purposes of reviewing code, which implies reading
code. In our expanded notion of the concept, defactoring can be
understood as a close reading of source code--and if necessary, a
reorganization of that code--to create a narrative around the function
of the code. This technique serves multiple purposes: critically
engaging the workings and meanings of code; peer reviewing code;
understanding the epistemological and methodological implications of the
inscribed computational process; and a mechanism for disseminating and
teaching computational methods. We use defactoring to produce what might
prospectively be called the first critical edition of source code in the
digital humanities by unpacking Ted Underwood and Jordan Sellers's code
associated with their article "The *Longue Duree* of Literary Prestige"
(Underwood and Sellers 2016).[^2]

The codebase that Underwood and Sellers produced and that underpins
their argument in "The *Longue Duree* of Literary Prestige" is a typical
example of multi layered code. The code written by Underwood and Sellers
is bespoke code, or fourth layer code in Hinsen's model of scientific
software layers. When dealing with a scholarly publication such as "The
*Longue Duree* of Literary Prestige", our reading should concentrate on
layer four, the bespoke code. The code from the lower layers, while
extremely important, should be evaluated in other processes. As Hinsen
points out, layer four software is the least likely to be shared or
preserved because it is bespoke code intended only for a specific use
case, this means it most likely has not been seen by anyone except the
original authors. Lower layer software, such as scikit-learn, has been
used, abused, reviewed, and debugged by countless people. There is much
less urgency therefore to focus the kind of intense critical attention
that comes with scholarly scrutiny on this software because it already
has undergone so much review and has been battle tested in actual use.

There is no established definition of 'defactoring' or its practice.
Defactoring provides a method and conceptual framework for close reading
the code in data intensive and computational digital humanities research
for the purposes of deep understanding. How this process of
understanding is performed is not prescribed and could take many forms.
One potential approach would be to simply run the code as-is in a
similar workflow but perhaps with different data, however this would not
generate much insights as the code would be treated as a black box.
Another approach might be reverse engineering, which would try to
approximate the code's function by comparing inputs and outputs (Seaver
2014). For closed source code, this might be the only option. Writing
automated tests that gauge the different responses to input might yet be
another approach (Berry 2014). Here however we are interested in a deep
and intimate understanding of code (cf. Frabetti 2012) to understand how
it is adding or changing methodology and how it could be critiqued.

Defactoring is a process or possible a tool for 'opening the black box'
of computational and data intensive scholarship. While it shares some
similarity to the process of refactoring--in that we are "restructuring
existing computing code without changing its external
behavior"--refactoring restructures code into separate functions or
modules to make it more reusable and re-combinable. Defactoring does
just the opposite. We have taken code that was broken up over several
functions and files and combined it into a single, linear narrative.

Our development of defactoring as a method of code analysis is deeply
imbricated with a technical platform (just as all computational research
is). But rather than pushing the code into a distant repository separate
from the prosaic narrative, we compose a computational narrative (Perez
and Granger 2015)---echoing Knuth's literate programming
(1984)---whereby Underwood and Sellers's data and code are bundled with
our expository descriptions and critical annotations. This method is
intimately intertwined with the Jupyter Notebook platform which allows
for the composition of scholarly and scientific inscriptions that are
simultaneously human and machine readable. The particular affordances of
the Notebook allow us to weave code, data, and prose together into a
single narrative that is simultaneously readable and executable. Given
our goals to develop a method for critically engaging computational
scholarship, it is imperative we foreground Underwood and Sellers's
bespoke code and the Jupyter Notebooks enables us to do so.

[^2]: Interestingly, the article and the accompanying code by Underwood
    and Sellers have been subject to scrutiny before. The publication
    and code served as a use case for a workflow modeling approach aimed
    at replication studies (Senseney 2016). We are not primarily
    interested in replication per se, but the example serves to show how
    valuable the publication of open source/open access code and data
    are for replication and peer review.
