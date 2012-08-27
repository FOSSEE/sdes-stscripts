------
Script
------

.. L1

{{{ Show the title slide }}}

.. R1

Hello friends and welcome to the tutorial on "LaTeX: Basics & Structure".

.. L2

{{{ Show the "Objectives" slide }}}

.. R2

At the end of this tutorial, you will be able to,

1. Understand basic structure of a LaTeX document, its various document
   classes and loading packages that add new features to the LaTeX system
#. Create a LaTeX document with a title and an abstract

.. L3

{{{ Show the "Objectives.." slide }}}

.. R3

3. Create numbered and non-numbered, sections and subsections in a LaTeX
   document
#. Create an appendix in a LaTeX document
#. Create a table of content in a LaTeX document


.. L4

{{{ Show the "Pre-requisite" slide }}}

.. R4

Before beginning this tutorial, we would suggest having a working installation 
of LaTeX and also complete the tutorial "Introduction to LaTeX".

.. L5

{{{ Show the "A Very Basic LaTeX document" slide }}}

.. R5

We begin this tutorial with an example introduced in the previous tutorial.
The text in the document is illustrative and can be replaced by a 
single alpha-numeric character, for example. When done so, the resulting 
document could be described as the shortest possible LaTeX input document, that
creates an output file. It consists of 3 LaTeX commands and one line/character
of text.

In our minimal example, document is an environment. Only the text enclosed by 
the begin and end commands is effected by the environment. The part of the file
before the <\\begin{document}> command is called the preamble, and is used to 
"configure" the LaTeX typesetter and change various parameters for typesetting.
In our current example, the preamble is empty. We will add preamble content
in the later part of the tutorial.

We will now see in the first line of the example we just showed,
the <\\documentclass{article}> command.

.. L6

{{{ Show the "documentclass command" slide }}}

.. R6

A LaTeX document starts with the command <\\documentclass[option]{type}>.
It is used to select the class of our document. The various classes that we can
select for our document are "article", "proc", "report", "book", "slides", 
"letter". The supported classes have a few differences, in how the content
of the document is typeset.
<\\documentclass> command can take various parameters also.
Parameters specify if you want to use a non default font size, for example.
More specifically the parameters can be used to alter things like font size of 
the document, paper size, two sided or single sided printing, etc, for each
class, that is supported by LaTeX.


.. L7

{{{ Show the "documentclass command.." slide }}}

.. R7

We now look at a hypothetical documentclass command.
The command being shown on the screen, instructs LaTeX to Create a new 
document of class report.
Optional Parameters,
"12 pt" sets the font size of main font. Other are relatively adjusted. 10pt is
the default. 
"a4paper" specifies the paper size.
"draft"  marks hyphenation and justification problems in typesetting with a 
square in the margin & makes LaTeX indicate hyphenation and justification
problems with a small square in the right-hand margin of the problem line so
they can be located quickly by a human. 
It also suppresses the inclusion of images and shows only a frame where 
they would normally occur.

.. L8

{{{ Show the "usepackage command" slide }}}

.. R8

The <\\usepackage> command is called with package name argument, prepended with
optional parameters. It is included optionally in a LaTeX document, to include
packages, which further extend the LaTeX's capabilities. There are a number of
packages that are included by default with LaTeX2 base distribution. You can
use the <texdoc> command for accessing package documentation.

.. L9

{{{ Show the "Top Matter" slide }}}

.. R9

Now let us see how to add top matter like title, author name and the date to 
the document. We add these before the <\\begin{document}> directive.
<\\title{}> command is used to add title to our document, similarly,
<\\author{}> is used to add the author name & <\\date{}> command adds the
current date to our document. We then compile the document to see if the
details appear in the document, but they do not.

.. L10

{{{ Show the "Top Matter.." slide }}}

.. R10

The command <\\maketitle> adds title, author name and date to the output file.
Of these, only the date is optional. The date command can be called with an 
optional parameter. If the optional parameter is not provided, the date of 
compilation of the LaTeX document is used. The parameter, if specified is used 
to override this value. The given example here will create a very simple
document with title, author name & date along with the written content.

.. L11

{{{ Show the "abstract command" slide }}}

.. R11

The abstract environment is used to insert the abstract of a document, into the 
output file. The content that we require as the abstract is placed between
<\\begin{abstract}> & <\\end{abstract}> command. 
Place it in the location, where you want your abstract to present in the
document. It is available for the document classes article and report, 
but not for the book class.

.. L12

{{{ Show the "abstract command".. slide }}}

.. R12

Given here is a simple latex document with abstract and other top matter.

.. L13

{{{ Show the "Sectioning" slide }}}

.. R13

Titles, chapters and sections are used to help the user find his or her way
through your work. The following commands are available in the article class:
<\\section>, <\\subsection>, <\\subsubsection>. We can create either numbered
sections or un-numbered sections based on requirement. The default behavior is 
to use numbered sections. We can use un-numbered sections by appending '*' 
(star) to section command. If you want to split your document without 
influencing the section or chapter numbering, use the part command.

.. L14

{{{ Show the "Sectioning".. slide }}}

.. R14

Given here is an example of sectioning in Latex document.


.. L15

{{{ Show the "Creating Chapters" slide }}}

.. R15

Longer documents can use report or book class. We can add a new chapter using
the <\\chapter> command, provided by the report or book class. Please keep in
mind that 'books' class in Latex do not have abstract environment.

.. L16

{{{ Show the "Creating Chapters".. slide }}}

.. R16

Given here is as example to create chapters in our Latex document.

.. L17

{{{ Show the "Appendix" slide }}}

.. R17

Appendix can be added to the document using <\\appendix> command. Any content 
after the <\\appendix> command will be added to the appendix. In the report or 
book class, we have to use <\\chapter> command to indicate that the chapters
are to be numbered as appendices.
Similarly for the article class, we have to use the <\\section> command to
indicate the sections that are to be numbered as appendices.

.. L18

{{{ Show the "Table of Contents [TOC]" slide }}}

.. R18

Now let us see how to add table of content in our document.
We use the <\\tableofcontents> command to add a TOC to a document is and is
placed at the point at which the table of content is to be placed.
It must be noted that <\\tableofcontents> command requires the LaTeX input file
to be compiled twice. On the first compilation only the "Contents" heading
appears in the document, but the actual table does not appear.
LaTeX has now gone through the input document and generated a temporary file
(.toc), with the entries that should go into the table of contents.
When the input document is compiled for the second time, these entries are made
and the actual table will appear in your output document. 
Note that any section/block that has been numbered automatically appears in the
table of contents. It is possible to get un-numbered sections, for instance a
Preface or a Foreword section to appear in the Table of Contents.

.. L19

{{{ Show the "TOC.." slide }}}

.. R19

Un-numbered sections are added to TOC using <\\addcontentsline> command.
For example we use the <\\addcontentsline> command called with the parameters
"{toc}{section}{Intro}", for the text "Intro" to appear in the Table of 
contents.

.. L20

{{{ Show the "Exercise 1" slide }}}

.. R20

We have seen the structure & basics of a Latex document, here is an exercise 
for you to perform.

Write a LaTeX script that creates a document of type book, containing both a
TOC at the beginning and an appendix at the end of document. 
The book should contain two chapters with numbered and un-numbered sections 
these chapters should appear in the TOC. 
Please pause the tutorial try out the excercise & resume for the solution.

.. L21

{{{continue from paused state}}}
{{{ Show the "Excercise 1: Solution" slide }}}

.. R21

This slide on screen shows a possible valid solution to the given exercise.
Note that this file has to be compiled twice for the TOC contents to appear.


.. L22

{{{ Show the "Summary" slide }}}

.. R22

This brings us to the end of this tutorial. In this tutorial, we have,

1. Understood the basic structure of a LaTeX document, its 
   various document classes and loading packages that add new features to 
   the LaTeX system.
#. Created a LaTeX document with a title and an abstract.


.. L23

{{{ Show the "Summary.." slide }}}

.. R23

#. Created both numbered and non-numbered sections and subsections in a 
   LaTeX document.
#. Created an appendix in a LaTeX document.
#. Created a table of content in a LaTeX document.


.. L24

{{{ Show the "Self assessment" slide }}}

.. R24

Here's a self assessment question for you to solve,

Is the LaTeX code given below a valid input file ? (File compiles successfully
and produces the intended result, that is to produce a book with two chapters 
and an appendix)

.. L25

{{{ Show the "Solution" slide }}}

.. R25

And the answer,

1. Although the given file looks syntactically valid, the output file is not 
what we expected. This is mainly because we are trying to use the section 
command to create sections in the appendix, for a document whose type is given
as a book.


.. L26

{{{ Show the SDES & FOSSEE slide }}}

.. R26

Software Development techniques for Engineers and Scientists - SDES, is an 
initiative by FOSSEE. For more information, please visit the given link.

Free and Open-source Software for Science and Engineering Education - FOSSEE, 
is based at IIT Bombay which is funded by MHRD as part of National Mission on 
Education through ICT.

.. L27

{{{ Show the ``About the Spoken Tutorial Project'' slide }}}

.. R27

Watch the video available at the following link. It summarises the Spoken 
Tutorial project.If you do not have good bandwidth, you can download and 
watch it. 

.. L28

{{{ Show the `` Spoken Tutorial Workshops'' slide }}}

.. R28

The Spoken Tutorial Project Team conducts workshops using spoken tutorials,
gives certificates to those who pass an online test.

For more details, contact contact@spoken-tutorial.org

.. L29

{{{ Show the Acknowledgements slide }}}

.. R29

Spoken Tutorial Project is a part of the "Talk to a Teacher" project.
It is supported by the National Mission on Education through ICT, MHRD, 
Government of India. More information on this mission is available at the 
given link.

.. L30

{{{ Show the Thankyou slide }}}

.. R30

Hope you have enjoyed this tutorial and found it useful.
Thank you!
