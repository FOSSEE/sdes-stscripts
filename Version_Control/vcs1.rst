
.. Prerequisites
.. -------------

.. None

.. Author : Primal Pappachan
   Internal Reviewer :
  


--------
Script
--------

.. L1

{{{ Show the first slide containing title, name of the production team along with the logo of MHRD}}}

.. R1

Hello friends and welcome to the tutorial on 'Version Control with Hg' 

.. L2

{{{Show the slide containing the objectives}}}

.. R2

At the end of this tutorial you will be able to

1. Understand what is Version Control and the need for it.

#. Create and use repository on a daily basis

.. R3

First let's understand what Version Control is

.. L3

{{{Show the slide 'what is version control'}}}

.. R4

Version control is just a way to track your files over time and share them. This allows you to go back to older versions when something goes wrong, see what changed when and why, collaborate on a single piece of work with a bunch of people.

Version control is just a way of backing up your files, before making changes to it. Most people would have cooked up their own version control system, without realizing there are tools built by others which takes the task much more organized and systematic.  

.. L4

{{{Show the slide 'Home-brewed'}}}

.. R5

Let's look at an example of home-brew Version Control system

Version control is just a way of backing up your files, before making changes to it. Most people would have cooked up their own version control system, without realizing there are tools built by others which takes the task much more organized and systematic.  

.. L5

{{{Show the slide 'Problems'}}}

Let's look at the various problems associated with this setup.

.. R6

Now let's move onto identifying the needs for a Version Control System.

.. L6

{{{Show the slide 'The need for Version Control'}}}

.. R7

1. To err is Human...

#. By tracking the history of the project, an outsider can see the evolution of a project.

#. Allows for effective collaboration on the project as everything is shared.

#. Helps to identify which additions have broken down the project and thus aids in efficient tracking down of the bugs.

#. It is good for a one man show as it is for a big group of people working on a project.

.. R8

It is similar to playing an Video game.

1. We play games ins stages

#. Once we finish a stage or a task - we SAVE

#. We continue playing

#. But, if necessary, we could choose from one of the saved states and start from there

#. We could alter the course of the game

.. L7

{{{Show the slide 'Mercurial or hg'}}}

.. R9

Some of the Version Control tool available and used widely are:

1. cvs(Concurrent Version Systems)

#. svn(subversion)

#. hg(mercurial)

#. git

.. R10

Each of these tools have their own merits and demerits. In this tutorial we will be learning to use mercurial or hg.

Let's now get into Installation

.. L8

sudo apt-get install mercurial

.. R11

For Windows,

.. L9

http://mercurial.selenic.com/downloads/

Type 'hg' which lists out all the commands 

.. L10

$hg

.. R12

and 'hg version' which gives the version number.

.. L11

$hg version

.. R13

Now why exactly is a repo? A repp/repository is a folder with all your files and a store of all the changes that were made to it. To save disk space, hg doesn't save all files, but only saves only a series of changes made to the files.

.. L13

{{{Show the slide for 'We need a repo!'}}}

.. R14

Let's now see how to initialize a repo

.. L14

cd working-directory/

$hg init

ls -a

.. R15

The .hg directory indicates that our book directory is now a hg repository. Mercurial keeps all the history of the changes made and a few other config files etc. in this directory.

.. L13

$hg status

.. R15

Gives the status of our repo. As a beginner, use it often.

.. L14

$hg help 'status'

.. R16

You can use 'hg help commandname' which gives the details about the command. For example.

.. L15

hg help status

{{{Show the slides for 'Status Codes'}}}

.. R17

Have a look at what various status codes associated with files means. By looking at the codes, it is clear that our files are not yet being tracked by hg. Now Let's move onto Adding Files.

.. L16

$hg status

.. R18

This shows that none of the files in the folder have not been added yet.

.. L17

$hg add

.. R19

This simply adds all the files in the (working) directory, to the repository, As expected, the status command shows an A has been appeneded to the filenames. We could also specify files individually, for example

.. L18

$ hg add filename

.. R20

We have added a set of files to the repository, but we haven't told mercurial to remember these changes. Now let's take a snapshot of this working directory. This can be done by using commit command.

.. L19

$hg commit -u "Primal Papppachan <primal007@gmail.com>" -m "Initial Commit."

.. R20

The -u parameter allows to specify the user details. The parameter -m is used to attach a commit message which gives a description of the changes committed to the repository. Check the status of repository by typing

.. L20

$ hg st

.. R21

To see the history of changes made to our repository, we use hg log. We can view the change that we just made to our repoistory.

.. L21

{{{Show the slide 'Thumbnail views'}}}

.. R21

hg log gives the log of the changes made in the form of changesets. A changeset is a set of changes made to the repository between two consecutive commits. It also shows the date at which the commit was made.


.. R22

User information is set in the hgrc file. It can be either globally or locally to the project.

.. L23

For linux systems

cat ~8.hgrc 
[ui]
username = Primal Pappachan <primal007@gmail.com>
editor = vim


.. R23


We have now set the username details for mercurial to use.

.. L24

{{{Show the slide 'Advice: commits, messages'}}} 

.. R24

1. Atomic changes; one change with one commit

#. Single line summary — 60 to 65 characters long

#. Followed by paragraphs of detailed description
   -  Why the change?
   - What does it effect?
   - Known bugs/issues?
   - etc.

.. L25

{{{Show the 'summary' slide'}}}

.. R25

This brings us to the end of the tutorial. In this tutorial, we have
learnt to,

.. L26

{{{Show self assessment questions slide}}}

.. R26

Here are some self assessment questions for you to solve

.. L27

{{{Show the solutions slide to self assessment questions }}}

.. R27

And the answers,


.. L27

{{{Show the thank you slide}}}

.. R28

Hope you have enjoyed this tutorial and found it useful.
Thank you

