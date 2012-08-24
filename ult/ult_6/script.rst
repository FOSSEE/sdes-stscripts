.. Objectives
.. ----------
   
   .. At the end of this tutorial, you will be able to:
   
   ..   1. Understand various features of shell
   ..   2. Learn about shell meta characters

.. Prerequisites
.. -------------

..   1. Getting started with Linux
..   2. Basic File Handling

 
Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on 
'Features of the Shell'.

.. L2

{{{ Show slide with objectives }}} 

.. R2

At the end of this tutorial, you will be able to,

 1. Understand various features of shell
 #. Learn about shell meta characters

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
previous tutorials as being displayed currently.

.. L4

{{{ Show slide, with Tab-completion }}} 

.. R4

The Bash shell has some nice features, that make our job of using the shell 
easier and much more pleasant. We shall look at a few of them, here.


Bash provides the feature of tab completion. What does tab completion mean? 
When you are trying to type a word, bash can complete the word for you, if you 
have entered enough portion of the word (to complete it unambiguously) and 
then hit the tab key.

If on hitting the tab key, the word doesn't get completed, either the word 
doesn't exist or the word cannot be decided unambiguously. If the case is the 
latter one, hitting the tab key a second time, will list the possibilities.

.. L5

{{{ Show slide, with Tab-completion.. }}} 

.. R5

Bash provides tab completion for the following.

- File Names
- Directory Names
- Executable Names
- User Names (when they are prefixed with a ~)- tilde
- Host Names (when they are prefixed with a @)- at sign
- Variable Names (when they are prefixed with a $)- dollar sign

.. R6

For example,

.. L6

{{{ Switch to terminal }}}
::


    pas<TAB><TAB>
    PA<TAB>
    ~/<TAB><TAB>

.. L7

{{{ Show slide, with History }}}

.. R7

Bash also saves the history of the commands you have typed. So, you can go 
back to a previously typed command. Use the up and down arrow keys to navigate 
in your bash history.
You can also search incrementally, for commands in your bash history. Ctrl-r 
search for the commands that you have typed before. But, note that the number 
of commands saved in the history is limited, generally upto a 1000 commands.

.. L8

{{{ Switch to terminal }}}
::

    <Ctrl-r> pas

.. R8

.. L9

{{{ Show slide, with Shell Meta Characters }}} 

.. R9

Unix recognizes certain special characters, called "meta characters," as 
command directives. The shell meta characters are recognized anywhere they 
appear in the command line, even if they are not surrounded by blank space. 
For that reason, it is safest to only use the characters A-Z, a-z, 0-9, and 
the period, dash, and underscore characters when naming files and directories
on Unix. If your file or directory has a shell meta character in the name, 
you will find it difficult to use the name in a shell command.

The characters that you see on the slide are the shell meta characters

 / < > ! $ % ^ & * | { } [ ] " ' ` ~ ;

.. R10

Let's take an example,

.. L10

{{{ Switch to terminal }}} 
::

    ls file.*

.. R11

It means, run on a directory containing the files - file.c, file.lst, and 
file.txt. However,

.. L11

::

    ls file.?

.. R12

Run on the same directory would only list file.c because the ?(question mark) 
matches only one character, in our case it is ``.c``. This can save you a great 
deal of typing time.

.. L13

{{{ Show slide, with File names }}}

.. R13

For example,if there is a file called ``california_cornish_hens_with_wild_rice``
and no other files whose names begin with 'c', you could view the file without 
typing the whole name by typing 
::

    more c*

Here, the c* matches that long file name.

Hence, File-names containing metacharacters can pose many problems and should 
never be intentionally created.

.. L14

{{{ Switch to Summary slide }}}

.. R14

This brings us to the end of the end of this tutorial.
In this tutorial, we have learnt to,

1. Implement features of tab-completion and history.
#. Make use of the shell meta characters.
 
.. L15
 
{{{ Show self assessment questions slide }}}

.. R15

Here are some self assessment questions for you to solve:

1. Bash does not provide tab completion for Host Names. True of False?

2. State the command which will list all the files in the current working 
   directory that end in either .c or .h

.. L16

{{{ Solutions for the self assessment questions on slide }}}

.. R16

And the answers:

1. False. Bash provides tab completion for Host Names when they are prefixed 
   with a @ sign.

  
2. The command which will find the files ending either in .c or .h is,
::

    ls *.[ch]


.. L17

{{{ Show the SDES & FOSSEE slide }}}

.. R17

Software Development techniques for Engineers and Scientists - SDES, is an 
initiative by FOSSEE. For more information, please visit the given link.

Free and Open-source Software for Science and Engineering Education - FOSSEE, is
based at IIT Bombay which is funded by MHRD as part of National Mission on 
Education through ICT.

.. L18

{{{ Show the ``About the Spoken Tutorial Project'' slide }}}

.. R18

Watch the video available at the following link. It summarises the Spoken 
Tutorial project.If you do not have good bandwidth, you can download and 
watch it. 

.. L19

{{{ Show the `` Spoken Tutorial Workshops'' slide }}}

.. R19

The Spoken Tutorial Project Team conducts workshops using spoken tutorials,
gives certificates to those who pass an online test.

For more details, contact contact@spoken-tutorial.org

.. L20

{{{ Show the ``Acknowledgements'' slide }}}

.. R20

Spoken Tutorial Project is a part of the "Talk to a Teacher" project.
It is supported by the National Mission on Education through ICT, MHRD, 
Government of India. More information on this mission is available at the 
given link.

.. L21

{{{ Show the Thank you slide }}}

.. R21

Hope you have enjoyed this tutorial and found it useful.
Thank you!

