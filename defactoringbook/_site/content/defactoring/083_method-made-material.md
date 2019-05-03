### Method Made Material

Defactoring reveals an important methodological aspect, as the
'binormal\_select()' case shows, about the relationship between mundane
data management and urbane methodology, both are represented in code,
but only the method is mentioned in the MLQ article. Underwood and
Sellers chose not to use a more robust method for feature selection
because they foresaw that the improved accuracy would not measure up to
the effort required to explain it to an audience unfamiliar with more
advanced statistics. There is a clear tension between the techniques
being used and the explanation that must accompany them. From the
comments in the code we can infer that at that point in time these
research design issues were still relevant and the decision to go hither
or whither hinged not only on which method would technically be better.
Similarly in the MLQ publication and the Figshare contribution we find
many allusions to the tweaking of the models that Underwood and Sellers
used, but for which we do not find the full code anymore---for instance
where they refer to including gender as a feature (2016:338) and to
using multi period models (2016:329). Traces remain of these additional
analyses in the code but supplanted by later code and workflows these
statistical wanderings are not explicitly documented anymore.[^4]

In all this means that there is a lot of analysis and code-work that
remains unrepresented. Even in a radically open project such as Pace of
Change, there is still going to be code, data, and interpretive prose
that does not make the final cut (i.e the MLQ article). Moreover, much
analytic and code effort remains also invisible because it does not make
the making of documentary that the final codebase could be regarded as,
not leaving more than the odd trace, and left uninvestigated in a
defactoring like ours.

The invisibility of so many parts of the research narrative and effort
signals to us again the very need for the development of a scholarly
literacy that engages with the code level of research not as banal
drudgery, but as the actual, material manifestation of methodology. Only
by such deep and intimate code level understanding we can uncover and
merit the full analytical effort that scholars undertake in
computational explorations. We find that the insights that such close
reading of code yields are relevant to development of methodology,
techniques, and also training.

In what respect is *Defactoring 'Pace of Change'* a critical work? On a
small scale, as we mentioned earlier, the representation of Ted
Underwood and Jordan Sellers' code that we produce may be compared to a
critical scholarly edition of that code. Although a generally accepted
strong definition of what constitutes a critical scholarly edition does
not exist (cf. Gabler 1995:2--3), scholars tend to agree that a critical
edition represent a text undergone scholarly scrutiny to establish
scholarly curated text that is accompanied by an "apparatus criticus"
that accounts for the actions and decisions of the scholarly editor that
gave rise to the specific form in which the text is represented. In this
sense the defactored code represented in this article stays close to
this definition. At the same time the process of defactoring resulted
very much in a restructuring especially the modularity of the original
code, much more so than a scholarly editor would probably consider
passable in the case of a scholarly edition. However, in the sense that
every scholarly edition is also a theory about a text and an
interpretation (Cerquiglini 1999), the defactored code is a textual
critical and contextualized reading and interpretation of the code. We
did not however make a *critique* of the code, nor of the content
substance Underwood and Sellers present on the basis of this code in
their MLQ article. We did not make a critique of their method, we are
however validating what Underwood and Sellers argue in their MLQ article
by comparing it to their code.

The larger criticism that our defactoring experiment raises is that
there is a clear gap between the narrative of the code and that of the
MLQ article that Underwood and Sellers produced. This gap is rather
enlarged than narrowed by the current conventions of scholarly
publishing and communication. Much gets covered over between code and
MLQ article. This gap is of a methodological nature. One of our
reviewers argued that the code is not that interesting because scholars
are primarily interested in the "underlying methodology". If the
breaking down of the walls between code and literary analysis serves
anything it is that we think the gap suggests that there is such a thing
as an "underlying methodology", whereas we argue there is not. The code
*is* the underlying thing. There is not some metaphysical intellectual
method that does not have a material reality. If we read code we read
method. Sure enough, a representation of the method as method is not a
self-identical phenomenon, but method nonetheless. Probably the closest
we can come to a meticulous registration of methods. Just as a
publication is not self-identical with the text the authors had in mind,
nor with the actual research, but it comes closest to representing
these.

Thus, code is methodology made material. Defactoring tells us more about
the methods Underwood and Sellers apply than what is discussed in the
MLQ article. Reading the methodological details in the code proved
important to us to understand more exactly and more precisely what
Underwood and Sellers had done. Close reading of code helps us to better
understand what the successive transformations of the data actually add
up to in the end. It made us see how insight and meaning arise from a
series of tiny changes to data that in themselves are comprehensible and
valid. As such reading the code adds to understanding and validation of
the research by Sellers and Underwood. Defactoring traces that process
of data to insight. Reading the code tells us how this process is
materially instantiated. Method is not metaphysical, it is material and
exists in this world. Defactoring makes it visible.

This is a radical proposition that implies a disruptive intervention in
the conventions of scholarly publishing and communication where data and
computationally intensive works are concerned. Very rarely are the data
and code incorporated directly into the prosaic narrative, why would
they? Code is difficult to read, filled with banal boilerplate, and
doesn't contribute to an argument if it is expressed in a print-centric,
static medium like a PDF or book. But when the documentary medium itself
becomes a platform for the manipulation and execution of the code, of
the material expression of methodological procedures *in-line* with the
prosaic representations of the rhetorical procedure, then, we argue,
there is value in positioning the code as a first-order expression of
the methods deployed in data and computationally intensive research
publications.

*Defactoring 'Pace of Change'* is perhaps an unsuccessful attempt at
achieving this vision. We have, given the tools at our disposal, tried
to create a publication that represents what could be, and should be,
possible. However, the platforms and the practices do not exist or have
not come together to truly represent this idyllic confluence of prose,
data, and code. *Defactoring 'Pace of Change*' leverages Jupyter
Notebooks as a platform that affords the ability for both humans and
machines to read the same document, but the platforms of publishing and
reading such documents are non-existent or immature. Beyond platforms,
there are research and publication practices, a set of conventions, that
need to emerge where code is more seamlessly integrated into the
narrative. Our reconfiguration of Underwood and Seller's Python code
into a linear narrative and the intermixing of prosaic descriptions,
*defactoring* as a method, is an experiment in establishing new
practices and conventions for computational narratives.

Exploring the process of defactoring also taught us again that it is
impossible to take data out of its analytical context without veritably
rendering it meaningless. It is the context of code and argument that
co-creates interpretation and meaning from data. Cultural Analytical
insights are composed of three parts: the narrative, the data, and the
code. We contend that you cannot evaluate, review, or critique the
argument without attending to all three of these parts. Currently that
seems a rather intractable goal, if it were only for the few scholars
having the required skills, but also because publication platforms are
still nascent (e.g. Jupyter Notebook) and the scholarly publishing
infrastructure to support them is non-existent. However, we hope to have
put forth defactoring as a step towards reaching that ideal.

[^4]: This also does not address Andrew Goldstone's efforts to
    [reproduce *Pace of Change* in
    R](https://www.google.com/url?q=https://andrewgoldstone.com/blog/2016/01/04/standards/&sa=D&ust=1547653817150000&usg=AFQjCNGGwS__xOQYjaCIKccwEEdHiPfcmw),
    which implies a form of methodological equivalence of materially
    dissimilar code bases.
