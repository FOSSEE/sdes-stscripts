.. Objectives
.. ----------

.. At the end of this tutorial, you will 

.. Install LaTeX on your computer.
.. Learn how to install a plug-in for a TeX editor.
.. Configure the TeX editor with the LaTeX plug-in.
.. Useful information on some LaTeX packages.
.. Compile a TeX file to pdf.

.. Prerequisites
.. -------------

.. You'll need a TeX distribution.
.. A good text editor and a DVI or PDF viewer.
.. Updated Linux distribution as Operating System.
.. Working internet connection (for installation over the network).


.. Author              : Kiran Isukapatla < kiran [at] fossee [dot] in >
   Internal Reviewer   : Kiran Isukapatla < kiran [at] fossee [dot] in >
   External Reviewer   :
   Langauge Reviewer   : 
   Checklist OK?       : 25-Feb-2012

Script
--------

.. L1

{{{Show the first slide containing title, name of the production team along
with the logo of MHRD}}}

.. R1

Hello friends, welcome to the tutorial on 'LaTeX Installation'. 

.. L2

{{{Show the slide containing the objectives}}}

.. R2

At the end of this tutorial you will,

1. Learn how to install LaTeX.
#. Learn how to install a TeX editor plug-in.
#. Know how to configure the TeX editor for LaTeX.
#. Know some useful information on LaTeX packages.
#. Be able to compile a TeX file to pdf.

.. L3

{{{Show the slide 'Prerequisites'}}}

.. R3

Before beginning this tutorial, you will need a TeX distribution, a good text
editor, DVI or PDF viewer. Also make sure to have a Linux Distribution as
Operating System on your computer & a working internet connection for 
installing LaTeX over internet.

.. L4

{{{Show the slide 'TeX Distribution'}}}

.. R4

TeX Live is an easy way to get up and running with the TeX document production 
system. It provides a comprehensive TeX system with binaries for most flavors
of Unix, including GNU/Linux, and also Windows.

.. L5

{{{Show the slide 'Installation'}}}

.. R5

There are multiple ways of installation. You may download a LaTeX distribution
and run the installer.
An other way is to install using the command: 'sudo apt-get install texlive'
(or) 'sudo apt-get install texlive-full'.

.. L6

{{{Move onto next slide of 'Installation'}}}

.. R6

We may also install LaTeX using a package manager like 'Synaptic Package
Manager in Ubuntu'.
Using 'Synaptic Package Manager': Open the 'Package Manager' > Search for
'texlive-full' > Mark for installation and apply.


.. L7

{{{Show the slide 'LaTeX Plug-in'}}}

.. R7

We may use a Text editor (as per your choice) as LaTeX editor.
However, we require a plug-in to do this.
We would like to illustrate the same using Gedit.
Install the plug-in: 'sudo apt-get install gedit-latex-plugin'.
To activate the plug-in: Click (Edit > Preferences > Plugins >
Check LaTeX Plugin).

.. L8

{{{Show the slide 'LaTeX Packages'}}}

.. R8

Add-on features for LaTeX are known as packages. Dozens of these are
pre-installed with LaTeX and can be used in your documents immediately. 
Listed here are a few popular ones and their usage.


.. L9

{{{Show the slide 'Compilation'}}}

.. R9

A given LaTeX document may be compiled to pdf using the command:
'pdflatex filename.tex'
This produces an output file, in the pdf format.


.. L10

{{{Show the slide 'Summary'}}}

.. R10

This brings us to the end of the tutorial. In this tutorial, we have
learnt to,

1. Install LaTeX on your computer.
#. Install/Configure TeX editor with LaTeX plug-in.
#. Choose a LaTeX packages as per requirement.
#. Compile a TeX file to pdf.

.. L11

{{{ Show the slide 'Exercise' }}}

.. R11

1. How can we check the version of the LaTeX package installed ?
2. How can we check if the plug-in is properly configured with TeX editor ?

.. L12

{{{ Show the slide 'Solutions' }}}

.. R12

1. Use the command latex with -v option to check the version installed
2. In the editor select the edit menu and follow the sequence


.. L13

{{{ Show the SDES & FOSSEE slide }}}

.. R13

Software Development techniques for Engineers and Scientists - SDES, is an 
initiative by FOSSEE. For more information, please visit the given link.

Free and Open-source Software for Science and Engineering Education - FOSSEE, is
based at IIT Bombay which is funded by MHRD as part of National Mission on 
Education through ICT.

.. L14

{{{ Show the ``About the Spoken Tutorial Project'' slide }}}

.. R14

Watch the video available at the following link. It summarises the Spoken 
Tutorial project.If you do not have good bandwidth, you can download and 
watch it. 

.. L15

{{{ Show the `` Spoken Tutorial Workshops'' slide }}}

.. R15

The Spoken Tutorial Project Team conducts workshops using spoken tutorials,
gives certificates to those who pass an online test.

For more details, contact contact@spoken-tutorial.org

.. L16

{{{ Show the Acknowledgements slide }}}

.. R16

Spoken Tutorial Project is a part of the "Talk to a Teacher" project.
It is supported by the National Mission on Education through ICT, MHRD, 
Government of India. More information on this mission is available at the 
given link.

.. L17

{{{ Show the Thankyou slide }}}

.. R17

Hope you have enjoyed this tutorial and found it useful.
Thank you!
