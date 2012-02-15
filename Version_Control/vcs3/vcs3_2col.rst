
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



+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{ Show the first slide containing title, name of the production team along    | Hello friends and welcome to the tutorial on 'Version Control with Hg'           |
| with the logo of MHRD}}}*                                                        |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide 'Prerequisite'}}}*                                            | Please make sure that you have gone through the following tutorials before you   |
|                                                                                  | continue on this tutorial                                                        |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide containing the objectives}}}*                                 | At the end of this tutorial you will be able to                                  |
|                                                                                  |                                                                                  |
|                                                                                  | 1. Learn how to view and revert changes made to files in a repository.           |
|                                                                                  |                                                                                  |
|                                                                                  | #. Learn how to share repositories and deal with simultaneous conflicting change |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide 'Revert Changes'}}}*                                          | While you were wondering, let's say your friend walks in and together you make   |
|                                                                                  | a lot of changes. 1. You replace all the occurrences of & in chapter1.txt with   |
|                                                                                  | and. 2. You delete the chapter3.txt file.                                        |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg revert --all``                                                            | After running this command, you can see that all deleted files have been         |
|                                                                                  | restored. But hg has generated new files with .orig extension.  Mercurial        |
| ``reverting chapter1.txt``                                                       | actually doesn't like  to delete any of the changes that you have made. So, it   |
|                                                                                  | makes a back-up of the already existing files in the present state and gives     |
| ``reverting chapter3.txt``                                                       | you back the old file.                                                           |
|                                                                                  |                                                                                  |
| ``$ hg st``                                                                      | If we now decide, that we want to redo the changes that we had done to the       |
|                                                                                  | existing file, we can just overwrite it with the backed up file.                 |
| ``? chapter1.txt.orig``                                                          |                                                                                  |
|                                                                                  |                                                                                  |
| ``$ ls``                                                                         |                                                                                  |
|                                                                                  |                                                                                  |
| ``chapter1.txt  chapter1.txt.orig  chapter2.txt  chapter3.txt``                  |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ mv chapter1.txt.orig chapter1.txt``                                          | Let's say we now want to commit these changes, but we are not sure of all the    |
|                                                                                  | changes that we have made to the file, since it's been a while after we made     |
| ``$ hg st``                                                                      | the changes. We could use the diff command to see all the changes that have      |
|                                                                                  | been made in the file.                                                           |
| ``M chapter1.txt``                                                               |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``{{{Show the slide 'Viewing Changes'}}}``                                       | You see some cryptic output, but it's essentially giving you the list of         |
|                                                                                  | changes made to the file. All the lines that were deleted are preceded by a -    |
|                                                                                  | and all the new-lines are preceded by a +. You can see that the & occurrences    |
|                                                                                  | have been replaces with and.                                                     |
|                                                                                  |                                                                                  |
|                                                                                  | We should note here that, the diff wouldn't make much sense, if we had some      |
|                                                                                  | binary files like .jpg or .pdf files. We would see some gibberish in the         |
|                                                                                  | output. Let's now commit this change.                                            |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg diff``                                                                    | We can pass an additional argument, -v or --verbose, to hg log to get the whole  |
|                                                                                  | commit message, instead of just the summary.                                     |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$hg commit``                                                                   | Also, we are not always, interested to see the whole history of the project. It  |
|                                                                                  | would often suffice to see the last few commits.                                 |
| ``$hg log``                                                                      |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$hg log -v``                                                                   | To limit the output of hg log, we could use the -l or --limit argument. Now it   |
|                                                                                  | will print only last three commits.                                              |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg log -v -l3``                                                              | Often, the level of detail provided by the commit messages is also not enough.   |
|                                                                                  | We would want to see what exactly changed with a commit, probably as a diff. We  |
|                                                                                  | could do that using revision numbers.                                            |
|                                                                                  |                                                                                  |
|                                                                                  | Use the log command to get a brief description of all the changes made, by       |
|                                                                                  | showing us the summary line of all the commits. Look at the changeset line in    |
|                                                                                  | the output of the command. It shows a number followed by a semi-colon and some   |
|                                                                                  | long hexa-decimal string. The number is called the revision number. It is an     |
|                                                                                  | identifier for the commit, and can be along with various commands to specify     |
|                                                                                  | the revision number, if required.                                                |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide 'Revision Numbering'}}}*                                      | The revision number can also be passed as an argument to many commands. Let's    |
|                                                                                  | say we wish to see the changes between revision 1 and revision 2. We shall use   |
|                                                                                  | the diff command to do this.                                                     |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide  'Using revision numbers'}}}*                                 | The diff command takes two revision numbers as arguments and gives the changes   |
|                                                                                  | made from revision in the first argument to revision in the second argument.     |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg diff -r1 -r2``                                                            | It can be passed to other commands as well. For instance, we can check the logs  |
|                                                                                  | of the very first commit, by saying                                              |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg log -r0``                                                                 | You could also specify a range of commits whose logs you would like to see.      |
|                                                                                  | Say, we would like to see the last two commits,                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg log -r0:2``                                                               | To see changes made to a particular file, in the speciifed range of commits,     |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg log -r0:2 chapter2.txt``                                                  | This brings us to the end of the tutorial. In this tutorial, we have             |
|                                                                                  | seen,                                                                            |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the 'summary' slide'}}}*                                                | In this tutorial, we have learnt to,                                             |
|                                                                                  |  #. Undo changes to the repository using hg revert,                              |
|                                                                                  |  #. View changes done to the repository using hg diff                            |
|                                                                                  |  #. Use revision numbers as arguments to different hg commands                   |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{ Show self assessment questions slide }}}*                                   | Here are some self assessment questions for you to solve                         |
|                                                                                  |                                                                                  |
|                                                                                  | #. How to accomplish not saving backup files using hg revert command?            |
|                                                                                  | #. Get the history of revisions 2 to 4 without having to list each revision?     |
|                                                                                  | #. Print the description and content of a change. Hint: Use --patch option       |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{ Solution of self assessment questions on slide }}}*                         | And the answers,                                                                 |
|                                                                                  |                                                                                  |
|                                                                                  | 1. hg revert -C --no-backup                                                      |
|                                                                                  |                                                                                  |
|                                                                                  | 2. hg log -r 2:4                                                                 |
|                                                                                  |                                                                                  |
|                                                                                  | 3. hg log -v -p -r 2                                                             |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{ Show the Thank you slide }}}*                                               | Hope you have enjoyed this tutorial and found it useful. Feel free to play       |
|                                                                                  | around with Mercurial and read the documentation given by hg help command. When  |
|                                                                                  | you are ready to move on, please proceed to the third tutorial on 'Version       |
|                                                                                  | Control using Hg'                                                                |
|                                                                                  |                                                                                  |
|                                                                                  | Thank you!                                                                       |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
