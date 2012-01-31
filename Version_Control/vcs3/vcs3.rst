
---------------------------------
Version Control using Hg  Part 3
---------------------------------

.. Prerequisites
.. -------------

.. Version Control with hg - Part 1,2

.. Author : Primal Pappachan
   Internal Reviewer :
   Date: Jan 27, 2012
   
   
--------
Script
--------

.. L1

*{{{ Show the first slide containing title, name of the production team along
with the logo of MHRD}}}*

.. R1

Hello friends and welcome to the tutorial on 'Version Control with Hg' 

.. L2

*{{{Show the slide 'Prerequisite'}}}*

.. R2

Please make sure that you have gone through the following tutorials before you
continue on this tutorial

.. L3

*{{{Show the slide containing the objectives}}}*

.. R3

At the end of this tutorial you will be able to

1. Learn how to view and revert changes made to files in a repository.

#. Learn how to share repositories and deal with simultaneous conflicting changes.

.. L4

*{{{Show the slide 'Operational overhead?'}}}*

.. R4 

Let's first try to find out why we should commit inspite of the additional
operational costs and loss of time?

.. L4

*{{{Show the slide 'Revert Changes'}}}*

.. R4

While you were wondering, let's say your friend walks in and together you make
a lot of changes. 1. You replace all the occurrences of & in chapter1.txt with
and. 2. You delete the chapter3.txt file.

.. L5 

``$ rm chapter3.txt``

``$ hg st``

``M chapter1.txt``

``! chapter3.txt``

.. R6

But after a while, you realize that these changes are unwarranted. You want to
go back to the previous state, undoing all the changes that you made, after
your friend arrived.

The undo in your editor may allow undoing some changes(if you haven't closed it
after making the changes) but there's no way of getting back deleted files
using your editor. That's where mercurial comes to the rescue.

We shall use the revert command of hg to undo all the changes after the last
commit. If we want to undo all the changes, we use the revert command with the
--all argument, else use revert command with specific filename as argument.

.. L5

``$ hg revert --all``

``reverting chapter1.txt``

``reverting chapter3.txt``

``$ hg st``

``? chapter1.txt.orig``

``$ ls``

``chapter1.txt  chapter1.txt.orig  chapter2.txt  chapter3.txt``

.. R5

After running this command, you can see that all deleted files have been
restored. But hg has generated new files with .orig extension.  Mercurial
actually doesn't like  to delete any of the changes that you have made. So, it
makes a back-up of the already existing files in the present state and gives
you back the old file.

If we now decide, that we want to redo the changes that we had done to the
existing file, we can just overwrite it with the backed up file. 

.. L6

``$ mv chapter1.txt.orig chapter1.txt``

``$ hg st``

``M chapter1.txt``

.. L7

``{{{Show the slide 'Viewing Changes'}}}``

.. R6

Let's say we now want to commit these changes, but we are not sure of all the
changes that we have made to the file, since it's been a while after we made
the changes. We could use the diff command to see all the changes that have
been made in the file.

.. L8

``$ hg diff``

.. R7

You see some cryptic output, but it's essentially giving you the list of
changes made to the file. All the lines that were deleted are preceded by a -
and all the new-lines are preceded by a +. You can see that the & occurrences
have been replaces with and. 

We should note here that, the diff wouldn't make much sense, if we had some
binary files like .jpg or .pdf files. We would see some gibberish in the
output. Let's now commit this change.

.. L9

``$hg commit``

``$hg log``

.. R8

We can pass an additional argument, -v or --verbose, to hg log to get the whole
commit message, instead of just the summary.

.. L10

``$hg log -v``

.. R9

Also, we are not always, interested to see the whole history of the project. It
would often suffice to see the last few commits.

.. L11

``$ hg log -v -l3``

.. R10

To limit the output of hg log, we could use the -l or --limit argument. Now it
will print only last three commits.

.. L12

*{{{Show the slide 'Revision Numbering'}}}*

.. R11

Often, the level of detail provided by the commit messages is also not enough.
We would want to see what exactly changed with a commit, probably as a diff. We
could do that using revision numbers. 

Use the log command to get a brief description of all the changes made, by
showing us the summary line of all the commits. Look at the changeset line in
the output of the command. It shows a number followed by a semi-colon and some
long hexa-decimal string. The number is called the revision number. It is an
identifier for the commit, and can be along with various commands to specify
the revision number, if required. 

.. L13

*{{{Show the slide  'Using revision numbers'}}}*


.. R12

The revision number can also be passed as an argument to many commands. Let's
say we wish to see the changes between revision 1 and revision 2. We shall use
the diff command to do this.

.. L14

``$ hg diff -r1 -r2``

.. R13

The diff command takes two revision numbers as arguments and gives the changes
made from revision in the first argument to revision in the second argument.

.. R14

It can be passed to other commands as well. For instance, we can check the logs
of the very first commit, by saying

.. L15

``$ hg log -r0``

.. R15

You could also specify a range of commits whose logs you would like to see.
Say, we would like to see the last two commits,

.. L16

``$ hg log -r0:2``

.. R16 

To see changes made to a particular file, in the speciifed range of commits, 

.. L17

``$ hg log -r0:2 chapter2.txt``


.. R17

This brings us to the end of the tutorial. In this tutorial, we have
seen,

.. L18

*{{{Show the 'summary' slide'}}}*

.. R18

In this tutorial, we have learnt to, 
 #. Undo changes to the repository using hg revert,
 #. View changes done to the repository using hg diff
 #. Use revision numbers as arguments to different hg commands

.. L19

*{{{ Show self assessment questions slide }}}*

.. R19

Here are some self assessment questions for you to solve
#. How to accomplish not saving backup files using hg revert command?
#. Get the history of revisions 2 to 4 without having to list each revision? 
#. Print the description and content of a change. Hint: Use --patch option

.. L20

*{{{ Solution of self assessment questions on slide }}}*

.. R20

And the answers,
1. hg revert -C --no-backup

2. hg log -r 2:4

3. hg log -v -p -r 2

.. L21

*{{{ Show the Thank you slide }}}*

.. R21

Hope you have enjoyed this tutorial and found it useful. Feel free to play
around with Mercurial and read the documentation given by hg help command. When
you are ready to move on, please proceed to the third tutorial on 'Version
Control using Hg'

Thank you!
