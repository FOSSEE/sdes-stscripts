
.. Prerequisites
.. -------------

.. None

.. Author : Primal Pappachan
   Internal Reviewer : Kiran Isukapatla
   Date: Jan 8, 2012
--------
Script
--------

.. L1

{{{ Show the first slide containing title, name of the production team along with the logo of MHRD}}}

.. R1

Hello friends and welcome to the second tutorial on Latex. 

.. L2

{{{Show the slide containing the objectives}}}

.. R2

At the end of this tutorial you will be able to

1. Learn how to typeset your document using LaTEX

#. Use lists, listings in your document for formatting text

.. L3

{{{Show the slide 'Prerequisite'}}}

.. R3

Please make sure that you have gone through the following tutorials before you continue on this tutorial

.. L4

{{{Show the slide 'Quotation Marks'}}}

.. R4

Look at the quotation marks around the text, Sigh Pie. They are not formatted properly.

.. L5

{{{Show rev11 of hg}}}

.. R5

To place quotation marks in LaTeX, you should use ` character for the left quote & ' character for the right quote. For double quotes, they should be used twice.

.. L6

{{{Show the slide 'Fonts'}}}

.. R6

The names of the software tools, Scilab, Matlab, etc. appear in italics or emphasized as it is called in LaTeX. 

.. L7

{{{Show rev12 of hg}}}

.. R7

To emphasize text, the \emph command is used.

.. R8

Let's try and form a tabular structure by separating the left and right columns using spaces. On compiling we find that LaTeX doesn't add multiple spaces between words. Just like multiple empty lines, multiple spaces are considered as a single space.

Also, you would have noticed that LaTeX starts a new paragraph at the beginning of the table. To avoid this, we use the flushleft environment.

.. L8

{{{Show slides second part of 'Fonts'}}}

.. R9

\textbf is used to change text to bold face and \texttt is used to change text to fixed width font.

.. L9

{{{Show rev13 of hg}}}

.. R10

We could also change the separating - (hyphen) to an em-dash (or en-dash) -- is em-dash and --- is an em-dash, to improve the appearance of the document.

.. L10

{{{Show the slides Lists }}}

.. R11

The section on Use of Scipy in this course, contains lists. Let's now add lists to our document. 

.. L11

{{{Show rev14 of hg}}}

.. R12

The enumerate environment adds numbered lists to our document and the itemize environment adds un-numbered lists. \item command adds a new entry to a list. Note, that LaTeX can easily handle nested lists. In fact most environments can be embedded within other environments, without any problems.


.. L12

{{{Show slides 'Footnotes'}}}

.. R13

Let's now add the footnote to pylab. LaTeX provides a footnote command to add a footnote.


.. L13

{{{Show rev15 of hg}}}

.. R14

In case we wish to add another Appendix before the section on using pylab, the footnote will have to be edited. To avoid this, LaTeX provides a handy system of labels and referencing.

.. L14

{{{Show the slide 'Labels and References'}}}

.. R15

We first add a label to the section that we want to refer in this footnote. Then, we change the footnote, and add the reference to this label instead of the character A. If you look at the output after compiling the document once, you will see that the footnote has question marks instead of the section number. You will have to compile once again, for the section number to appear in the footnote.

.. L15

{{{Show rev15 of hg}}}


.. R16

LaTeX by default provides the verbatim environment to include pre-formatted text. You can try that out during the lab session. We shall look at using the listings package, specifically meant for including code in our document.

.. L16

{{{Show the slide 'Include Code'}}}

.. R17

First of all you need to tell LaTeX, that you want to use the listings package in your document. We add the directive \usepackage{listings} to the preamble of our document.

Then we set the language of the code that we are going to embed into our document. For this we use the lstset command.

.. L17

{{{Show rev16 of hg}}}

.. L18

{{{Show slide 'Including code'}}}

.. R18

Now, to put a line of code, inline and not as a separate block, we use the \lstinline command. We change the name pylab in the footnote to use lstinline instead of the texttt. To embed a block of code, we use the lstlisting environment (\begin{lstlisting} and \end{lstlisting}).

.. L19

{{{Show rev16 of hg}}}

.. R19

For example, let's add the code to the Appendix of our document.

.. L20

{{{Show the 'summary' slide'}}}

.. R20

This brings us to the end of the tutorial. In this tutorial, we have
learnt to,

1. Put Quotation Marks around text

#. How to Emphasize and give fixed width to fonts.

#. Use numbered and un-numbered lists

#. Add Footnotes, Labels and References

#. Use the listings package to include code

.. L21

{{{Show self assessment questions slide}}}

.. R21

Here are some self assessment questions for you to solve

.. L22

{{{Show the solutions slide to self assessment questions }}}

.. R22

And the answers,


.. L23

{{{Show the thank you slide}}}

.. R23

Hope you have enjoyed this tutorial and found it useful.
Thank you

