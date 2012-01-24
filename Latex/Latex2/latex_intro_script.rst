.. Objectives
.. ----------

.. By the end of this tutorial, you will 

.. 1. Get acquainted to LaTeX.
.. #. Know why we prefer LaTeX?
.. #. Know the advantages and disadvantages of typesetting documents  
..    using the LaTeX approach.
.. #. Have a description, of a typical work flow; which uses LaTeX to typeset 
..    documents.
.. #. Recognise and differenciate between LaTeX commands, LaTeX comments and
..    special characters, spacing and actual document content.
.. #. Create and compile a very simple LaTeX document.

.. Prerequisites
.. -------------

.. 1. Should have already installed LaTeX and its supported packages on the host machine.
.. #. Should be comfortable using a text editor of your choice. 

     
.. Author              : Harish Badrinath < harish [at] fossee [dot] in > 
   Internal Reviewer   : Kiran Isukapatla < kiran [at] fossee [dot] in >
   External Reviewer   :
   Langauge Reviewer   : 
   Checklist OK?       : <put date stamp here, if OK> 

Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello Friends and welcome to the tutorial on introduction to LaTeX. 

.. L2

{{{ Show the objectives slide }}}

.. R2

.. By the end of this tutorial, you will 

.. 1. Get acquainted to LaTeX.
.. #. Know why we prefer LaTeX?
.. #. Know the advantages and disadvantages of typesetting documents  
..    using the LaTeX approach.
.. #. Have a description, of a typical work flow; which uses LaTeX to typeset 
..    documents.
.. #. Recognize and differentiate between LaTeX commands, LaTeX comments and
..    special characters, spacing and actual document content.
.. #. Be able to create and compile a very simple LaTeX document.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial, we would suggest having a working installation of
LaTeX on your computer. You can do this by completing the tutorial titled 
"Installing LaTeX".

.. L4


.. R4

LaTeX began as TeX, a computer program originally created by
Donald E. Knuth. Its was designed mainly to aid typesetting
of text and mathematical formulae. 

LaTeX is a document preparation system for high quality type 
setting. It is based on the TeX typesetting language or certain
extensions.

LaTeX is pronounced Lah-tech or Lay-tec.
TeX is pronounced Tech. TeX is also the first syllable in the Greek word for
technology.
LaTeX allows authors to typeset and print their content at the highest
typographical quality, using predefined, professional layouts.

.. L5


.. R5

Below are some of the reasons we prefer LaTeX
(a) LaTeX offers excellent visual quality.
(b) It handles typesetting and lets you focus on content.
(c) Its makes writing complex math equation extremely simple.
(d) It is also a standard used widely, especially by the scientific community. 

We can define LaTex as a document based markup language. This sentence is
deceptively simple, as it reveals a lot about LaTex. We now break this sentence
up as follows
Mark-up — a system of annotating text, adding extra information to
specify structure and presentation of text
Document based markup - you don’t have to worry about each
element individually.
This is essentially a fancy way of saying,LaTeX handles typesetting and lets 
you focus on content.

.. L6


.. R6

Some of the advantages of using LaTeX approach to typesetting are
(1) Easy availability of professionally crafted layouts.
(2) Typesetting of mathematical formulae is supported in a convenient
environment.
(3) Typesetting for most cases can be done with very little learning curve
using easy to use/understand commands, that only specify the logical structure
of the document.
(4) Presence of lots of add-on packages.
(5) It encourages creation of well structured texts.

.. L7


.. R7

Some of the disadvantages of using LaTeX approach to typesetting is 
(1) Designing a whole new layout is difficult.

.. L8


.. R8

LaTeX input files are simple ASCII text files that are processed by a TeX
processing engine. 
Next comes the question compiling LaTeX input files and viewing the output
typeset document.
The process is a little different from other markup languages like HTML.
We compile ASCII text files into typeset files that are normally DVI,Postscript
or PDF files.
The latex command converts LaTeX input files into dvi files.
We can view DVI files on Gnu/Linux using xdvi.
Further  DVI files can be converted either to a post script file, using the
dvips command or to a PDF file using the dvipdfm command.
The command pdflatex is used to convert LaTeX input files directly to pdf files.
The resultant PDF files can be viewed using standard tools on most platforms
(Eg: evince on Gnu/Linux). PDF file are also widely supported.

.. L9


.. R9

LaTeX, like most utilities in Linux is case sensitive. Commands begin with a
backslash.LaTeX environments have a begin and end marker. Any content after
\end{document} is ignored.

Anything that follows a percentage sign (%) till the end of that line is a
comment. Special characters like tilde or hash,etc have to be escaped by a
backslash. If you have to insert a backslash into a LaTeX output file, you have
to use the LaTeX command \textbackslash.

Normally LaTeX automatically spaces the given input optimally. But, sometimes we
have to insert manual line breaks. This is achieved using the \\ command.

We can also start a new paragraph using an empty line.

It must be noted that multiple spaces/empty lines are automatically compressed 
to a single space/line.

.. L10

{{{ Show slide with exercise 1 }}}

.. R10

Now, we try to create a simple LaTeX document. Pause the tutorial and type the
content shown on the screen in a text editor. Save the file as temp.tex

.. L10

{{{continue from paused state}}}

.. R10

Now we compile the commands in the LaTeX input file that is, temp.tex into a 
typeset file.
The first alternative is to compile LaTeX input file into a DVI file. We use 
the latex command for this purpose.
For compiling the LaTeX input file temp.tex into a DVI file, we use the
following command
latex temp.tex. 
The output file would be temp.dvi.
On Gnu/Linux use a program like xdvi to view the output file.

.. L11


.. R11

The other alternative is to create PDF files from LaTeX input files.
We use the pdflatex command for this purpose. 
For compiling the LaTeX input file temp.tex into a PDF file, we use the
following command
pdflatex temp.tex
The output file would be temp.pdf
On Gnu/Linux use a program like evince to view the output file.

.. L12

{{{ Show summary slide }}}

.. R12

This brings us to the end of this tutorial. In this tutorial, we have learnt

.. 1. About LaTeX.
.. #. why we prefer LaTeX.
.. #. About the advantages and disadvantages of typesetting documents  
..    using the LaTeX approach.
.. #. A description, of a typical work flow; which uses LaTeX to typeset 
..    documents.
.. #. The ability to recognize and differentiate between LaTeX commands, LaTeX
..    comments and special characters, spacing and actual document content.
.. #. Created and compiled a very simple LaTeX document.

.. L13

{{{Show self assessment questions slide}}}

.. R13

Here are some self assessment questions for you to solve

 1. Convert the temp.dvi created during the course of this tutorial to temp_1.ps
using the dvips command. Verify that the two files indeed look the same.

 2. Convert the temp.dvi created during the course of this tutorial to
temp_1.pdf using the dvipdfm command. Verify that the two files indeed look the
same.

.. L14

{{{Show self assessment questions slide}}}

.. R14

And the answers,

1. We can use the following command to convert temp.dvi to temp_1.ps
dvips -o temp_1.ps temp.dvi

2. We can use the following command to convert temp.dvi to temp_1.pdf
dvipdfm -o temp_1.pdf temp.dvi

.. L15

{{{ Show the thank you slide }}}

.. R15

Hope you have enjoyed this tutorial and found it useful.
Thank you!
