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

First let's define what Version Control is

.. L3

{{{Show the slide 'what is version control'}}}

.. R4

A way to track changes made to files over time, by keeping copies of files as we change them.

.. L4

{{{Show the slide 'Home-brewed'}}}

.. R5

Let's look at an example of home-brew Version Control system

Let's look at the various problems associated with this setup.

.. L5

{{{Show the slide 'Problems'}}}

.. R6

Now let's move onto identifying the needs for a Version Control System.

.. L6

{{{Show the slide 'The need for Version Control'}}}

.. R7

1. To err is Human...

#. By tracking the history of the project, an outsider can see the evolution of a project.

#. Allows for effective collaboration on the project as everything is shared.

#. Helps to identify which additions have broken down the project and thus aids in efficient tracking down of the bugs.

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

Let's now get into Installation

.. L8

sudo apt-get install mercurial

.. R10

For Windows, install TortoiseHg

Type 'hg' which lists out all the commands 

.. L9

$hg

.. R11

and 'hg version' which gives the version number.

.. L10

$hg version

.. R12

Now why do we need a Repo?

.. L11

{{{Show the slide for 'We need a repo!'}}}

.. R13

Let's now see how to initialize a repo

.. L12

$hg init

.. R14

Creates a fresh repository

It adds a .hg directory to our working directory. This directory keeps log of changes made henceforth.


.. L13

$hg status

.. R15

Gives the status of our repo. As a beginner, use it often.

.. L14

$hg help 'status'

.. R16

You can use 'hg help commandname' which gives the details about the command.

.. L15

{{{Show the slides for 'Status Codes'}}}

.. R17

Have a look at what various status codes associated with files means.

Let's move onto Adding Files.

.. L16

$hg status

.. R18

This shows that none of the files in the folder have not been added yet.

.. L17

$hg add

.. R19

Appends an A to the filenames.

Now let's take a snapshot of this working directory.

.. L18

$hg commit

.. R20

It remembers the changes made to the directory. The parameter -m is used to attach a commit message which gives a description of the changes committed to the repository.

.. L19

{{{Show the slide 'Thumbnail views'}}}

.. R21

hg log gives the log of the changes made in the form of changesets.

.. R22

User information is set in the hgrc file. It can be either globally or locally to the project.

.. L20

For linux systems

cat ~/.hgrc 

.. L21

{{{Show the slide 'Advice: commits, messages'}}} 

.. R23

1. Atomic changes; one change with one commit

#. Single line summary — 60 to 65 characters long

#. Followed by paragraphs of detailed description
 -  Why the change?
 - What does it effect?
 - Known bugs/issues?
 - etc.

.. L22

{{{Show the 'summary' slide'}}}

.. R23

This brings us to the end of the tutorial. In this tutorial, we have
learnt to,

.. L24

{{{Show self assessment questions slide}}}

.. R24

Here are some self assessment questions for you to solve

.. L25

{{{Show the solutions slide to self assessment questions }}}

.. R25

And the answers,


.. L26

{{{Show the thank you slide}}}

.. R26

Hope you have enjoyed this tutorial and found it useful.
Thank you

