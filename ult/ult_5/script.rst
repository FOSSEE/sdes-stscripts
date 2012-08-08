.. Objectives
.. ----------
   
   .. At the end of this tutorial, you will be able to:
   
   ..   1. Understand what is Redirection and Piping.
   ..   2. Learn various features of shell.

.. Prerequisites
.. -------------

..   1. Getting started with Linux
..   2. Basic File Handling
..   4. Advanced file handling
 
Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on 
'Redirection and Piping'.

.. L2

{{{ Show slide with objectives }}} 

.. R2

At the end of this tutorial, you will be able to,

 1. Understand what is Redirection. 
 #. Learn the concept of Piping.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
former tutorials as being displayed currently.

.. R4

Let us begin with the concept of 'Redirection and Piping'  which 
performs the  same operations as the ``cut`` and ``paste`` commands.

Consider the files ``marks.txt`` and ``students.txt``.The contents of 
the files  are as following:

.. L4

{{{ Open the terminal }}}
::

    cat marks1.txt
    cat students.txt

.. R5

Now, let us view the contents of both these files side-by-side.

.. L5
::

    cut -d " " -f 2- marks1.txt | paste -d " " students.txt -

.. R6

Now, in order to view the same output in a new file at an other 
location, we say,

.. L6
::

    cut -d " " -f 2- marks1.txt > /tmp/m_tmp.txt
    paste -d " " students.txt m_tmp.txt

.. R7

First, let us try to understand the second solution,which is a two 
step approach.
Later, we shall look at the first solution. 

.. L7

.. L8

{{{ Show slide, with Redirection }}}

.. R8

The standard output, in general, goes to the display.
But, this may not be what we always require. 

For instance, in the solution above, we use the cut command and get only
the required columns of the file and write the output to a new temporary
file. The ``>`` character is used to state that we wish to redirect the
output, and it is followed by the location to which we wish to redirect. 
For example,

    command > file1

.. L9

{{{ Show slide, with Redirection.. }}}

.. R9

Similarly, the standard input (stdin) can be redirected as,
    
    command < file1

The input and the output redirection could be combined in a single command, 
as, 

    command < infile > outfile

.. L10

{{{ Show slide, with stderr }}}


.. R10

There is actually a third kind of standard stream, called the Standard
error (stderr). Any error messages that you get, are coming through this
stream. Like ``stdout``, ``stderr`` also streams to the display by default,
but it could be redirected to a file, as well. 

.. R11

For instance, let's reproduce an error using the ``cut`` command used
before. We shall change the ``-f`` option to ``-c`` 

.. L11

{{{ Switch to terminal }}}
::

    cut -d " " -c 2- marks1.txt > /tmp/m_tmp.txt

.. R12

This displays an error saying that the delimiter option should be used 
with the fields option only. You may verify this by looking at the 
``m_tmp.txt`` file, which is now empty.We can now, redirect the 
``stderr`` also to a file, instead of showing it on the display. 

.. L12
::

    cut -d " " -f 2- marks1.txt 1> /tmp/m_tmp.txt 2> /tmp/m_err.txt

.. R13

The above command redirects all the errors to the ``m_err.txt`` file
and the output to the ``m_tmp.txt`` file. When redirecting, 1 stands
for ``stdout`` and 2 stands for ``stderr``. 

Let us complete the solution by using the ``paste`` command.

.. L13
::

    paste -d " " students.txt m_tmp.txt

.. R14

So, in two steps we solved the problem of getting rid of the roll numbers
from the marks file and displaying the marks along with the names of the
students. Now, that we know how to redirect output, we could choose to
write the output to a file, instead of showing on the display. 

Let us now look at the first solution. 

.. L14
::

    cut -d " " -f 2- marks1.txt | paste -d " " students.txt -

.. L15

{{{ Show slide, with Piping }}}

.. R15

First of all, the hyphen at the end is to ask the paste command to 
read the standard input, instead of looking for a FILE. The ``man`` 
page of ``paste`` command gives us this information. 

Now, let us observe the ``cut`` command. If we look at the command only 
upto the ``|`` character, it appears as a normal ``cut`` command .

.. L16

{{{ Show slide, with Piping.. }}}

.. R16

So, the ``|`` character here, seems 
to be joining the two commands in some way. 
Essentially, what we are doing is, to redirect the output of the first
command to ``stdin`` and the second command takes the input from the ``stdin``. 
This activity is commonly called piping and the character ``|`` is called 
a pipe. 

.. L17

{{{ Show slide, with Piping... }}}

.. R17

This is roughly equivalent to using two redirects and a temporary file.

    command1 > tempfile
    command2 < tempfile
    rm tempfile

Also, given that a pipe is just a way to send the output of a command to
the ``stdin``, it should be obvious to you that we can use a chain of
pipes. Any number of commands can be piped together and therefore it should
 be noted that it is not restricted to only two commands. 

.. L18

{{{ Switch to Summary slide }}}

.. R18

This brings us to the end of the end of this tutorial.
In this tutorial, we have learnt to,

 1. Use the ``cut`` and ``paste`` commands in redirection.
 2. Use the pipe ( | ) character. 
 
.. L19
 
{{{ Show self assessment questions slide }}}

.. R19

Here are some self assessment questions for you to solve:

1. How will you redirect the content of a file to a device ?

2. How to view last field(30), in a file located at /home/test.txt whose
   first line is "data:myscripts:20:30"
    
    - cut -d : -f 4 /home/test.txt
    - cut -f 3 /home/test.txt
    - cut -d : -f 3 /home/test.txt
   

.. L20

{{{ Solutions for the self assessment questions on slide }}}

.. R20

And the answers:

1. A file can be redirected to a device as,
::
   
    cat filename > device
For eg:
::

    cat sound.wav > /dev/audio  
    

2. The correct option would be
::
    
    cut -d : -f 4 /home/test.txt

.. L21

{{{ Show the SDES & FOSSEE slide }}}

.. R21

Software Development techniques for Engineers and Scientists - SDES, is an 
initiative by FOSSEE. For more information, please visit the given link.

Free and Open-source Software for Science and Engineering Education - FOSSEE, is
based at IIT Bombay which is funded by MHRD as part of National Mission on 
Education through ICT.

.. L22

{{{ Show the ``About the Spoken Tutorial Project'' slide }}}

.. R22

Watch the video available at the following link. It summarises the Spoken 
Tutorial project.If you do not have good bandwidth, you can download and 
watch it. 

.. L23

{{{ Show the `` Spoken Tutorial Workshops'' slide }}}

.. R23

The Spoken Tutorial Project Team conducts workshops using spoken tutorials,
gives certificates to those who pass an online test.

For more details, contact contact@spoken-tutorial.org

.. L24

{{{ Show the ``Acknowledgements'' slide }}}

.. R24

Spoken Tutorial Project is a part of the "Talk to a Teacher" project.
It is supported by the National Mission on Education through ICT, MHRD, 
Government of India. More information on this mission is available at the 
given link.

.. L25

{{{ Show the Thank you slide }}}

.. R25

Hope you have enjoyed this tutorial and found it useful.
Thank you!
