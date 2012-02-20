
================================
Version Control using Hg  Part 4
================================

.. Prerequisites
.. -------------

.. Version Control using Hg Part 1, 2, 3


.. Author : Primal Pappachan
   Internal Reviewer :
   Date: Jan 27, 2012

======
Script
======

.. L1

*{{{ Show the first slide containing title, name of the production team along
with the logo of MHRD}}}*

.. R1

Hello friends and welcome to the fourth part of tutorial on 'Version Control wit

.. L2

*{{{Show the slide 'Prerequisite'}}}*

.. R2

Please make sure that you have gone through the following tutorials before you
continue on this tutorial

.. L3

*{{{Show the slide containing the objectives}}}*

.. R3

At the end of this tutorial you will be able to
 #. Clone existing repositories 
 #. Share your repositories with peers
 #. use version control for collaborating with your peers

.. L4

*{{{Show the slide 'Cloning Repositories'}}}*

.. R4

When motivating the use of version control systems, we spoke a lot about
collaboration and sharing our changes with our peers. Let us now see how we can
share our project with our peers and collaborate with them.

For this purpose let us create a central repository, a copy of our repository,
which is different from the one in which we are working. The clone command is
used to clone or replicate an existing repository.

.. L5

``$hg clone SOURCE [DEST]``

``$ hg clone book book-repo``

.. R5

The syntax of the clone command is -- hg clone SOURCE [DEST], where the
optional argument DEST is being represented in brackets. The clone command can
be used to replicate already existing repositories, either on your own machine
or on some remote machine somewhere on the network. Since, hg maintains a copy
of the full repository with every copy of the repository, the two copies that
we have are exactly equivalent.

In this example book-repo shall be our central repository we are sharing with
peers.

.. L6

*{{{Show the slide 'Sharing Repositories'}}}*

.. R6

A mercurial repository can be shared in multiple ways. We shall use the http
protocol to share the repository. Mercurial comes inbuilt with a tiny server
that can be used to share your repository over the network. To start sharing
the repository, we say

.. L7

``$cd ../book-repo``

``$hg serve``

.. R7

This will start serving the repository on the network on the port 8000. Anybody 

.. L8

Open the url http://localhost:8000 in browser.

.. R8

Now if your friend John wishes to clone the repository, use

.. L9

``$ hg clone http://my-ip-address:8000 book-john``

.. R9


By this process, we share a central repository; work on our local copies. It
doesn't make much sense to allow anybody to make changes to a public
repository, by default. We will need to make changes to the settings of the
repository to allow this. To set the write permissions, add the following lines
in .hg/hgrc

.. L10

``[web]``

``push_ssl=False``

``allow_push=*``

.. R10 

This will allow anybody to push to the repository, now. John can now push and
his changes will appear in the central repository.

.. L11


*{{{Show the slide 'Sharing Changes'}}}*

.. R11

Use hg push to push your commits (changesets) to the central repository. The
changes made by Primal will appear in the central repository.

.. L12

``$ hg push``

.. R12

Let's now see how to get the changes from central repository.

.. L13

*{{{Show the slide 'Pulling Changes'}}}*

.. R13

Before pulling the changes, we can use the command hg incoming to see the
changes that have been made to the repository after our last pull and the
changesets that will be coming into our repository after we do a pull.

.. L14

``$ hg incoming``

.. R14

If you wish  pull those changes shown by hg incoming, we use the pull command.

.. L15

``$ hg pull``

.. R15

These changes do not affect our working directory. To see this, we could use
the hg parent command.

.. L16

``$ hg parent``

.. R16

As pulling in the changes, the parent will still be the last commit, and the
changes are still not in your working directory.

.. L17

*{{{Show the slide 'Pulling Changes 2'}}}*

.. R17

To get these changes we do the update as suggested by hg.

.. L18

``$ hg update``

.. R18

The update command updates the parent to the latest changes that we
just pulled from the remote repository.
 
 #. Updates to the tip if no revision is specified
 #. tip is the most recently added changeset
 #. Can specify revision number to update to

You can try

.. L19

``$ hg up -r1``

.. R19

hg tip shows the tip of the repository

.. L20

``$ hg tip``

.. R20

What happens when two users have made simultaneous changes to the same file,
by editing different parts at the same time.

.. L21

*{{{Show the slide 'Simultaneous Changes'}}}*

.. R21

With simultaneous changes, following things happen
 #. The logs of both repositories will be different
 #. The repositories have diverged
 #. hg push fails, in such a scenario



Don't take the advice given by mercurial. Using the -f would be disastrous. We
will leave out a discussion of that, for this course.

.. L22

*{{{Show the slide 'Merging'}}}*

.. R22

The new changes that have been pushed to the 
repository after the last pull, has to be pulled and merged. So
use following commands in order

.. L24

``$ hg pull``

``$ hg merge``

.. R24

We have now pulled the changes from the central repository and merged them with
the changes in our repository. As hg warns u, do not forget to commit. 

.. L25

``$ hg commit``

.. R25

The changes can be pushed to the central repository now. We could also check
the changes that will be pushed, before pushing them, using the hg outgoing 
command.

.. L26

*{{{Show the slide 'Outgoing Changes'}}}*

.. L26

``$ hg outgoing``

``$ hg push``

.. R26

The changes have now been successfully pushed! Let us look at the web interface
of the repo, to see that the changes have actually taken place.

.. L27

Show the Change graph in browser.

.. R27

What will happen if we edited the same portion of the file, at the same time?
How would merges work? This will be the last thing that we are going to see in
this part of the spoken tutorial. 

.. L28

*{{{Show the slide 'Simultaneous Conflicting Changes'}}}*

.. R28

Let's say both of us edit the same part of the same file.
 #. hg push fails
 #. So we first do hg pull
 #. followed by hg merge


.. L29

``$ hg commit``

``$ hg push``

``$ hg pull``

``$ hg merge``

.. R29

What happens now actually depends on how Mercurial is configured and the
programs available in your machine. You will either get a diff view with 3
panes or merge will insert markers in your file at the points where the
conflicts occur.

If you get a 3 pane view, the first pane is the actual file, where you make
changes, to resolve the conflicts. The second pane shows the changes that you
made, to the file. The last pane shows the changes that you pulled from the
original repo. Once you are satisfied with the changes, save and quit.

Once you are done, you need to tell mercurial that you have resolved the
conflicts manually.

.. L30

``$ hg resolve -m filename``

.. R30

You will now need to commit your changes, just like the simple merge that we per

.. L31

``$ hg commit -m "Merge heads."``

``$ hg push``

.. R31

We could look at the graph of the changes, in our web interface, which makes
clear how the merging has occurred. 

.. L32

Show the change graph in browser.

.. R32 

Here's an advice on the Work-flow to be followed.

.. L33

*{{{Show the slide 'Advice: Work-flow}}}*


.. R33

That brings us to the end of this tutorial on Mercurial. What we have covered
is nothing close to all the features of Mercurial. We've only scratched the
surface, but let's hope that this will get you started and you will be able to
organize your work and projects, better.

.. L34

*{{{Show the 'summary' slide'}}}*

.. R35

In this tutorial, we have learnt to, 

#. Clone repositories, using hg clone,
#. Serve our repositories via http using hg serve,
#. push changes to a repository using hg push,
#. check the changesets in a repository after last pull, using hg incoming,
#. pull changes from a repository using hg pull ,
#. update the working directory, using hg update,
#. merge two heads, using hg merge,
#. and resolve conflicts using hg resolve.

.. L36

*{{{Show the slide 'Evaluation'}}}*

.. R36

Here are some self assessment questions for you to solve
 #. Mention the easiest way to get started on sharing your repository by providi
 #. Suppose Joey and Melissa have made simultaneous changes to the same file in 
 #. What are the commands involved in the process of merging changes? 
   
.. L37

*{{{ Show Solution of self assessment questions on slide }}}*

.. R37

And the answers,

 #. hg serve
 #. No, whenever we've done a merge, hg parents will display two parents until w
 #. hg pull, hg merge, hg commit -m "Merged Remote changes"

.. L38

*{{{Show the slide 'Additional Reading'}}}*

.. R38

It is strongly recommended that you to go through the following topics, once
you are comfortable with using Mercurial on a day-to-day basis.

 #. .hgignore
 #. hg rollback
 #. hg bisect
 #. hg backout


.. L39

{{{ Show the Thank you slide }}}

.. R39

Hope you have enjoyed this tutorial and found it useful. Feel free to play
around with Mercurial and read the documentation given by hg help command. When
you are ready to move on, please proceed to the third tutorial on 'Version
Control using Hg'

Thank you!


