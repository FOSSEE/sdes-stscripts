.. Objectives
.. ----------
   
   .. At the end of this tutorial, you will be able to:
   
   ..   1. Display the contents of files.
   ..   2. Read only parts of a file.
   ..   3. Look at the statistical information of a file.

.. Prerequisites
.. -------------

..   1. Getting started with Linux
..   2. Basic File Handling
..   3. File permissions and ownership

 
Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on 
'Advanced File Handling'.

.. L2

{{{ Show slide with objectives }}} 

.. R2

At the end of this tutorial, you will be able to,

 1. Display the contents of files.
 #. Read only parts of a file.
 #. Look at the statistical information of a file.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
former tutorials as being displayed currently.

.. R4

Let us begin with how to read a file as a whole.
The ``cat`` command is the most commonly used command for this purpose.
To view the contents of a file, say, ``foo.txt``, we
simply say, 

.. L4

{{{ Switch to terminal }}}
::

    cat foo.txt

.. R5

You can see the contents of the file on the terminal. 

The cat command could also be used to concatenate the text of multiple
files. Say, we have two files,``foo.txt`` and ``bar.txt``, 

.. L5
::

    cat foo.txt bar.txt

.. R6

It shows the output of both the files concatenated on the standard output. 
But if we had a long file,the output of ``cat`` command is not convenient 
to read.
Let's look at the ``less`` command which turns out to be more useful in 
such a case. 

``less `` allows you to view the contents of a text file one screen at a
time. 

.. L6
::

    less wonderland.txt

<Press enter few times and show the contents of the file, then press Ctrl-z>

.. R7

This shows us the file, one screen at a time.

.. L7

.. L8

{{{ Show slide with, less }}}

.. R8

``less`` has a list of commands that it allows you to use, once you have
started viewing a file. A few of the common ones have been listed below. 

    * q: to Quit.

    * [Arrows]/[Page Up]/[Page Down]/[Home]/[End]:to Navigate through 
      the content.

    * ng: to jump to a given line number (n).Default, is the first line of 
      a file.

    * /pattern: Search for pattern. Regular expressions can be used.

    * h: for Help. 

.. R9

Let us move ahead with the topic. Often, we would like to get only some 
statistical information about a file, rather than it's full contents. 
The ``wc`` command prints these details for a file. 

.. L9
::

    wc wonderland.txt

.. L10

{{{ Highlight the required portions accordingly while narrating }}}

.. R10

As you can see, we get some information about the file.
The first number is the number of lines, the second is the number of words
and the third is the number of characters in the file. 

.. R11

Let us now look at a couple of commands that let's you see parts of files,
instead of the whole file. The ``head`` and ``tail`` commands allow you to see 
parts of files. As their names suggest, they display the start and end of a 
file, respectively.

.. L11
::

    head wonderland.txt

.. R12

It prints only the first 10 lines of the file. Similarly tail will print the
last 10 lines of the file. If we wish to change the number of lines that we
wish to view, we use the option ``-n``. 

.. L12
::

    head -n 1 wonderland.txt

.. R13

It prints only the first line of the file. Similarly, we could print only
the last line of the file.

The most common use of the tail command is to monitor a continuously
changing file, for instance, a log file. Say, you have a process running,
which is continuously logging it's information to a file, for instance, the
logs of the system messages. 

.. L13
::

    tail -f /var/log/dmesg

.. R14

This will show the last 10 lines of the file as expected, but along with
that, it starts monitoring the file. Any new lines added at the end of the
file, will be shown. To interrupt tail, while it is monitoring, hit
``Ctrl-C``. 

We looked at a couple of functions that allowed us to view a part of a file,
line-wise. We shall now look at a couple of commands that will allow us to look
at, only certain sections of each line of a file and merge those parts.
Let's take the ``/etc/passwd`` file as our example file. It contains
information about each user of the system.

.. L14
::

    cat /etc/passwd

.. R15

In the output, let us look at only the first, fifth, sixth and the last 
columns.The first column is the ``user name``, the fifth column is the 
``user info``, the sixth column is the ``home folder`` and the last column 
is the ``path of the shell program`` that the user uses. 
Let's say, we wish to look at only the user names in the file, how do we do it?

.. L15
::
    
    cut -d : -f 1 /etc/passwd

.. R16

It gives us the required output. Let us understand this operation in detail.
The first option ``-d`` specifies the delimiter between the various fields in
the file, in this case it is the ``semicolon``. If no delimiter is specified,
the TAB character is assumed to be the delimiter. The ``-f`` option specifies,
the field number that we wish to choose. 
You can print multiple fields, by separating the field numbers with a
comma. 

Pause the video here, try out the following exercise and resume the video.

.. L16

.. L17

{{{ Show slide with exercise }}}

.. R17

Print only the first, fifth and the seventh fields of the file ``/etc/passwd``.

.. R18

Switch to the terminal for solution

.. L18

{{{ continue from paused state }}}
{{{ Switch to the terminal }}}

::
    
    cut -d : -f 1,5,7 /etc/passwd

.. R19

We get the correct output.
Instead of choosing by fields, ``cut`` also allows us to choose on the
basis of characters or bytes. For instance, we could get the first 4
characters of all the entries of the file, ``/etc/passwd`` by saying,

.. L19
::

    cut -c 1-4 /etc/passwd 

.. R20

The end limits of the ranges can take sensible default values, if they are
left out. For example, 

.. L20
::

    cut -c -4 /etc/passwd 

.. R21

It gives the same output as before. If the start position has not been
specified, it is assumed to be the start of the line. Similarly if the end
position is not specified, it is assumed to be the end of the line. 

.. L21
::

    cut -c 10- /etc/passwd 

.. R22

It prints all the characters from the 10th character up to the end of the
line. 
Let us now solve an inverse problem. Let's say we have two columns of data
in two different files, and we wish to view them side by side. 

.. L22

.. L23

{{{ Show slide with, paste }}}

.. R23

For instance, consider a file 'students.txt' containing the names of students 
and another file 'marks.txt' containing their respective marks.

.. R24

we wish to view the contents, side by side. The ``paste`` command allows 
us to do that. 

.. L24
::

    paste students.txt marks.txt
    paste -s students.txt marks.txt

.. R25

The first command gives us the output of the two files, next to each other
and the second command gives us the output one below the other. 

Now, this problem is a bit unrealistic because, we wouldn't have the marks
of students in a file, without any information about the student to which
they belong. Let's say our marks file had the first column as the roll
number of the student, followed by the marks of the students. What would we
do then, to get the same output that we got before? 

Essentially we need to use both the ``cut`` and ``paste`` commands, but
how do we do that? That brings us to the concept of Redirection and Piping
which is covered in the next spoken tutorial. 

.. L25

.. L26

{{{ Switch to summary slide }}}

.. R26

This brings us to the end of this tutorial.
In this tutorial, we have learnt to, 

 1. Display the contents of files using the ``cat`` command.
 #. View the contents of a file one screen at a time using the 
    ``less`` command.

.. L27

{{{ Switch to slide Summary... }}}

.. R27

 1. Display only specific contents of file using the ``head`` and 
    ``tail`` commands.
 #. Use the ``cut``, ``paste`` and ``wc`` commands.
  

.. L28

{{{ Show self assessment questions slide }}}

.. R28

Here are some self assessment questions for you to solve

1. How to view lines from 1 to 15 in ``wonderland.txt``?

2. In ``cut`` command, how to specify space as the delimiter? 

.. L29

{{{ Solution of self assessment questions on slide }}}

.. R29

And the answers,

1. We can use the head command as,
::

    head -15 wonderland.txt

2. We use the -d option with the command as,
::

    cut -d " " <filename>

.. L30

{{{ Show the SDES & FOSSEE slide }}}

.. R30

Software Development techniques for Engineers and Scientists - SDES, is an 
initiative by FOSSEE. For more information, please visit the given link.

Free and Open-source Software for Science and Engineering Education - FOSSEE, is
based at IIT Bombay which is funded by MHRD as part of National Mission on 
Education through ICT.

.. L31

{{{ Show the ``About the Spoken Tutorial Project'' slide }}}

.. R31

Watch the video available at the following link. It summarises the Spoken 
Tutorial project.If you do not have good bandwidth, you can download and 
watch it. 

.. L32

{{{ Show the `` Spoken Tutorial Workshops'' slide }}}

.. R32

The Spoken Tutorial Project Team conducts workshops using spoken tutorials,
gives certificates to those who pass an online test.

For more details, contact contact@spoken-tutorial.org

.. L33

{{{ Show the ``Acknowledgements'' slide }}}

.. R33

Spoken Tutorial Project is a part of the "Talk to a Teacher" project.
It is supported by the National Mission on Education through ICT, MHRD, 
Government of India. More information on this mission is available at the 
given link.

.. L34

{{{ Show the Thank you slide }}}

.. R34

Hope you have enjoyed this tutorial and found it useful.
Thank you!

