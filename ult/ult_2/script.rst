.. Objectives
.. ----------
   
   .. At the end of this tutorial, you will be able to:
   
   ..   1. Remove files and directories.
   ..   2. Copy files from one location to another.
   ..   3. Move files and directories.
   ..   4. Know the Linux File Hierarchy

.. Prerequisites
.. -------------

..   1. Getting started with Linux
 
Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on 
'Basic File handling'.

.. L2

{{{ Show slide with objectives }}} 

.. R2

At the end of this tutorial, you will be able to,

 1. Remove files and directories.
 #. Copy files from one location to another.
 #. Move files and directories.
 #. Know the Linux File Hierarchy

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with Linux".

.. R4

Let us start with the concept of basic file handling.
Let's begin with removing files.
The ``rm`` command  is used to delete files. 

Here's example to remove a file named "foo" from the directory "sdes", 

.. L4

{{{ Copy the folder /sdes to your home folder }}}
{{{ Open the terminal }}}
{{{ Navigate to /home/user/sdes/ }}}
::

    ls
    rm foo
    ls

.. R5

Note that, as such, ``rm`` works only for files and not for directories.
For instance, if you try to remove a directory named ``bar`` using, 

.. L5
::

    rm bar

.. R6

we get an error saying, cannot remove `bar`: Is a directory. But ``rm``
takes additional arguments which can be used to remove a directory and all
of it's content, including sub-directories.We use the ``-r`` option. 

.. L6
::

    rm -r bar
    ls

.. R7

It removes the directory ``bar`` and all of it's content including
sub-directories, recursively. The ``-r`` stands for recursive. 

Let's say we wish to copy a file, ``foo`` from ``sdes/linux-tools/scripts``, 
which is the source location to the target location ``sees/linux-tools``, 
how would we do it? 

.. L7
::

    pwd 
    cp linux-tools/scripts/foo linux-tools/
    ls linux-tools/

.. R8

Note, that we haven't changed the name of the file name at the target
location. We could have done that by specifying a new filename at the
target location,as,

.. L8
::

    cp linux-tools/scripts/foo linux-tools/bar
    ls linux-tools/

.. R9

A copy the file ``foo`` is created, but with the new name,
``bar``. 

But, what would have happened if we had a file named ``bar`` already at the
new location? Let's try doing the copy again, and see what happens. 

.. L9
::

    cp linux-tools/scripts/foo linux-tools/bar

.. R10

We get no error message, what happened? ``cp`` actually overwrites files.
In this case, it's not a problem since, we just re-copied the same content,
but in general it could be a problem, and we could lose data. To prevent
this, we use the ``-i`` flag with ``cp``. 

.. L10
::

    cp -i linux-tools/scripts/foo linux-tools/bar

.. R11

We are now prompted, whether the file should be over-written. To over-write
say ``y``, else say ``n``. 

Now, let's try to copy the directory ``sdes`` to a new directory called
``course``. How do we do it?

.. L11
::

    cd 
    pwd
    cp -i sdes course
   
.. R12

``cp`` refuses to copy the directory ``sdes``. We use the option ``-r``
(recursive) to copy the directory and all it's content. 

.. L12
::

    cd /home/user
    cp -ir sdes course
    ls

.. R13

We see that a new directory named course has been created with all it's 
contents.

Now, If we want to move files, instead of copying them, one way to go about
it, would be to ``cp`` the file to the new location and ``rm`` the old
file. Instead, you can make use of only one command which can do this task at 
one go. The ``mv`` command can move files or directories. It also takes 
the ``-i`` option to prompt before overwriting. 

.. L13
::

    cd /home/user
    mv -i sdes/ course/

.. R14

Let us understand what exactly happened when we used the ``mv`` command

.. L14
::

    ls course

.. R15

We can see that the ``sdes`` directory has been inserted as sub-directory
of the ``course`` directory. The move command doesn't over-write
directories, but the ``-i`` option is useful when moving files around.

A common way to rename files (or directories), is to copy a file (or a
directory) to the same location, with a new name. 

.. L15
::

    mv sdes/linux-tools sdes/linux
    ls sdes

.. R16

It renames the ``linux-tools`` directory to just ``linux``

While moving around our files and directories, we have been careful to stay
within the ``/home/`` directory, but other than that there are many other 
directories too. Let us take this opportunity to understand a few things 
about the linux file hierarchy and file permissions. 

.. L16
::

    cd /

{{{ Switch to slide, Linux File Hierarchy }}}

.. R17

The ``/`` directory is called the root directory. All the files and
directories, (even if they are on different physical devices) appear as
sub-directories of the root directory. 

.. L17

{{{ Switch to terminal }}}
::

    ls 

.. R18

You can see the various directories present at the top most level.

.. L18

{{{ Pause for sometime and then continue }}}

.. R19

For more information, it is recommended that you look at the ``man`` page
of ``hier``. 

.. L19
::

    man hier

{{{ Pause for sometime and then hit q }}}


.. L20

.. L21

{{{ Show summary slide }}}

.. R21

This brings us to the end of the tutorial.In this tutorial, we have learnt to,

 1. Remove files using ``rm`` command.
 #. Copy and move files from one location to another, using the ``cp`` 
    and ``mv`` commands respectively.
 #. Learnt the file system hierarchy of Linux.

.. L22

{{{ Show self assessment questions slide }}}

.. R22

Here are some self assessment questions for you to solve

1. How to copy all the contents of one folder into another?

2. How will you rename the file wonderland.txt to alice.txt using the 
   commands learnt so far?

.. L23

{{{ Solution of self assessment questions on slide }}}

.. R23

And the answers,

1. We use the ``cp`` command along with a star sign. The star denotes that 
   it will copy all the files of folder 1 to folder 2.
::

    cp folder1/* folder2 

2. To rename a file, we use the ``mv`` command as,
::

    mv wonderland.txt alice.txt

.. L24

{{{ Show the SDES & FOSSEE slide }}}

.. R24

Software Development techniques for Engineers and Scientists - SDES, is an 
initiative by FOSSEE. For more information, please visit the given link.

Free and Open-source Software for Science and Engineering Education - FOSSEE, is
based at IIT Bombay which is funded by MHRD as part of National Mission on 
Education through ICT.

.. L25

{{{ Show the ``About the Spoken Tutorial Project'' slide }}}

.. R25

Watch the video available at the following link. It summarises the Spoken 
Tutorial project.If you do not have good bandwidth, you can download and 
watch it. 

.. L26

{{{ Show the `` Spoken Tutorial Workshops'' slide }}}

.. R26

The Spoken Tutorial Project Team conducts workshops using spoken tutorials,
gives certificates to those who pass an online test.

For more details, contact contact@spoken-tutorial.org

.. L27

{{{ Show the ``Acknowledgements'' slide }}}

.. R27

Spoken Tutorial Project is a part of the "Talk to a Teacher" project.
It is supported by the National Mission on Education through ICT, MHRD, 
Government of India. More information on this mission is available at the 
given link.

.. L28

{{{ Show the Thankyou slide }}}

.. R28

Hope you have enjoyed this tutorial and found it useful.
Thank you!
     
