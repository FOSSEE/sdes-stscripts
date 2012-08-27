.. Objectives
.. ----------
   
   .. At the end of this tutorial, you will be able to:
   
   ..   1. Sort lines of text files
   ..   2. Print lines matching a pattern
   ..   3. Translate or delete characters
   ..   4. Omit repeated lines


.. Prerequisites
.. -------------

..   1. Getting started with Linux
..   2. Redirection and Piping


 
Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on 'Text Processing'.

.. L2

{{{ Show slide with objectives }}} 

.. R2

At the end of this tutorial, you will be able to,

 1. Sort lines of text files
 #. Print lines matching a pattern
 #. Translate or delete characters
 #. Omit repeated lines.


.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
previous tutorials as being displayed currently.

.. R4

In this tutorial, we shall learn about text processing.
TO begin with, consider data kept in two files, namely ``marks1.txt`` and 
``students.txt``.
Let us see what data they contain. Open a terminal and type, 

.. L4

{{{ Open the terminal }}}
::

    cat marks1.txt
    cat students.txt

.. R5

Let's say we wish to sort the output in the alphabetical order
of the names of students. We can use the ``sort`` command for this
purpose.

We just pipe the previous output to the ``sort`` command as,

.. L5
::

    cut -d " " -f 2- marks1.txt | paste -d " " students.txt -| sort

.. R6

Let's say we wish to sort the names, based on the marks in the first
subject i.e. the first column after the name. ``sort`` command also allows us to
specify the delimiter between the fields and sort the data on a particular
field. ``-t`` option is used to specify the delimiter and ``-k`` option
is used to specify the field. 

.. L6
::

    cut -d " " -f 2- marks1.txt | paste -d " " students.txt -| sort -t " " -k 2

.. L7

{{{ Show slide with, Sort... }}}

.. R7

This command give us a sorted output as required. But, what if we would 
like the output to appear in the reverse order. ``-r`` option allows the output
to be sorted in the reverse order and the ``-n`` option is used to choose 
a numerical sorting. 

.. R8

Let us do it on the terminal and see for ourselves, 

.. L8

{{{ Switch to the terminal }}}
::

    cut -d " " -f 2- marks1.txt | paste -d " " students.txt -| 
    sort -t " " -k 2 -rn

.. R9

Suppose, While you are compiling the students marklist, Anne walks up to you and
wants to know her marks. You, being a kind person that you are, oblige.
But you do not wish her to see the marks that others have scored. What
do you do? Here, the ``grep`` command comes to your rescue. 

``grep`` is a command line text search utility. You can use it to search
for Anne and show her, what she scored. ``grep`` allows us to search for a
search string in files. But we could, like any other command, pipe the
output of other commands to it. So, we shall use the previous combination
of ``cut and paste`` that we had, to get the marks of students along with their
names and search for Anne in that. 

.. L9
::

    cut -d " " -f 2- marks1.txt | paste -d " " students.txt - | grep Anne 

.. R10

This will give us only the line containing the word Anne as the output.
The ``grep`` command is by default case-sensitive. So, we wouldn't have got
the result if we had searched for anne, with a small a, instead of 
Anne, with a capital a. But, what if we didn't know, whether the name was 
capitalized or not? ``grep`` allows you to do case-insensitive searches 
by using the ``-i`` option. 

.. L10
::

    cut -d " " -f 2- marks1.txt | paste -d " " students.txt - | grep -i Anne 

.. R11

Now, in another scenario, if we wished to print all the lines, which do
not contain the word Anne, we could use the ``-v`` option. 

.. L11
::

    cut -d " " -f 2- marks1.txt | paste -d " " students.txt - | grep -iv Anne

.. R12

``grep`` allows us to do more complex searches. For instance, searching for
sentences starting or ending with a particular pattern and regular
expression based searches. 

.. L12

{{{ Show slide with, tr }}}

.. R12

``tr`` is a command that takes two sets of characters as parameters, and
replaces occurrences of the characters in the first set with the
corresponding elements from the other set. It reads from the standard
input and writes to the standard output. 

.. R13

For instance, if we wish to replace all the lower case letters in the
students file with upper case, we can do it as, 

.. L13

{{{ Switch to the terminal }}}
::

    cat students.txt | tr a-z A-Z

.. R14

A common task is to remove empty newlines from a file. The ``-s`` flag
causes ``tr`` to compress sequences of identical adjacent characters in its
output to a single token. For example,

.. L14
::

    tr -s '\n' '\n'

.. R15

Hit enter 2-3 times and see that every time we hit enter we get a newline.

.. L15
::

    <Enter>
    <Enter> 

.. R16

It replaces sequences of one or more newline characters with a single newline.

The ``-d`` flag causes ``tr`` to delete all tokens of the specified set of
characters from its input. In this case, only a single character set
argument is used. The following command removes carriage return characters,
thereby converting a file in DOS/Windows format to the Unix format. 

.. L16
::

    cat foo.txt | tr -d '\r' > bar.txt

.. R17

The ``-c`` flag complements the first set of characters.

.. L17
::

    tr -cd '[:alnum:]' 

.. R18

It therefore removes all non-alphanumeric characters.

Let us consider one more scenario.Suppose we have a list of items, say books, 
and we wish to obtain a list of names of all the books only once, without 
any duplicates. To achieve this, we use the ``uniq`` command. Let us first 
have a look at our file

.. L18
::

    cat items.txt

.. R19

Now, let us try and get rid of the duplicate lines from this file using 
the ``uniq`` command.

.. L19
::

    uniq items.txt

.. R20

Nothing happens! Why? The ``uniq`` command removes duplicate lines only when 
they are next to each other. So, henceforth, we get a sorted file from the 
original file and work with that file. 

.. L20
::

    sort items.txt > items-sorted.txt

.. R21

Now, the ``uniq`` command will work. Let's try it out

.. L21

::

    uniq items-sorted.txt

.. R22

The same result can also be obtained by a more precise command. We include the 
option ``-u`` which gives the lines which are unique and do not have any 
duplicates in the file

.. L22 
::

    uniq -u items-sorted.txt 

.. R23

``uniq -d`` outputs only those lines which have duplicates. 
The ``-c`` option displays the number of times each line occurs in the file.

.. L23
::

    uniq -dc items-sorted.txt

.. L24

{{{ Show summary slide }}}

.. R24

This brings us to the end of the end of this tutorial.
In this tutorial, we have learnt to, 
 
1. Use the ``sort`` command to sort lines of text files.
#. Use the ``grep`` command to search text pattern.

.. L25

{{{ Show summary slide.. }}}

.. R25

#. Use the ``tr`` command to translate and/or delete characters.
#. Use the ``uniq`` command to omit repeated lines in a text. 

.. L26

{{{ Show self assessment questions slide }}}

.. R26

Here are some self assessment questions for you to solve

1. To obtain a one-per-line pattern, which command is used?
   
    - grep -f
    - grep -i
    - grep -v
    - grep -e

.. L27

{{{ Show self assessment questions slide.. }}}

.. R27

2. Translate the word 'linux' to upper-case.

3. Sort the output of ``ls -al`` command, numerically and by filesize in 
   ascending order. 

.. L28

{{{ Solution of self assessment questions on slide }}}

.. R28

And the answers,

1. In order to obtain patterns one per line, we use the ``grep`` command
   alongwith the -f option.

2. We use the tr command to change the word into uppercase 
::

    echo 'linux' | tr a-z A-Z
 

3. We use the sort command as, 
::
     
    ls -al | sort -n -k5
The -n  means "sort numerically", and the -k5 option means to key off of 
column five. 

.. L29

{{{ Show the SDES & FOSSEE slide }}}

.. R29

Software Development techniques for Engineers and Scientists - SDES, is an 
initiative by FOSSEE. For more information, please visit the given link.

Free and Open-source Software for Science and Engineering Education - FOSSEE, is
based at IIT Bombay which is funded by MHRD as part of National Mission on 
Education through ICT.

.. L30

{{{ Show the ``About the Spoken Tutorial Project'' slide }}}

.. R30

Watch the video available at the following link. It summarises the Spoken 
Tutorial project.If you do not have good bandwidth, you can download and 
watch it. 

.. L31

{{{ Show the `` Spoken Tutorial Workshops'' slide }}}

.. R31

The Spoken Tutorial Project Team conducts workshops using spoken tutorials,
gives certificates to those who pass an online test.

For more details, contact contact@spoken-tutorial.org

.. L32

{{{ Show the ``Acknowledgements'' slide }}}

.. R32

Spoken Tutorial Project is a part of the "Talk to a Teacher" project.
It is supported by the National Mission on Education through ICT, MHRD, 
Government of India. More information on this mission is available at the 
given link.

.. L33

{{{ Show the Thank you slide }}}

.. R33

Hope you have enjoyed this tutorial and found it useful.
Thank you!
