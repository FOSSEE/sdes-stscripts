.. Objectives
.. ----------
   
   .. At the end of this tutorial, you will be able to:
   
   ..   1. Change file permissions
   ..   2. Change ownership of files
  
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

Hello friends and Welcome to the tutorial on "File permissions and ownership".

.. L2

{{{ Show slide with objectives }}} 

.. R2

At the end of this tutorial, you will be able to,

 1. Change file permissions
 #. Change ownership of files

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
former tutorials as being displayed currently.

.. L4

.. R4

Let us now look at file permissions. Linux is a multi-user environment and
allows users to set permissions to their files to allow only a set of
people to read or write it. Similarly, it is not "safe" to allow system
files to be edited by any user. All this access control is possible in
Linux. 

.. R5

To start, in the root directory, say,

.. L5

{{{ Open the terminal }}}
::

    cd /
    ls -l

.. R6

You get a list of all the sub-directories, with a lot of additional information.
Let us try and understand the output.

.. L6

.. L7

{{{ Highlight the required portions accordingly while narrating }}}

.. R7

The first column denotes the type and the access permissions of the file.
The second is the number of links. The third and fourth are the owner and
group of the file. The next field is the size of the file in bytes. The
next field is the date and time of modification and the last column is the
file name.
We shall look at the permissions of the file now, ie., the first column of
the output. 

The first character in the first column specifies, whether the item is a
file or a directory. Files have a ``-`` as the first character and
directories have a ``d``. 

The rest of the 9 characters are actually sets of 3 characters each. The 
first set of 3 characters defines the permissions of the user, the next 3 
is for the group and the last three is for others. 
Based on the values of these characters, access to files is provided or denied, 
to each of the users.

So, what does each of the three characters stand for? Let's suppose, we are
looking at the set, corresponding to the permissions of the user. In the
three characters, the first character can either be an ``r`` or a ``-``.
Which means, the user can either have the permission to read the file or
not. If the character is ``r``, then the user has the permission to read
the file, else not. Similarly, ``w`` stands for write permissions and
decides whether the user is allowed to write to the file or not. ``x`` stands 
for execute permissions. You cannot execute a file, if you do not have the
permission to execute it.

Similarly, the next set of characters decides the same permissions for the
members of the group, that the file is associated with. The last set of
characters defines these permissions for the users, who are neither owners
of the file nor in the group, with which the file is associated. 

Now, it's not as if these permissions cannot be changed. If you are the
owner of a file, you can change the permissions of a file, using the
``chmod`` command.


.. R8

Let's say, we wish to give the execute permissions for a file, to both the
user and the group, how do we go about doing it? To be more explicit, given
a file ``foo.sh``, with the permissions flags as ``-rw-r--r--``, change it
to ``-rwxr-xr--``. 

The following command does it for us, 

.. L8
::

    chmod ug+x foo.sh
    ls -l foo.sh

.. R9

As you can see, the permissions have been set to the required value. But
what did we exactly do?  

.. L9

.. L10

{{{ Switch to slide,Symbolic modes }}}

.. R10

Let us understand these parameters one by one.
The ``u`` is the user who is the owner of the file. 
``g`` stands for group which consists of users who are members of the
file’s group. The reference ``o``, which we shall use later in the tutorial,    
stands for others who are users of the file but not the owners or members of 
a group.

.. L11

{{{ Switch to slide,Symbolic modes... }}}

.. R11

Let us now understand the operators. The plus operator adds the specified modes 
to the specified classes. The minus operator removes the specified modes from 
the specified classes. And finally the equal-to operator is used where modes 
specified are to be made the exact modes for the specified classes.

.. L12

{{{ Switch to slide,Symbolic modes... }}}

.. R12

We shall now learn the function of each mode. ``r`` stands for read which reads 
a  file or lists a directory’s contents. ``w`` is for write by which we can     
write to a file or a directory. ``x`` stands for execute. As the name suggests, 
it executes a file or recurse a directory tree.
   
.. L13

{{{ Switch to the terminal }}}
{{{ Highlight the command, chmod ug+x foo.sh }}}

.. R13

In the command, the parameter ``ug+x`` is the mode parameter to the
``chmod`` command. It specifies the changes to be made to the
permissions of the file ``foo.sh``. 
The ``u`` and ``g`` stand for the user and group, respectively. The ``x``
stands for the execute permission and ``+`` stands for adding the
specified permission. So, essentially, we are asking ``chmod`` command to
add the execute permission for the user and group. The permission of others
will remain unchanged. 

.. R14

So, if we wished to add the execute permission to all the users, instead of
adding it to just the user and group, we would have instead said 

.. L14
::

    chmod a+x foo.sh 

.. R15

or 

.. L15
::

    chmod ugo+x foo.sh

.. R16

Pause the video here, try out the following exercise and resume the video.

.. L16

.. L17

{{{ Show slide with exercise }}}

.. R17

Change the permissions of a directory along with all of its
sub-directories and files.

.. L18

{{{ Show slide with solution }}}

.. R18

To change the permissions of a directory along with all of its
sub-directories and files, recursively, we use the ``-R`` option
with the chmod command as shown

  chmod go-r -R <directory name>/

.. R19

It is important to note that the permissions of a file can only be changed
by a user who is the owner of a file or the superuser.
The superuser or the ``root`` user is the only user
empowered to a certain set of tasks and hence is called the superuser.
What if we wish to change the ownership of a file? The ``chown`` command is
used to change the owner and group. 
By default, the owner of a file (or directory) is the user that
created it. The group is a set of users that share the same access
permissions i.e., read, write and execute. 
For instance, to change the user and the group of the file
``wonderland.txt`` to ``alice`` and ``users``, respectively, we say,

.. L19
::

    chown alice:users wonderland.txt

.. R20

We get an error saying, the operation is not permitted.
We have attempted to change the ownership of a file that we own, to a
different user. Logically, this shouldn't be possible, because, this can
lead to problems, in a multi-user system. 
Only the superuser is allowed to change the ownership of a file from one
user to another. The command above would have worked, if you did login as 
the superuser and then changed the ownership of the file. 

.. L20

.. L21

{{{ Show Summary slide }}}

.. R21

This brings us to the end of the tutorial.In this tutorial, we have learnt to,

 1. Chane the permissions of files using the ``chmod'' command.
 #. Use the ``chown'' command to change the ownership of files.

.. L22

{{{ Show self assessment questions slide }}}

.. R22

Here are some self assessment questions for you to solve

 1. For a given file, change mode to r, w, x for all (user, group, others)
 
 2. What changes, on specifying only an owner in the "chown" command?
    
    - Only the owner of the file
    - The group ownership of the file
    - Neither the owner nor the group

.. L23

{{{ Solution of self assessment questions on slide }}}

.. R23

And the answers,

1. The required result can be obtained as,
::

    chmod ugo+rwx wonderland.txt


2. For ``chown'' command, if only  an  owner (a username or numeric user ID) 
   is given, then, that user is made the owner of each given file, and the 
   files' group is not changed.


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

