
.. Prerequisites
.. -------------

.. None

.. Author : Primal Pappachan
   Internal Reviewer : Kiran Isukapatla
   Date: Jan 13, 2012
--------
Script
--------

.. L1

{{{ Show the first title slide }}

.. R1

Hello friends and welcome to the tutorial on Typesetting Text in Latex. 

.. L2

{{{Show the slide containing the objectives}}}

.. R2

At the end of this tutorial you will learn how to:

1. Typeset your document using LaTEX.

#. Use lists, listings in your document for formatting text.

.. L3

{{{Show the slide 'Prerequisites'}}}

.. R3

Please make sure that you have gone through the following tutorials before you
continue on this tutorial:

1. Latex Installation
2. Latex Introduction
3. Latex Basics & Structuring


.. L4

{{{Show the slide 'Quotation Marks'}}}

.. R4
Let us begin with how to add qutation marks to our document.
For this, we use ` (accent) character for the left quote &
' (apostrophe) character for the right quote. 
For double quotes, we use them twice.

.. L5

{{{Show the slide Fonts-emphasizes, fixed width}}}

.. R5

The <\emph> command is used to give the text an emphasized & italic effect.
In tabular structures, LaTeX doesn't add multiple spaces between words. 
Just like multiple empty lines, multiple spaces are considered 
as a single space.
Also, LaTeX starts a new paragraph at the beginning of the table. 
To avoid this, we use the 'flushleft environment' to have left aligned text.
Similarly 'flushright' & 'center' to have right & center aligned text
respectively.

.. L6

{{{Show the slide Fonts-emphasizes, fixed width..}}}

.. R6

<'\texttt'> is used to change text to fixed width font & 
<'\textbf'> is used to change text to bold face.
We could also change the separating - (hyphen) to -- (n-dash) or --- (em-dash)
to improve the appearance of the document.

.. L7

{{{Show the slide Lists }}}

.. R7

The 'enumerate' environment adds numbered lists to our document and
the itemise environment adds un-numbered lists. <\item> command adds 
a new entry to a list. Note, that LaTeX can easily handle nested lists. 
In fact, most environments can be embedded within other environments, 
without any problems.


.. L8

{{{Show slide 'Footnotes'}}}

.. R8

LaTeX provides a footnote command to add a footnote.
In case we wish to add another Appendix before the section, the footnote has 
to be edited. To avoid this, LaTeX provides a handy system 
of labels and referencing.

.. L9

{{{Show the slide 'Labels and References'}}}

.. R9

We can create labels for any elements in the document and then refer them
anywhere in the document.
<\\label{label-name}> command is used to create a label for a particular
element. Then, to refer to that element with a label, <\\ref{label-name}> 
command is used.

But, remember that when you compile the document first time, you will see
question marks instead of the element you have referred using labels.
Do not worry, you just have to compile the document once again to make the
elements referred by labels to appear.

So, whenever you use the labels & references remember to compile the document
twice.

.. L10

{{{Show the slide 'Code Inclusion'}}}

.. R10

Now let us see how we can include code in our Latex document.
LaTeX by default provides the verbatim environment to include
pre-formatted text. 
But, we shall look at using the listings package, specifically meant for 
including code in our document.

First of all, we need to tell LaTeX, that we want to use the 
listings package in our document. We do this by adding the directive 
<\usepackage{listings}> to the preamble of our document.
Then, we specify the language of the code that we are going to embed 
into our document. This can be done in two ways,
directly specifying it while declaration <\lstinputlisting[language=Python]> 
or we can use the <'lstset'> command.


.. L11

{{{Show slide 'Code Inclusion..'}}}

.. R11

Now, to put a line of code (inline and not as a separate block), 
we use the <\lstinline> command. To embed a block of code, we use 
the lstlisting environment <(\begin{lstlisting} and \end{lstlisting})>.

.. L12

{{{Show the 'summary' slide'}}}

.. R12

This brings us to the end of the tutorial. In this tutorial, we have
learnt to,

1. Add Quotation Marks around text.

#. Emphasize and give fixed width to fonts.

#. Use numbered and un-numbered lists.

#. Add Footnotes, Labels and References.

#. Include code.

.. L13

{{{Show self assessment questions slide}}}

.. R13

Here are some self assessment questions for you to solve.

1. Which environment is used to include a block of code?

2. Joe has used numerous labels inside his Latex document. 
But all the references to label names come up as question marks. 
What might be the problem?


.. L14

{{{Show the solutions slide to self assessment questions }}}

.. R14

And the answers are,

1. Use the lstlistings package to include code.

2. While using labels, the latex document should be compiled twice 
for the references to show up.



.. L15

{{{ Show the SDES & FOSSEE slide }}}

.. R15

Software Development techniques for Engineers and Scientists - SDES, is an 
initiative by FOSSEE. For more information, please visit the given link.

Free and Open-source Software for Science and Engineering Education - FOSSEE,
is based at IIT Bombay which is funded by MHRD as part of National Mission on 
Education through ICT.

.. L16

{{{ Show the About the Spoken Tutorial Project slide }}}

.. R16

Watch the video available at the following link. It summarises the Spoken 
Tutorial project.If you do not have good bandwidth, you can download and 
watch it. 

.. L17

{{{ Show the Spoken Tutorial Workshops slide }}}

.. R17

The Spoken Tutorial Project Team conducts workshops using spoken tutorials,
gives certificates to those who pass an online test.

For more details, contact contact@spoken-tutorial.org

.. L18

{{{ Show the Acknowledgements slide }}}

.. R18

Spoken Tutorial Project is a part of the "Talk to a Teacher" project.
It is supported by the National Mission on Education through ICT, MHRD, 
Government of India. More information on this mission is available at the 
given link.

.. L19

{{{ Show the Thankyou slide }}}

.. R19

Hope you have enjoyed this tutorial and found it useful.
Thank you!
