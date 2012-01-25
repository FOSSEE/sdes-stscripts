.. Objectives
.. ----------

.. By the end of this tutorial, you will be able to

.. 1. Write and typeset simple mathematical formulae in LaTeX.
.. #. Write bibliography for a LaTeX document.
.. #. Make presentations in LaTeX, using beamer.

.. Prerequisites
.. -------------

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

.. By the end of this tutorial, you will be able to

.. 1. Write and typeset simple mathematical formulae in LaTeX.
.. #. Write bibliography for a LaTeX document.
.. #. Make presentations in LaTeX, using beamer.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you complete the tutorials titled 
"Introduction to LaTeX","Basics of LaTeX and its document structure","Basics of
LaTeX and its documents structure" and "Typesetting LaTeX text".

.. L4

.. R4

Math formulae can be embedded in two ways. One is inline, and the other way is
 to enclose them in a dedicated environment as and when required.
The first method is also called text style and second method is also called 
displayed style.

In-lining is done by enclosing the required command and text withing two dollar
signs or between an backslash opening bracket and backslash closing bracket.

The most common LaTeX environment used to typeset mathematical formulae is 
from equation family. Its use is given in more detail, further in the tutorial.

It must be noted that amsmath is included in the base distribution of LaTex, in
most recent versions.

.. L5


.. R5

An environment like bmatrix for example, is used to render a matrix. The syntax
for specifying a matrix is similar to that used in the tabular environment. The
& symbol is used for demarcating columns and \\ is used to demarcate rows.

Various types of matrix have different/no type of border decorations. A table 

showing the data is being shown on the screen. The matrix and its allied 
environments are defined by the amsmath package.

.. L6


.. R6

The screen shows the an example, that renders different types of matrices using
LaTeX.
It also shows the two ways in which mathmatical formulae can be embedded into
LaTeX documents. The second method of embedding mathamtical formula will be 
explained in detail, later in the tutorial. Please pause the tutorial and go through the example shown on the screen. 

.. L7

{{{continue from paused state}}}

.. R7

Charet is used to render text in superscript, while underscore is used to
render text in subscript.
Multiple characters and ambiguity is resolved by grouping them using opening
and closing curly brackets.

.. L8


.. R8

sum and int commands are used to show summation and integration in the rendered
document respectively. We can specify the upper and lower limits for these
commands using charet and underscore respectively.

.. L9


.. R9

As mention earlier, we can display mathematical formulas in either one of two
ways. The first was mentioned earlier, now we use the equation environment
to render mathematical formulae, which are numbered. The equation star
environment is used to render unnumbered equations.

Backslash and opening square bracket and its counterpart the backslash
closing square bracket is a short hand for \begin equation star environment.
There is no similar shorthand for equation environment (i.e, the numbered
equation environment).

.. L10


.. R10

The equation and its allied  environments allows only one equation at a time.
To come around this requirement, we can use eqnarray environment to group 
multiple equations. 

The eqnarray environment provides additional convenience like auto alignment
using the ampersand command, auto numbering of equations, etc.

Each distinct equation in the group needs to be separated by a newline command.

.. L11


.. R11

We typeset fractions using the frac command. We can also render surds using 
sqrt command.
Please note that there is a special command dfrac, that can be used to render
fractions as if its placed in display mode and is meant to be used even in
inline mode.

.. L12

.. R12

There are appropriately named commands for inserting greek alphabets.
There are also commands for inserting spaces as required and is intended to be
used mainly for mathematical formulae. The relevant commands are shown on the
screen, in the table.

.. L13

.. R13

We can easily produce a bibliography with the bibliography environment.
Each entry is added in the bibliography environment with the bibitem command.
The marker used in the bibitem command is used to cite the source at the place
required.
If you do not use the label parameter to manually specify an index, the entries
get enumerated automatically. Please pause the tutorial and go through the 
example shown on the screen.

.. L14

{{{continue from paused state}}}

.. R14

It is highly recommended to use beamer to create presentations, especially when
you are using LaTeX for your report. This is mainly because, it would be really
easy to reuse the original content for your presentation.
 
We begin a beamer presentation with the command document with an argument
with the value beamer. This tells LaTeX to start a beamer presentation.

A beamer document is very similar to other LaTeX documents, with the exception
that content is divided into slides.

.. L15

.. R15

The usetheme command is used to specify the theme to be used for the current
presentation. The usecolor theme command is used to specify the color theme to
be used in the current presentation. The contents of a slide are enclosed 
within the begin frame and end frame environment.

If we have to use the the verbatim environment inside a slide, then we have to
pass an additional argument to begin frame, which is fragile.

Overlays and simple animation can be achieved using the pause command.

We recommend you look at the beamer user guide, to get more acquainted with 
this marvelous utility.

.. L16

.. R16

This screen shows a very basic LaTeX presentation done using beamer. We use the
warsaw theme. There are three slides in the actual document definition, but we
see more than 3 slides in the output document. This is because of the overlay 
we created in the last slide. Please pause the tutorial and go through the
example shown on the screen.

.. L17

{{{continue from paused state}}}
{{{ Show summary slide }}}

.. R17

This brings us to the end of this tutorial. In this tutorial, we have,

.. 1. Written and typeset simple math formulae in LaTeX.
.. #. Written bibliography for a LaTeX document.
.. #. Made a sample presentations in LaTeX, using beamer.

.. L18

{{{Show self assessment questions slide}}}

.. R18

Here are some self assessment questions for you to solve

 1. What is the function of useoutertheme command used in the beamer 
presentation example shown before ?? what happens when you comment out or
remove the line.

 2. Are commands like \alpha, \beta ,etc commands provided by amsmath package ?

.. L19

{{{Show self assessment questions slide}}}

.. R19

And the answers,

1. The outertheme command in beamer is used to customize the amount of 
header/footer information shown in each slide. In the example shown below the
useoutertheme command with infolines argument automatically adds more 
information to the footer like page number, author and institute,etc.

2. No, commands like alpha, beta, etc are not commands provided by the amsmath
package.

.. L20

{{{ Show the thankyou slide }}}

.. R20

Hope you have enjoyed this tutorial and found it useful.
Thank you!
