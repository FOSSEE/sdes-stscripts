.. Prerequisites
.. -------------

.. None

.. Author : Primal Pappachan
   Internal Reviewer : Kiran Isukapatla
   Date: May 10 2012

--------
Script
--------

.. L1

{{{ Show the first slide containing title, name of the production team along 
with the logo of MHRD}}}

.. R1

Hello friends and welcome to the tutorial on 'Version Control with Hg'

.. L2

{{{Show the slide containing the objectives}}}

.. R2

At the end of this tutorial you will be able to

1. Understand what is Version Control.

#. Identify the need for using Version Control.

#. Install Mercurial.

.. L3

{{{Show the slide 'what is version control'}}}


.. R3

First, let's understand what 'Version Control' is. 

'Version control' is a way to track files over time and share them. 
This allows access to earlier versions of a file(s) if and when required. 
It therefore enables us to make changes to the content of a file, view it's 
change log and collaborate on a single piece of work with a team of people.
 
.. L4

{{{Show the slide 'Home-brewed'}}}

.. R4

Lets look at an example of home-brewed Version Control system.Version control 
is a way of backing up files, before making changes. Most people would have 
cooked up their own version control system. But there are more general purpose 
tools which can do this task in an organized way.

.. L5

{{{Show the slide 'Problems'}}}

.. R5

Let's look at the various problems associated with this set-up.

1. Name and changes made are not related or linked.

#. Cant track sequence of changes made to a file.

#. Does not scale.


.. L6

{{{Show the slide 'The need for Version Control'}}}

.. R6

Now, let's move to identifying the needs for a 'Version Control System'.

We have seen that one of the main motivations to use a Version Control system 
is the ability to go back to a working version of a file, when something 
goes wrong. Below are a few more advantages of using an automated version 
control system.

1. By tracking the history of a project, any person may see the evolution 
 of a project.

2. Allows for effective collaboration on a project, as everything is shared.

3. Helps to identify which additions have broken down a project and thus 
 aids in efficient tracking down of the bugs.

4. It is good for a one man show as it is for a big group of people working 
 on a project.


.. L7

{{{Show the slide 'How does it work? - Analogy}}}

.. R7

It is, in some ways, similar to playing a video game. We generally play games 
in stages. While playing, we save the game at some instances as per our choice. 
We continue playing, but we could, if necessary, choose to go back to one of the
saved states and start over. In this manner, we could change the state of 
the game.

.. L8

{{{Show the slide 'Mercurial or hg'}}}

.. R8

mercurial or hg is:

1. Easy to learn and use
    
#. Lightweight

#. Scales excellently

#. Written in Python


Some of the Version Control tools available and used widely are: cvs, svn, 
git and so on.

Each of these tools have their own merits and demerits. In this tutorial we 
shall learn how to use mercurial or hg.

.. L9

{{{Show the slide 'Installation'}}}

.. R9

Let's now get into Installation

.. L10

sudo apt-get install mercurial

.. R10

Type sudo apt-get install mercurial

Type hg  

.. L11

$hg

.. R11

It will give you the list of basic commands.

.. L12

$hg version

.. R12

and 'hg version' gives the version number of mercurial you are presently using.

.. L13

{{{Show the 'summary' slide'}}}

.. R13

This brings us to the end of the tutorial. In this tutorial, we have
learnt:

1. What is Version Control.

#. Identify the need for using Version Control

#. Install Mercurial.

.. L14

{{{Show self assessment questions slide}}}

.. R14

Here are some self assessment questions for you to solve

1. Is Mercurial a Centralized VCS or Distributed Version Control System? 

#. How can you verify whether Mercurial has been installed properly?

#. What is the command for accessing built-in help system of Mercurial?

.. L15

{{{Show the solutions slide to self assessment questions }}}

.. R15

And the answers,

1. Mercurial is a Distributed Version Control system.

#. hg version

#. hg help command


.. L16

{{{Show the thank you slide}}}

.. R16

Hope you have enjoyed this tutorial and found it useful.
Thank you

