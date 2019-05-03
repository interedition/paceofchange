## Pace of Change

The bespoke code we defactor is that which underlies an article that
Underwood and Sellers published in Modern Language Quarterly (2016): The
*Longue Durée* of Literary Prestige. This article was the culmination of
prior work in data preparation (Underwood and Sellers, 2014), coding
(Underwood and Sellers 2015a ad 2018) and preparatory analysis
(Underwood and Sellers, 2015). The main thrust of the MLQ article seems
to be one of method: "Scholars more commonly study reception by
contrasting positive and negative reviews. That approach makes sense if
you're interested in gradations of approval between well-known writers,
but it leaves out many works that were rarely reviewed at all in
selective venues. We believe that this blind spot matters: literary
historians cannot understand the boundary of literary distinction if
they look only at works on one side of the boundary" (Underwood and
Sellers 2016:324). To substantiate their claim Underwood and Sellers
begin their "inquiry with the hypothesis that a widely discussed "great
divide" between elite literary culture and the rest of the literary
field started to open in the late nineteenth century". To this end they
compare volumes of poetry that were reviewed in elite journals in the
period 1820-1917 with randomly sampled volumes of poetry from the
HathiTrust Digital Library from the same period. They filtered out
volumes from the HathiTrust resource that were written by authors that
were also present in the reviewed set, effectively ending up with
non-reviewed volumes. In all they compare 360 volumes of 'elite' poetry
and 360 non-reviewed volumes. For each volume the relative frequencies
of the 3200 most common words are tallied and they apply linear
regression to these frequency histograms. This linear regression model
enables them finally to predict whether a sample that was not part of
the regression data would have been reviewed or not. The accuracy of
their predictions is between 77.5 and 79.2 percent, which demonstrates
that there is some relationship between some poetry volume's vocabulary
and that volume being reviewed. But more importantly, what they can
glean from their results is that the traditional idea that literary
fashions are pretty stable over some decades and are then revolutionized
towards a new fashion deserves revisiting: the big 19th century divide
turns out not to be a revolutionary change but a stable and slowly
progressing trend since at least since 1840. Underwood and Sellers
conclude: none of our "models can explain reception perfectly, because
reception is shaped by all kinds of social factors, and accidents, that
are not legible in the text. But a significant chunk of poetic reception
can be explained by the text itself (the text supports predictions that
are right almost 80 percent of the time), and that aspect of poetic
reception remained mostly stable across a century". Sudden changes also
do not emerge if they try to predict other social categories like genre
or authorial gender. They finally conclude that the question why the
general slow trend they see exists is too big to answer from these
experiments alone, because of the many social factors that are involved.

Underwood and Sellers purposely divided their code into logical and
meaningful parts, modules, and functions stitched together into a data
processing and analysis script. We found to better understand the code
as readers (vs. authors) and to narrate its execution it was necessary
to restructure, defactor, the code into what is usually understood as a
poor software engineering practice, namely making a single long,
strongly integrated, procedural process. This makes the code a linear
narrative, which is easier for humans to read while the computer is for
the most part indifferent. There is a tension between these two mutually
exclusive representations of narratives with code divided and branched,
emerging from the process of development by software engineers, and with
prose as a linear narrative intended for a human reader. What we
observed is that the processes of deconstructing literature and code are
not symmetrical but mirrored. Where deconstructing literature usually
involves breaking a text apart into its various components, meanings,
and contexts, deconstructing software by defactoring means integrating
the code's disparate parts into a single, linear computational
narrative. "Good code," in other words, is already deconstructed (or
'refactored') into modules and composable parts. For all practical
purposes we effectively are turning "well engineered" code into
sub-optimal code full of 'hacks' and terrible 'code smells' by
de-modularizing it. However, we argue, this "bad" code is easier to read
and critique while still functioning as its authors intended.

Defactoring injects the logical sections of the code, parts that execute
steps in the workflow, with our own narrative reporting on our
understanding of the code and its functioning at that moment of the
execution. The Jupyter Notebook platform makes this kind of incremental
exploration of the code possible and allows us to present a fully
functioning and executable version of Underwood and Sellers's code that
we have annotated. Reading (and executing along the way) this notebook
therefore gives the reader a close resembling of the experience of how
we as deconstructionists 'closely read' the code.[^3]

[^3]: To support ourselves in the reading process we found it useful to
    keep track of the 'state' of the code as it was executing. We
    implemented this by listing all the 'active' variables and their
    values at each step of the process. The explanation of each step is
    therefore also amended with a listing of these variables.
