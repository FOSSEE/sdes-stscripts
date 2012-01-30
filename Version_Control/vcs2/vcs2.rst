---------------------------------
Version Control using Hg  Part 2
---------------------------------

.. Prerequisites
.. -------------

.. Version Control using Hg Part 1

.. Author : Primal Pappachan
   Internal Reviewer : Kiran Isukapatla
   Date: Jan 27, 2012

----------------------
Spoken Tutorial Script
----------------------

.. L1

{{{ Show the first slide containing title, name of the production team along
with the logo of MHRD}}}

.. R1

Hello friends and welcome to the second part of tutorial on 'Version Control
using Hg' 

.. L2

{{{Show the slide 'Prerequisite'}}}

.. R2

Please make sure that you have gone through the following tutorials before you
continue on this tutorial:

.. L3

{{{Show the slide 'Objectives'}}}

.. R3

At the end of this tutorial you will be able to
 1. initialize a new repository,
 #. obtain the status of a repository,
 #. add new files to a repository,
 #. take snapshots of a repository,
 #. view the history of a repository,
 #. and set your user information for hg 

.. L4

{{{Show the slide for 'We need a repo!'}}}

.. R4

To start using Mercurial (or hg) and get the benefits of using a version
control system, we should first have a repository. 

Now, what exactly is a repo? A repo/repository is a folder with contains all
the files and information on all the changes that were made to it. To save disk
space, hg doesn't save all files, but only saves only a series of changes made
to the files.

.. L5

{{{Show the slide 'Initializing a Repo'}}}

.. R5

A repository can either be started using an init command or an existing
repository could be cloned. Let us look at creating our own repository, now. We
can look at obtaining already existing repositories, at a later stage.

Let's say we have a folder called book, which has all the chapters of a book as
text files. Let us convert that folder, into a hg repository.

.. L6

$ cd book/
$ ls -a
. .. chapter1.txt chapter2.txt chapter3.txt

.. R6

We have three chapters in the folder. We convert this folder into a mercurial
repository using the hg init command

.. L7

$ hg init
$ ls -a
. .. .hg chapter1.txt chapter2.txt chapter3.txt

.. R7

The .hg directory indicates that our book directory is now a hg repository.
Mercurial keeps all the history of the changes made, and a few other config
files, etc. in this directory. The directory, book is called our working
directory.

.. L8

{{{Show the slides 'Status Report'}}}

.. R8

We now have a fresh repository, but all our files are not being tracked or
watched by mercurial, yet. We need to explicitly ask it to watch the files,
that we want it to.

.. L9

$hg status

.. R9

Gives the status of our repo. As a beginner, use it often.

.. L10

$hg help 'status'

.. R10

You can use 'hg help commandname' which gives the details about the command.
For example.

.. L11

$hg help status

.. L12

{{{Show the slides for 'Status Codes'}}}

.. R11

Let's now to try to discern what each of the status code associated with the
files mean. By looking at the codes, it is clear that our files are not being
tracked by hg yet. Now let's move onto 'Adding Files'.

.. L13

$hg add

.. R12

This simply adds all the files in the (working) directory, to the repository.
As expected, the status command shows an A before he file names. We could also
specify files individually, for example

.. L14

$ hg add chapter1.txt

.. R13

If you have deleted files, hg status will show you the status code !. You can,
then, tell hg to stop tracking these files, using the hg remove command. Look
at hg help remove for more details.

.. L15

{{{Show the slides 'Taking Snapshots'}}}

.. R14

We have added a set of new files to the repository, but we haven't told
mercurial to remember these changes, i.e., to take a snapshot at this point in
time. We do this by using the commit command.

.. L16

$ hg commit -u "Primal Pappachan <primal@fossee.in>" -m "Initial Commit."

.. R15

The -u parameter allows us to specify the user details. It is a general good
practice to use full name followed by the email id. The -m parameter allows us
to give the commit message --- a message describing the changes that are being
committed.

Mercurial has now taken a snapshot of our repository and has attached our
description along with it. To see the status of the files in the repository,
use the hg status command.

.. L17

$ hg st

.. R16

The command does not return anything, when there are no uncommitted changes.
Also, notice that I have started getting lazy and used only a short name st for
the status command.

.. L18

{{{Show the slide 'Thumbnail views'}}}

.. R17

To see the history of the changes to our repository, we use hg log. We can view
the change that we just made to our repository.

.. L19

$ hg log

.. R18

hg log gives the log of the changes made in the form of changesets. A changeset
is a set of changes made to the repository between two consecutive commits. It
also shows the date at which the commit was made. Please have a look of the
various aspects of the changeset.

.. L20

{{{Show the slide 'User Information'}}}

.. R19

There are two aspects which can be improved upon. Firstly, it is unnecessary to
keep typing the user information each and every time we make a commit.
Secondly, it is not very convenient to enter a multi-line commit message from
the terminal. To solve these problems, we set our user details and editor
preferences in the .hgrc file in our home folder. ($HOME/.hgrc on Unix like
systems and %USERPROFILE%\.hgrc on Windows systems) This is a global setting
for all the projects that we are working on. 


For linux systems, we open the configuration file in our favorite editor and
add the username details and our editor preferences.

.. L21


vim ~/.hgrc 
[ui]
username = Primal Pappachan <primal@fossee.in>
editor = vim

.. R21

We have now set the user-name details for mercurial to use.

.. L22

{{{Show the slide 'Advice: commits, messages'}}} 

.. R22

Some Recommended Practices for commit messages

1. Atomic changes; one change with one commit

#. Single line summary — 60 to 65 characters long

#. Followed by paragraphs of detailed description
 -  Why the change?
 - What does it effect?
 - Known bugs/issues?
 - etc.

.. L23

{{{Show the 'summary' slide'}}}

.. R23

This brings us to the end of the tutorial. In this tutorial, we have
seen,
 1. how to initialize a new repository using hg init,
 #. get the status of a repository using hg status and meaning of it's status
 codes
 #. make commits of changes to files, using hg commit 
 #. view the history of the repository using the hg log command,
 #. set our user information in the global hgrc file.

.. L24

{{{Show self assessment questions slide}}}

.. R24 

Here are some self assessment questions for you to solve

 1. How can you tell hg to stop tracking deleted files?
 #. Here's a part of the output that is printed in 'hg log'.
	changeset:   1:2278160e78d4
	tag:         tip
	user:        Primal Pappachan <primal@fossee.in>
	date:        Sat Jan 26 22:16:53 2012 +0530
	summary:     Added Readme
 Try to identify each component of this changeset and it's meaning. In the
 changeset, what is the significance of the number as well as hexadecimal
 string?

 #. What happens when 'hg commit' command is run first time without specifying
 username as parameter or creating the hg configuration file? 
 
.. L25

{{{Show the solutions slide to self assessment questions }}}

.. R25

And the answers,

 1. If you have deleted files, hg status will show you the status code !. You
 can, then, tell hg to stop tracking these files, using the hg remove command.
 #. The revision number is a handy notation that is only valid in that
 repository. The hexadecimal string is the permanent, unchanging identifier
 that will always identify that exact changeset in every copy of the repository
 
 #. If you have set the EMAIL environment variable, this will be used. Next,
 Mercurial will query your system to find out your local user name and host
 name, and construct a username from these components. Since this often results
 in a username that is not very useful, it will print a warning if it has to do
 this. If all of these mechanisms fail, Mercurial will fail, printing an error
 message. In this case, it will not let you commit until you set up a
 username.

.. L26

{{{Show the thank you slide}}}

.. R26

Hope you have enjoyed this tutorial and found it useful. Feel free to play
around with Mercurial and read the documentation given by hg help command. When
you are ready to move on, please proceed to the third tutorial on 'Version
Control using Hg'

Thank you

