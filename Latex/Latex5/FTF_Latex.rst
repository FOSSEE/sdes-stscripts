
.. Prerequisites
.. -------------

.. None

.. Author : Primal Pappachan
   Internal Reviewer : Kiran Isukapatla, Sushma Dubey
   Date: Jan 15, 2012
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

1. Learn how to add figures to your document

#. Include tabular environments

.. L3

{{{Show the slide 'Prerequisite'}}}

.. R3

Please make sure that you have gone through the following tutorials before you continue on this tutorial

.. L4

{{{Show the slide 'Figures'}}}

.. R4

To include graphics in a LaTeX document, we need to use the graphicx package. Add the \usepackage{graphicx} directive to the preamble of the document.

To add the graphic, use the includegraphics command. The relative path of the image that we wish to include is passed as an argument to includegraphics. It takes an optional argument of scaling the image.

.. L5

{{{Show rev17 of hg}}}

.. R5

We use a scale of 0.4 to scale our image.
 
.. L6
 
{{{Show slide 'includegraphics'}}}
 
.. R6
 
It takes other optional arguments.

1. width=x, height=x

If only the height or width is specified, the image is scaled, maintaining the aspect ratio.

#. keepaspectratio

This parameter can either be set to true or false. When set to true, the image is scaled according to both width and height, without changing the aspect ratio, so that it does not exceed both the width and the height dimensions.

#. angle=x

This option can be used to rotate the image by x degrees, counter-clockwise.

.. L7

{{{Show the slide 'Floats'}}}

.. R7

Figures (and tables) are treated specially because, they cannot be broken across pages. They are "floated" across to the next page, if they donot fit on the current page, filling the current page with text. To make our graphic into a float, we should enlose it within a figure environment. The figure environment takes an additional parameter for the location of the float.

.. L8

\begin{figure}[hbtp!]

.. R8

The specifiers htbp are permissions to place the float at various locations. t for top of page, b for bottom of page, p for a separate page for floats and h for here, as in the same place where the command appears in the source. ! mark overrides a few of LaTeX's internal parameters for good position of floats.

.. L9

{{{Show the slide Captions and References}}}

.. R9

The figure environment also, allows us to add a caption to the graphic using the \caption command.

To place the graphic in the center aligned in the page, we use the center environment.

To label a figure, we just add a label with in the figure environment. Note, that the label to a figure should be added after the caption command.

.. L9

{{{Show rev17 of hg}}}

.. R9

Figures are auto numbered

.. L10

{{{Show the slide 'Tables'}}}

.. R10

Now, let us look at the other kind of floats - Tables. We shall convert the list of sub-packages in the sub-packages section to a table.

To begin a table, we use the tabular environment. And to make this a float, it is enclosed in the table environment. The table environment also allows us to add captions to the table and Tables are also auto numbered.

.. L11

{{{Show the slide 'tabular'}}}

.. R11

The tabular environment takes as arguments the columns and the formatting of each column. The possible arguments to the tabular environment are

1. l for left justified column content

#. r for right justified column content

#. c for centered column content

#. | for produces a vertical line.

It also takes an optional parameter that specifies the position of the table; t for top, b for bottom, or c for center.

.. L12

{{{Show rev18 of hg}}}

.. R12

Each column of a table is separated by an & symbol and each row is separated by a new line. The \hline command allows you to draw horizontal lines between two rows of the table. 

.. L13

{{{Show the slide 'List of Tables, Figures'}}}

.. R13

You could also add a listoftables or listoffigures to the document, similar to the way we added table of contents.

.. L14

{{{Show the 'summary' slide'}}}

.. R20

This brings us to the end of the tutorial. In this tutorial, we have
learnt to,

1. Add graphics to a LateX document

#. Include tabular environments in a LateX document


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







 


