# Defactoring 'Pace of Change'

## Introduction

Code, the symbolic representation of computer instructions driving
software, has long been a part of research methods in literary
scholarship. While it is a tired cliché to point to the work of Father
Busa and his compatriots at IBM (Jones 2016, Nyhan and Flinn 2016) as
foundational work in this respect, it was indeed a very early and
important application of computation as a means of analyzing literature.
In recent examples we find Broadwell and Tangherlini (2012) who
calculated geo-references for a large corpus of folklore stories, and
Piper (2015) who sought linguistic identifiers for 'conversional'
reading (that is, whether texts bear linguistic witness to life altering
experiences). But where is the code associated with these works? When we
are lucky we may retrieve the code enabling such feats of computational
literary analysis, like the code of Scott Enderle (2016) who crucially
contributed to a methodological discussion about perceived "fundamental
narrative arcs" from sentiment data in works of fiction or Mike
Kestemont et al.'s "Lemmatization for variation-rich languages using
deep learning" (2017), which improves automatic lemmatization for
historical literary texts. Unfortunately, much of the code used in the
long history of humanities computing or the recent abundance in digital
humanities has not been adequately recognized for its importance in the
production of knowledge.

In this article we argue that code cannot be simply regarded as the
interim-stage detritus of research; it is an explicit codification of
methodology and therefore must be treated as a fundamental part of
scholarly output alongside figures and narrative prose. The increased
application of code both as a means to create digital cultural artefacts
and as a mechanism for analysis within the humanities warrants the
necessity to elevate code out of the invisible research process and into
visible research outputs. The current system and practices of scholarly
publishing do not adequately accommodate the potential of code in
computational work---although it is a lynchpin of the discourse as both
the explication and execution of method, the code itself is not
presented as part of the discourse. We posit that its methodological and
rhetorical role in the evolving epistemology of literary studies (and
the humanities in general) warrants a more overt inclusion of
*code-as-method* in the scholarly discourse.

The current systems of scholarly communication are not tailored very
well to such inclusion. In the humanities there are no conventions for
theorizing, critiquing, interrogating, or peer reviewing code. Nor are
there agreed methods on how to read and understand it. Finally,
widespread conventions and infrastructure of scholarly publishing do not
support the dissemination and preservation of code as part of the
scholarly record. But given the increasing role of code and coding in
computational and data-intensive humanities research, this absence is
increasingly becoming an urgent crisis requiring immediate action.

This article is a first step investigating a solution to this problem.
We develop one possible method for reading and interrogating the
*bespoke code* of computational research. Modern computing is possible
because of an enormous infrastructure of code, layers upon layers of
accumulated operating systems, shared libraries, and software packages.
Rather than following every codified thread and unravelling the sweater,
we focus on the *bespoke code* associated with a single scholarly
publication, that is, the code written and executed in the pursuit of a
specific and unique research output, not general-purpose libraries or
software packages; the code that runs only once. As a result, we present
*defactoring*, a technique for analyzing and reading code used in
computational and data-intensive research. In the sections below, we
apply this technique to the code underlying a recent publication in the
field of literary studies by Ted Underwood and Jordan Sellers titled
"The *Longue Duree of Literary Prestige*" (2016). This analysis of their
work was made possible by the fact that they released preprints and
their code on both Zenodo (Underwood 2015) and GitHub (Underwood 2018).
Building upon their informally published work, we produced a
computational narrative in the form of a Jupyter Notebook documenting
our experience interrogating and reviewing the code. Following our
"close reading" of Underwood and Sellers's code, we discuss and reflect
upon their work and on defactoring as an approach to reviewing scholarly
code.

On the epistemological level this article subsequently questions how
useful it is that conventional scholarly literacy, means of critique,
and publications conventions keep in place and even enforce a strong
separation between the realm of the scholarly publication and the realm
of code, if both are expressions of the same. We contend that these
walls of separation can and should be broken down. To this end we need
to examine the effects and affordances of disrupting and breaking these
boundaries. This article in itself an attempt to create an instance of
such a disruption. We are looking to join the technical and the content
and ask how this adds to discourse. What would it look like if we joined
the quotidian of scholarly practice in code to the loftily theoretical
in the same discursive space? How does this new computationally
inflected mode of discourse afford a more robust scholarly dialogue?
What may be gained by opening up Jupyter Notebook and having multiple
discussions---the literary interpretative and, the computationally
methodological---simultaneously?

The specific intervention we have in mind also explains why this article
has the length it has and that some, maybe even the majority of readers,
will judge overly verbatim. Much of its long length is a result of
integrating into the article the very code we are talking about. With
our epistemological intervention in mind however, it will be clear to
the reader hopefully that we cannot do otherwise. If we were, for
instance, to relegate the code to an afterthought in an appendix, we
would rather re-inforce known boundaries rather than break them in the
interest of covering new ground.
