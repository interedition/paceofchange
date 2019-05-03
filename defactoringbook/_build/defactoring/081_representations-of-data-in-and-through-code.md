---
redirect_from:
  - "/defactoring/081-representations-of-data-in-and-through-code"
title: 'Representations of Data in and Through Code'
prev_page:
  url: /defactoring/080_discussion-and-conclusion
  title: 'Discussion and Conclusion'
next_page:
  url: /defactoring/082_what-defactoring-as-a-method-helps-us-understand
  title: 'What Defactoring as a Method Helps Us Understand'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
### Representations of Data in and Through Code

From the perspective of data, the codebase of Pace of Change as a
narrative does not start at the beginning. The project begins with a
collection of data and metadata that came from somewhere, they are not
"raw" but had already been "cooked" to an extant from poetry volumes
into bags of words (Underwood 2014). There is a significant amount of
"data-work" done even before Pace of Change begins, but like the layers
of code in the form of shared libraries, operating systems, and general
purposes programming languages, this data-work is not bespoke to Pace of
Change. We can think of this data-work as happening at different layers
similar to Hinsen's layers of scientific software. Both the data and
code included in the Pace of Change GitHub repository are products
derived from or leveraging larger "libraries" (both in the sense of
software libraries like scikit-learn and digital libraries like
HathiTrust). Defactoring can use the same selection heuristic for code
as for data; only the bespoke data and code are the subject of our
investigation. The OCR'd texts in the HathiTrust digital library are
akin to the general-purpose programming languages or operating systems
in that they can be used for many purposes. While the content and
context of the data before the *Pace of Change* analysis are salient and
important, others have been attending to those stories (Chalmers and
Edwards 2017). The focus of defactoring is the intimate relationship
between the data, the code, and the execution environment within which
the representational work of computational research occurs.

The data in Pace of Change are not one thing, but rather a series of
interconnected things. The story of the data, as told through the code,
is a series of temporary representations created, manipulated, and
destroyed in the computational analysis process. The data in Pace of
Change starts as a tabular collection of metadata and a collection of
bags of words. The code filters and cleans metadata creating a Python
data structure with a subset of the data (mostly) relevant to the
analysis. The selected metadata then drives the processing of the data
files, the bags of words, to select a subset of those data, the top
3,200 word features, and to create vector representations for each
poetry volume and their associated status as reviewed or not reviewed.
Once transformed into normalized, numeric feature vectors and a vector
of binary labels. Much of the bespoke code-work of Pace of Change is in
the service of producing these two representations of the data (as is
much of the work in most data and computational research); bespoke code
for transforming bespoke data into standardized data conformant to
standardized software. What comes out the other side of the most
mathematically intensive transformation of Pace of Change is *more*
data, but these data are qualitatively and quantitatively different
because they are inoculated with new insights about the data they
represent. The predictions of 720 individual statistical models for each
poetry volume and the coefficients of the final statistical model are,
for Underwood and Sellers, the important representations---for it is
through the interpretation of these representations that they can find
new insights about literary history. This interpretation work is, of
course, done through code that produces a data visualization (because
charts surpass data tables in their comprehensibility and rhetorical
power). The data story of the *Pace of Change* code ends with a chart
and two new CSV files. One could, theoretically, review and critique
these data, but we would argue, focusing on just the data in absence of
the code by which they are made manifest would only be a small part of
the story.
