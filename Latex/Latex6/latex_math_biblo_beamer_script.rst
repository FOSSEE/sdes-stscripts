.. Objectives
.. ----------

.. At the end of this tutorial, you will be able to

.. 1. Write simple mathematical formulae in LaTeX.
.. #. Typeset simple mathematical formulae in LaTeX.
.. #. Write bibliography for a LaTeX document.
.. #. Make presentations in LaTeX, using beamer.

.. Prerequisites
.. -------------

.. 1. Basics of LaTeX and its document structure.
.. #. Typesetting LaTeX text.

.. 1. latex_intro 
.. Author              : Harish Badrinath < harish [at] fossee [dot] in > 
   Internal Reviewer   : 
   External Reviewer   :
   Langauge Reviewer   : 
   Checklist OK?       : <put date stamp here, if OK> 

Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and welcome to the tutorial on basics of typesetting mathematical 
formulae, bibliography and presentations, using LaTeX.

.. L2

{{{ Show the objectives slide }}}

.. R2

.. At the end of this tutorial, you will be able to

.. 1. Write simple mathematical formulae in LaTeX.
.. #. Typeset simple mathematical formulae in LaTeX.
.. #. Write bibliography for a LaTeX document.
.. #. Make presentations in LaTeX, using beamer.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial, it is recommended to complete the tutorials 
titled "Basics of LaTeX and its document structure" and "Typesetting LaTeX 
text".

.. L4

{{{ Show the "LaTeX & Mathematics : An Introduction" slide }}}

.. R4

In general, it is advisable to use the AMS-LaTeX bundle to typeset mathematics 
in LaTeX. AMS-LaTeX is a collection of packages and classes for mathematical
typesetting.

We can load amsmath by issuing the \usepackage{amsmath} in the preamble.It must 
be noted that amsmath is included in the base distribution of LaTex, in atleast 
the most recent versions.

Math formulae can be embedded in two ways,
  “inline” or “text style ” method,  which is  done by enclosing the 
  required command and text within two dollar signs or between an backslash
  opening bracket and backslash closing bracket.

  By enclosing them in a dedicated environment respectively/displayed style.

The most common LaTeX environment used to typeset mathematical formulae is 
from equation family.


.. L5

{{{ Show the "Matrices" slide }}}

.. R5

An environment like bmatrix for example, is used to render a matrix. The syntax
for specifying a matrix is similar to that used in the tabular environment. The
& symbol is used for demarcating columns and \\ is used to demarcate rows.

There are 5 other matrix environments and each have different/no type of 
delimiters. A table showing the data is being shown on the screen. The matrix
and its allied environments are defined by the amsmath package.

.. L6

{{{ Show the "Matrices ..." slide }}}

.. R6

The screen shows the an example, that renders different types of matrices using
LaTeX.

It also shows the two ways in which mathmatical formulae can be embedded into
LaTeX documents. 

Please pause the tutorial and go through the example shown on the screen. 

.. L7

{{{continue from paused state}}}
{{{ Show the "Superscripts & Subscripts" slide }}}

.. R7

To typeset superscripts in LaTeX, the carat character is used. The carat 
operator just acts on the next character.
To typeset subscripts in LaTeX, the underscore character is used. The carat 
operator just acts on the next character.
Multiple characters and ambiguity is resolved by grouping them using opening
and closing curly brackets.

.. L8

{{{ Show the "Summation & integration" slide }}}

.. R8

To typeset the summation symbol, use the sum command. Similarly, the integral 
symbol is obtained using the int command. The upper and lower limits, for both
the sum and int command are specified using the carat and underscore characters
, respectively.

.. L9

{{{ Show the "displayed math" slide }}}

.. R9

We now move onto using the equation environment to render mathematical formulae,
which are numbered. Another environment called equation star environment renders
unnumbered equations.

Backslash and opening square bracket and its counterpart the backslash
closing square bracket is a short hand for equation star environment.
There is no similar shorthand for equation environment (i.e, the numbered
equation environment).

.. L10

{{{ Show the "Groups of equations" slide }}}

.. R10

The equation and its allied  environments allows only one equation at a time.
We cannot use the newline command in the equation and its allied environment.
To come around this requirement, we can use eqnarray environment to group 
multiple equations. 

The eqnarray environment provides additional convenience like auto alignment
using the ampersand command, auto numbering of equations, etc.

Each distinct equation in the group needs to be separated by a newline command.
The parts of the equation that need to be aligned are indicated using an 
ampersand symbol.

.. L11

{{{ Show the "Fractions & Surds" slide }}}

.. R11

To typeset fractions use the frac command. To typeset surds, we use the sqrt
command with the optional paramter of [n].

Please note that there is a special command dfrac, that can be used to render
fractions as if its placed in display mode and is meant to be used even in
inline mode.

.. L12

{{{ Show the "Greek characters & Spacing in math environments" slide }}}

.. R12

Inserting Greek letters into LaTeX is simple. we use commands named alpha, beta,
gamma, etc for lower case Greek letters. Similarly, we use Alpha, with an upper
case A, Beta, with an upper case B, Gamma, with an upper case G, etc for upper 
case greek letters.

Also, math environments do not give extra spaces using the space or tab 
characters. The following commands show in the table on the screen are available
to specify the spacing required.

.. L13

{{{ Show the "Bibliography" slide }}}

.. R13

Writing bibliographies in LaTeX using the thebibliography environment is pretty
easy. You simply have to list down all the bibliography items within the 
bibliography environment.

Each entry of the bibliography begins with the command bibitem. It takes an 
optional parameter called label and a name for the entry.The label option
replaces the numbers from the auto enumeration with the labels given.

The to cite the bibliography item within the document, we use the cite command,
containing name as a parameter. 

We start the bibliography environment with a numerical parameter. This defines
how much space is to be reserved for all the labels.
If for example, we have less than 10 items in the Bibliography we would begin
the bibliography environment with an parameter, whose value is 9.

.. L14

{{{continue from paused state}}}
{{{ Show the "Beamer" slide }}}

.. R14

It is highly recommended to use beamer to create presentations, especially when
you are using LaTeX typesetting your report. This is mainly because, it would be 
really easy to reuse the LaTeX that you have used for the report/document for
the presentation as well.
 
We begin a beamer document with the documentclass being set to beamer.

A beamer document is very similar to other LaTeX documents, with the exception
that content is divided into slides.

.. L15

{{{ Show the "Beamer ..." slide }}}

.. R15

The usetheme command is used to specify the theme to be used for the current
presentation. The usecolor theme command is used to specify the color theme to
be used in the current presentation. 

The contents of a slide are enclosed within the begin frame and end frame 
environment. The begin command with frame as the parameter can optionally be 
passed the Title and Subtitle of the slide it contains.

We must also note that the title page of the presentation can be set like any 
other LaTeX document. 

If we have to use fragile environemts like verbatim or lstlisting  inside a 
slide, then we have to pass an additional parameter to begin frame, fragile.

Overlays and simple animation can be achieved using the pause command.

We recommend you look at the beamer user guide, to get more acquainted with 
this marvelous utility.

.. L16

{{{ Show the "Beamer: An Example presentation" slide }}}

.. R16

This screen shows a very basic LaTeX presentation done using beamer. We use the
warsaw theme. There are three slides in the actual document definition, but we
see more than 3 slides in the output document. This is because of the overlay 
we created in the last slide. Please pause the tutorial and go through the
example shown on the screen.

.. L17

{{{continue from paused state}}}
{{{ Show the "Summary" slide }}}

.. R17

This brings us to the end of this tutorial. In this tutorial, we have,

.. 1. Written simple mathematical formulae in LaTeX.
.. #. Typeset simple mathematical formulae in LaTeX.
.. #. Written bibliography for a LaTeX document.
.. #. Made a sample presentations in LaTeX, using beamer.

.. L18

{{{ Show the "Self assessment questions" slide }}}

.. R18

Here are some self assessment questions for you to solve

 1. What is the function of useoutertheme command used in the beamer 
presentation example shown before ?? what happens when you comment out or
remove the line.

 2. Are commands like \alpha, \beta ,etc commands provided by amsmath package ?

.. L19

{{{ Show the "Self assessment questions: Solutions" slide }}}

.. R19

And the answers,

1. The outertheme command in beamer is used to customize the amount of 
header/footer information shown in each slide. In the example shown below the
useoutertheme command with infolines argument automatically adds more 
information to the footer like page number, author and institute,etc.

2. No, commands like alpha, beta, etc are not commands provided by the amsmath
package.

.. L20

{{{ Show the "Thank you" slide }}}

.. R20

Hope you have enjoyed this tutorial and found it useful.
Thank you!
