
.. Prerequisites
.. -------------

.. Version Control with hg - Part 1

.. Author : Primal Pappachan
   Internal Reviewer :
   Date: Sept 23, 2011
   
   
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

1. Learn how to view and revert changes made to files in a repository.

#. Learn how to share repositories and deal with simultaneous conflicting changes.

.. L3

{{{Show the slide 'Operational overhead?'}}} 

.. R3 

Let's first try to find out why we should commit inspite of the additional operational costs and loss of time?

.. L4

{{{Show the slide 'Revert Changes'}}}

.. R4

The undo in your editor may allow undoing some changes(if you haven't closed it after making the changes) but there's no way of getting back deleted files using your editor. That's where mercurial comes to the rescue.

We shall use the revert command of hg to undo all the changes after the last commit. If we want to undo all the changes, we use the revert command with the --all argument, else use revert command with specific filename as argument.

.. L5

$ hg revert --all
reverting chapter1.txt
reverting chapter3.txt
$ hg st
? chapter1.txt.orig
$ ls
chapter1.txt  chapter1.txt.orig  chapter2.txt  chapter3.txt

.. R5

After running this command, you can see that all deleted files have been restored. But hg has generated new files with .orig extension.  Mercurial actually doesn't like to delete any of the changes that you have made. So, it makes a back-up of the already existing files in the present state and gives you back the old file.

If we now decide, that we want to redo the changes that we had done to the existing file, we can just overwrite it with the backed up file. 

.. L6

$ mv chapter1.txt.orig chapter1.txt
$ hg st
M chapter1.txt

.. L7

{{{Show the slide 'Viewing Changes'}}}

.. R6

Let's say we now want to commit these changes, but we are not sure of all the changes that we have made to the file, since it's been a while after we made the changes. We could use the diff command to see all the changes that have been made in the file.

.. L8

$ hg diff

.. R7

You see some cryptic output, but it's essentially giving you the list of changes made to the file. All the lines that were deleted are preceded by a - and all the new-lines are preceded by a +. You can see that the & occurrences have been replaces with and. 

We should note here that, the diff wouldn't make much sense, if we had some binary files like .jpg or .pdf files. We would see some gibberish in the output.

.. L9

{{{Show the slide 'Revision Numbering'}}}

.. R8

Often, the level of detail provided by the commit messages is also not enough. We would want to see what exactly changed with a commit, probably as a diff. We could do that using revision numbers. 

Use the log command to get a brief description of all the changes made, by showing us the summary line of all the commits. Look at the changeset line in the output of the command. It shows a number followed by a semi-colon and some long hexa-decimal string. The number is called the revision number. It is an identifier for the commit, and can be along with various commands to specify the revision number, if required.

.. L10

{{{Show the slide  'Using revision numbers'}}}


.. R9

The revision number can also be passed as an argument to many commands. Let's say we wish to see the changes between revision 1 and revision 2. We shall use the diff command to do this.

.. L11

$ hg diff -r1 -r2

.. R10

The diff command takes two revision numbers as arguments and gives the changes made from revision in the first argument to revision in the second argument.

.. R11

It can be passed to other commands as well. For instance, we can check the logs of the very first commit, by saying

.. L12

$ hg log -r0

.. R12

You could also specify a range of commits whose logs you would like to see. Say, we would like to see the last two commits,

.. L13

$ hg log -r0:2

.. R13 

When motivating the use of version control systems, we spoke a lot about collaboration and sharing our changes with our peers. Let us now see how we can share our project with our peers and collaborate with them.

.. L14

{{{Show the slide 'Cloning Repositories'}}}

.. R14

For this purpose let us create a central repository, a copy of our repository, which is different from the one in which we are working. The clone command is used to clone or replicate an existing repository.

.. L15

$hg clone SOURCE [DEST]
$ hg clone book book-repo

.. R15

The syntax of the clone command is -- hg clone SOURCE [DEST], where the optional argument DEST is being represented in brackets. The clone command can be used to replicate already existing repositories, either on your own machine or on some remote machine somewhere on the network. Since, hg maintains a copy of the full repository with every copy of the repository, the two copies that we have are exactly equivalent.

.. L16

{{{Show the slide 'Sharing Repositories'}}}

.. R16

A mercurial repository can be shared in multiple ways. We shall use the http protocol to share the repository. Mercurial comes inbuilt with a tiny server that can be used to share your repository over the network. To start sharing the repository, we say

.. L17

$hg serve

.. R17

This will start serving the repository on the network on the port 8000. Anybody in your network can access the repository in their browsers. Let us see how it looks, in our own browser.

.. L18

Open the url http://localhost:8000 in browser.

.. R18

To clone the repository, use

.. L19

$ hg clone http://my-ip-address:8000

.. R19

By this process, we share a central repository; work on our local copies. It doesn't make much sense to allow anybody to make changes to a public repository, by default. We will need to make changes to the settings of the repository to allow this. To set the write permissions, add the following lines in .hg/hgrc

.. L20

[web]
push_ssl=False
allow_push=*

.. R20 

This will allow anybody to push to the repository, now.

.. L21

{{{Show the slide 'Sharing Changes'}}}

.. R21

Use hg push to push your commits (changesets) to the central repository

.. L22

$ hg push

.. R22

Let us now pull these changes into our original repository that we have been working with.

.. L23

{{{Show the slide 'Pulling Changes'}}}

.. R23

Before pulling the changes, we can use the command hg incoming to see the changes that have been made to the repository after our last pull and the changesets that will be coming into our repository after we do a pull.

.. L24

$ hg incoming

.. R24

To now pull these changes, we use the pull command.

.. L25

$ hg pull

.. R25

These changes do not affect our working directory. To see this, we could use the hg parent command.

.. L26

$ hg parent

.. R26

As you can see, the parent is still our last commit, and the changes are still not in your working directory.

.. L27

{{{Show the slide 'Pulling Changes'}}}

.. R27

To get these changes we do the update as suggested by hg.

.. L28

$ hg update

.. R28

As expected the update command updates the parent to the latest changes that we just pulled from the remote repository.

1. Updates to the tip if no revision is specified

#. tip is the most recently added changeset

#. Can specify revision number to update to

.. R29

hg tip shows the tip of the repository

.. L29

$ hg tip

.. R30

What happens when two users have made simultaneous changes to the same file, by editing different parts at the same time.

.. L30

{{{Show the slide 'Simultaneous Changes'}}}

.. R31

With simultaneous changes, following things happen

1. The logs of both repositories will be different

#. The repositories have diverged

#. hg push fails, in such a scenario

.. L31

$ hg push
pushing to http://192.168.1.101:8000
searching for changes
abort: push creates new remote heads!
(did you forget to merge? use push -f to force)

.. R32 

Don't take the advice given by mercurial. Using the -f would be disastrous. We will leave out a discussion of that, for this course.

.. L32

{{{Show the slide 'Merging'}}}

.. R33

We will now need to pull the new changes that have been pushed to the repository after the last pull and merge them with the changes.

.. L33

$ hg pull

$ hg merge

.. R34

We have now pull the changes from the central repository and merged them with the changes in our repository. But, hg is warning us not to forget to commit. 

.. L34

$ hg commit 

.. R35

We can now push this changes to the central repository. We could also check the changes that will be pushed, before pushing them, using the hg outgoing command.

.. L35

{{{Show the slide 'Outgoing Changes'}}}

.. L36

$ hg outgoing 

$ hg push

.. R36

The changes have now been successfully pushed! Let us look at the web interface of the repo, to see that the changes have actually taken place.

.. L37

Show the Change graph in browser.

.. R37

What will happen if we edited the same portion of the file, at the same time? How would merges work? This will be the last thing that we are going to see in this part of the spoken tutorial. 

.. L38

{{{Show the slide 'Simultaneous Conflicting Changes'}}}

.. R38

Let's say both of us edit the same part of the same file.

1. hg push fails

#. So we first do hg pull

#. followed by hg merge


.. L39

$ hg push

$ hg pull

$ hg merge

.. R39

What happens now actually depends on how Mercurial is configured and the programs available in your machine. You will either get a diff view with 3 panes or merge will insert markers in your file at the points where the conflicts occur.

If you get a 3 pane view, the first pane is the actual file, where you make changes, to resolve the conflicts. The second pane shows the changes that you made, to the file. The last pane shows the changes that you pulled from the original repo. Once you are satisfied with the changes, save and quit.

Once you are done, you need to tell mercurial that you have resolved the conflicts manually.

.. L40

$ hg resolve -m filename

.. R40

You will now need to commit your changes, just like the simple merge that we performed.

.. L41

$ hg commit -m "Merge heads."
$ hg push

.. R41

We could look at the graph of the changes, in our web interface, which makes clear how the merging has occurred. 

.. L42

Show the change graph in browser.

.. R42 

Here's an advice on the Work-flow to be followed.

.. L43

{{{Show the slide 'Advice: Work-flow}}}


.. R43

That brings us to the end of this tutorial on Mercurial. What we have covered is nothing close to all the features of Mercurial. We've only scratched the surface, but let's hope that this will get you started and you will be able to organize your work and projects, better.

.. L44 

{{{Show the slide 'Summary'}}}

.. R44

In this tutorial, we have learnt to, 

1. Undo changes to the repository using hg revert,

#. View changes done to the repository using hg diff

#. Use revision numbers as arguments to different hg commands

#. Clone repositories, using hg clone,

#. Serve our repositories via http using hg serve,

#. push changes to a repository using hg push,

#. check the changesets in a repository after last pull, using hg incoming,

#. pull changes from a repository using hg pull ,

#. update the working directory, using hg update,

#. merge two heads, using hg merge,
 
#. and resolve conflicts using hg resolve.


.. L45

{{{ Show self assessment questions slide }}}

.. R45

Here are some self assessment questions for you to solve


.. L46

{{{ Solution of self assessment questions on slide }}}

.. R46

And the answers,



.. L47

{{{ Show the Thank you slide }}}

.. R47

Hope you have enjoyed this tutorial and found it useful.
Thank you!











