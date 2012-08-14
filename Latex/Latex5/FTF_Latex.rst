--------
Script
--------

.. L1

{{{ Show the title slide}}}

.. R1

Hello friends and welcome to the tutorial on Latex: Tables & Figures. 

.. L2

{{{Show the slide containing the objectives}}}

.. R2

In this tutorial we will learn how to:

1. Add figures in Latex document.

#. Include tabular environments in Latex document.

.. L3

{{{Show the slide 'Prerequisites'}}}

.. R3

Please make sure that you have gone through the following tutorials before you
continue on this tutorial:

1. Latex Installation
#. Latex Introduction
#. Latex Basics & Structuring
#. Latex Typesetting Text

.. L4

{{{Show the slide 'Figures'}}}

.. R4
Let us start with seeing how to include 'figures' in a Latex document.
To include graphics in a LaTeX document, we need to use the <graphicx> package.
To use this package, we have to add the <\\usepackage{graphicx}> directive
to the preamble of the document.

Then, to add a graphic, use the <\\includegraphics> command. 
The relative path of the image that we wish to include is passed as an
argument to includegraphics. You can see two images in each slide of this
presentation, these images are included using <\\includegraphics> command.
It takes an optional argument, to scale an image. For our images a scale
of 0.80 is used.
 
.. L5
 
{{{Show slide 'includegraphics'}}}
 
.. R5
 
<\\includegraphics> command also takes other optional arguments such as:

1. <width=x, height=x>

If only the height or width is specified, the image is scaled, 
maintaining the aspect ratio.

#. <keepaspectratio>

This parameter can either be set to true or false. 
When set to true, the image is scaled according to both width and height, 
without changing the aspect ratio, so that it does not exceed both the 
width and the height dimensions.

#. <angle=x>

This option can be used to rotate the image by x degrees, counter-clockwise.


.. L6
 
{{{Show slide 'includegraphics..'}}}
 
.. R6
 
Here is the complete syntax for <\\includegraphics> command with 
the optional arguments we just talked about and the relative path 
to the image.

.. L7

{{{Show the slide 'Floats'}}}

.. R7

Graphics (and tables) are treated specially because, 
they cannot be split into pages. 
They are "floated" across to the next page, 
if they do not fit on the current page, filling the current page with text. 
To make our graphic into a float, we should enlose it within 
a figure environment. The figure environment takes an additional parameter 
for the location of the float.

.. L8

{{{Show the slide 'Floats..'}}}

.. R8

The specifiers 't','b','p','h' & '!' are permissions to place the float at
various locations. 
't' for top of page, 'b' for bottom of page, 'p' for a separate page for 
floats and 'h' for here, as in pproximately at the same point it occurs in 
the source text. '!' mark overrides few of LaTeX's internal parameters 
for good position of floats.


.. L9

{{{Show the slide Captions and References}}}

.. R9

The figure environment also, allows us to add a caption to the graphic
using the <\\caption> command. This command will be placed within the figure 
environment.
To keep the graphic center aligned in the page, 
we use the center environment within the figure environment.
To label a figure, we just add a <\\label> command within the 
figure environment. 
Note that the label to a figure should be added after the caption command.
Figures are auto numbered.

.. L10

{{{Show the slide Captions and References..}}}

.. R10

Here, you can see a sample code that shows the use of figure environment
with caption & label.
It explains how to include image, how to center align it.
Also shows, how to add caption and label to an image.
You can note that the label is added after the caption, as we mentioned
earlier.


.. L11

{{{Show the slide 'Tables'}}}

.. R11

Now, let us look at how to include Tables in our document. 
To typeset content in a tabular format, we use the tabular environment. 
And to make it a float, it is enclosed in the table environment. 
The table environment also allows us to add captions & labels to the table,
just as we added in the figure environment. 
Tables are also auto numbered.

.. L12

{{{Show the slide 'tabular'}}}

.. R12

The tabular environment takes the columns, and the formatting of each column,
as arguments. The possible arguments to the tabular environment are

1. l for left justified column content

#. r for right justified column content

#. c for centered column content

#. | (pipe) produces a vertical line.


.. L13

{{{Show the slide 'tabular..'}}}

.. R13

Tabular also takes an optional parameter that specifies the position
of the table; 't' for top, 'b' for bottom, or 'c' for center.
Each column of a table is separated by an '&' (ampersand) symbol and 
each row is separated by a new line.
 
The <\\hline> command allows you to draw horizontal lines between 
two rows of the table. 

.. L14

{{{Show the slide 'tabular..'}}}

.. R14

A sample code that shows the complete use of the tabular
environment with all arguments and options.


.. L15

{{{Show the slide 'List of Tables, Figures'}}}

.. R15

You could also add a list of tables or list of figures to the document, 
using <\\listoftables> & <\\listoffigures> commands respectively.

.. L16

{{{Show the 'summary' slide'}}}

.. R16

This brings us to the end of the tutorial. In this tutorial, we have
learnt to,

1. Add graphics to a LateX document

#. Include tabular environments in a LateX document


.. L17

{{{Show self assessment questions slide}}}

.. R17

Here are some self assessment questions for you to solve,

1. Which input parameter is used in the figure environment to make it float
   to the bottom of the page ?
#. What is the mandatory argument in tabular environment specification ?

.. L18

{{{Show the solutions slide to self assessment questions }}}

.. R18

And the answers,

1. Input parameter `b' is passed as argument, to make it float to the bottom
   of the page.
#. It is mandatory to specify alignment of each column in tabular 
   environment.


.. L19

{{{ Show the SDES & FOSSEE slide }}}

.. R19

Software Development techniques for Engineers and Scientists - SDES, is an 
initiative by FOSSEE. For more information, please visit the given link.

Free and Open-source Software for Science and Engineering Education - FOSSEE,
is based at IIT Bombay which is funded by MHRD as part of National Mission on 
Education through ICT.

.. L20

{{{ Show the About the Spoken Tutorial Project slide }}}

.. R20

Watch the video available at the following link. It summarises the Spoken 
Tutorial project.If you do not have good bandwidth, you can download and 
watch it. 

.. L21

{{{ Show the Spoken Tutorial Workshops slide }}}

.. R21

The Spoken Tutorial Project Team conducts workshops using spoken tutorials,
gives certificates to those who pass an online test.

For more details, contact contact@spoken-tutorial.org

.. L22

{{{ Show the Acknowledgements slide }}}

.. R22

Spoken Tutorial Project is a part of the "Talk to a Teacher" project.
It is supported by the National Mission on Education through ICT, MHRD, 
Government of India. More information on this mission is available at the 
given link.

.. L23

{{{ Show the Thankyou slide }}}

.. R23

Hope you have enjoyed this tutorial and found it useful.
Thank you!

 


