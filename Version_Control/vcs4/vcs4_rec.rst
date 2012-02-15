
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



+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{ Show the first slide containing title, name of the production team along    | Hello friends and welcome to the fourth part of tutorial on 'Version Control wit |
| with the logo of MHRD}}}*                                                        |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide 'Prerequisite'}}}*                                            | Please make sure that you have gone through the following tutorials before you   |
|                                                                                  | continue on this tutorial                                                        |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide containing the objectives}}}*                                 | At the end of this tutorial you will be able to                                  |
|                                                                                  |  #. Clone existing repositories                                                  |
|                                                                                  |  #. Share your repositories with peers                                           |
|                                                                                  |  #. use version control for collaborating with your peers                        |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide 'Cloning Repositories'}}}*                                    | When motivating the use of version control systems, we spoke a lot about         |
|                                                                                  | collaboration and sharing our changes with our peers. Let us now see how we can  |
|                                                                                  | share our project with our peers and collaborate with them.                      |
|                                                                                  |                                                                                  |
|                                                                                  | For this purpose let us create a central repository, a copy of our repository,   |
|                                                                                  | which is different from the one in which we are working. The clone command is    |
|                                                                                  | used to clone or replicate an existing repository.                               |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$hg clone SOURCE [DEST]``                                                      | The syntax of the clone command is -- hg clone SOURCE [DEST], where the          |
|                                                                                  | optional argument DEST is being represented in brackets. The clone command can   |
| ``$ hg clone book book-repo``                                                    | be used to replicate already existing repositories, either on your own machine   |
|                                                                                  | or on some remote machine somewhere on the network. Since, hg maintains a copy   |
|                                                                                  | of the full repository with every copy of the repository, the two copies that    |
|                                                                                  | we have are exactly equivalent.                                                  |
|                                                                                  |                                                                                  |
|                                                                                  | In this example book-repo shall be our central repository we are sharing with    |
|                                                                                  | peers.                                                                           |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide 'Sharing Repositories'}}}*                                    | A mercurial repository can be shared in multiple ways. We shall use the http     |
|                                                                                  | protocol to share the repository. Mercurial comes inbuilt with a tiny server     |
|                                                                                  | that can be used to share your repository over the network. To start sharing     |
|                                                                                  | the repository, we say                                                           |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$cd ../book-repo``                                                             | This will start serving the repository on the network on the port 8000. Anybody  |
|                                                                                  |                                                                                  |
| ``$hg serve``                                                                    |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Open the url http://localhost:8000 in browser.                                   | Now if your friend Primal wishes to clone the repository, use                    |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg clone http://my-ip-address:8000 book-primal``                             | Now if Primal makes some changes to the repository and tries to commit it fails  |
|                                                                                  | obviously as access rights haven't been taken care of.                           |
|                                                                                  |                                                                                  |
|                                                                                  | By this process, we share a central repository; work on our local copies. It     |
|                                                                                  | doesn't make much sense to allow anybody to make changes to a public             |
|                                                                                  | repository, by default. We will need to make changes to the settings of the      |
|                                                                                  | repository to allow this. To set the write permissions, add the following lines  |
|                                                                                  | in .hg/hgrc                                                                      |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``[web]``                                                                        | This will allow anybody to push to the repository, now. Primal can now push and  |
|                                                                                  | his changes will appear in the central repository.                               |
| ``push_ssl=False``                                                               |                                                                                  |
|                                                                                  |                                                                                  |
| ``allow_push=*``                                                                 |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide 'Sharing Changes'}}}*                                         | Use hg push to push your commits (changesets) to the central repository. The     |
|                                                                                  | changes made by Primal will appear in the central repository.                    |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg push``                                                                    | Let us now pull these changes into our original repository that we have been     |
|                                                                                  | working with.                                                                    |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide 'Pulling Changes'}}}*                                         | Before pulling the changes, we can use the command hg incoming to see the        |
|                                                                                  | changes that have been made to the repository after our last pull and the        |
|                                                                                  | changesets that will be coming into our repository after we do a pull.           |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg incoming``                                                                | To now pull these changes, we use the pull command.                              |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg pull``                                                                    | These changes do not affect our working directory. To see this, we could use     |
|                                                                                  | the hg parent command.                                                           |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg parent``                                                                  | As you can see, the parent is still our last commit, and the changes are still   |
|                                                                                  | not in your working directory.                                                   |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide 'Pulling Changes'}}}*                                         | To get these changes we do the update as suggested by hg.                        |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg update``                                                                  | As expected the update command updates the parent to the latest changes that we  |
|                                                                                  | just pulled from the remote repository.                                          |
|                                                                                  |                                                                                  |
|                                                                                  |  #. Updates to the tip if no revision is specified                               |
|                                                                                  |  #. tip is the most recently added changeset                                     |
|                                                                                  |  #. Can specify revision number to update to                                     |
|                                                                                  |                                                                                  |
|                                                                                  | For example                                                                      |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg up -r1``                                                                  | hg tip shows the tip of the repository                                           |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg tip``                                                                     | What happens when two users have made simultaneous changes to the same file,     |
|                                                                                  | by editing different parts at the same time.                                     |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide 'Simultaneous Changes'}}}*                                    | With simultaneous changes, following things happen                               |
|                                                                                  |  #. The logs of both repositories will be different                              |
|                                                                                  |  #. The repositories have diverged                                               |
|                                                                                  |  #. hg push fails, in such a scenario                                            |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg push``                                                                    | Don't take the advice given by mercurial. Using the -f would be disastrous. We   |
|                                                                                  | will leave out a discussion of that, for this course.                            |
| ``pushing to http://192.168.1.101:8000``                                         |                                                                                  |
|                                                                                  |                                                                                  |
| ``searching for changes``                                                        |                                                                                  |
|                                                                                  |                                                                                  |
| ``abort: push creates new remote heads!``                                        |                                                                                  |
|                                                                                  |                                                                                  |
| ``(did you forget to merge? use push -f to force)``                              |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide 'Merging'}}}*                                                 | We will now need to pull the new changes that have been pushed to the            |
|                                                                                  | repository after the last pull and merge them with the changes.                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg pull``                                                                    | We have now pull the changes from the central repository and merged them with    |
|                                                                                  | the changes in our repository. But, hg is warning us not to forget to commit.    |
| ``$ hg merge``                                                                   |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg commit``                                                                  | We can now push this changes to the central repository. We could also check the  |
|                                                                                  | changes that will be pushed, before pushing them, using the hg outgoing          |
|                                                                                  | command.                                                                         |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg outgoing``                                                                | The changes have now been successfully pushed! Let us look at the web interface  |
|                                                                                  | of the repo, to see that the changes have actually taken place.                  |
| ``$ hg push``                                                                    |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Show the Change graph in browser.                                                | What will happen if we edited the same portion of the file, at the same time?    |
|                                                                                  | How would merges work? This will be the last thing that we are going to see in   |
|                                                                                  | this part of the spoken tutorial.                                                |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide 'Simultaneous Conflicting Changes'}}}*                        | Let's say both of us edit the same part of the same file.                        |
|                                                                                  |  #. hg push fails                                                                |
|                                                                                  |  #. So we first do hg pull                                                       |
|                                                                                  |  #. followed by hg merge                                                         |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg commit``                                                                  | What happens now actually depends on how Mercurial is configured and the         |
|                                                                                  | programs available in your machine. You will either get a diff view with 3       |
| ``$ hg push``                                                                    | panes or merge will insert markers in your file at the points where the          |
|                                                                                  | conflicts occur.                                                                 |
| ``$ hg pull``                                                                    |                                                                                  |
|                                                                                  | If you get a 3 pane view, the first pane is the actual file, where you make      |
| ``$ hg merge``                                                                   | changes, to resolve the conflicts. The second pane shows the changes that you    |
|                                                                                  | made, to the file. The last pane shows the changes that you pulled from the      |
|                                                                                  | original repo. Once you are satisfied with the changes, save and quit.           |
|                                                                                  |                                                                                  |
|                                                                                  | Once you are done, you need to tell mercurial that you have resolved the         |
|                                                                                  | conflicts manually.                                                              |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg resolve -m filename``                                                     | You will now need to commit your changes, just like the simple merge that we per |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``$ hg commit -m "Merge heads."``                                                | We could look at the graph of the changes, in our web interface, which makes     |
|                                                                                  | clear how the merging has occurred.                                              |
| ``$ hg push``                                                                    |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Show the change graph in browser.                                                | Here's an advice on the Work-flow to be followed.                                |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide 'Advice: Work-flow}}}*                                        | That brings us to the end of this tutorial on Mercurial. What we have covered    |
|                                                                                  | is nothing close to all the features of Mercurial. We've only scratched the      |
|                                                                                  | surface, but let's hope that this will get you started and you will be able to   |
|                                                                                  | organize your work and projects, better.                                         |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the 'summary' slide'}}}*                                                |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
|                                                                                  | In this tutorial, we have learnt to,                                             |
|                                                                                  |                                                                                  |
|                                                                                  | #. Clone repositories, using hg clone,                                           |
|                                                                                  | #. Serve our repositories via http using hg serve,                               |
|                                                                                  | #. push changes to a repository using hg push,                                   |
|                                                                                  | #. check the changesets in a repository after last pull, using hg incoming,      |
|                                                                                  | #. pull changes from a repository using hg pull ,                                |
|                                                                                  | #. update the working directory, using hg update,                                |
|                                                                                  | #. merge two heads, using hg merge,                                              |
|                                                                                  | #. and resolve conflicts using hg resolve.                                       |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide 'Evaluation'}}}*                                              | Here are some self assessment questions for you to solve                         |
|                                                                                  |  #. Mention the easiest way to get started on sharing your repository by providi |
|                                                                                  |  #. Suppose Joey and Melissa have made simultaneous changes to the same file in  |
|                                                                                  |  #. What are the commands involved in the process of merging changes?            |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{ Show Solution of self assessment questions on slide }}}*                    | And the answers,                                                                 |
|                                                                                  |                                                                                  |
|                                                                                  |  #. hg serve                                                                     |
|                                                                                  |  #. No, whenever we've done a merge, hg parents will display two parents until w |
|                                                                                  |  #. hg pull, hg merge, hg commit -m "Merged Remote changes"                      |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| *{{{Show the slide 'Additional Reading'}}}*                                      | It is strongly recommended that you to go through the following topics, once     |
|                                                                                  | you are comfortable with using Mercurial on a day-to-day basis.                  |
|                                                                                  |                                                                                  |
|                                                                                  |  #. .hgignore                                                                    |
|                                                                                  |  #. hg rollback                                                                  |
|                                                                                  |  #. hg bisect                                                                    |
|                                                                                  |  #. hg backout                                                                   |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the Thank you slide }}}                                                 | Hope you have enjoyed this tutorial and found it useful. Feel free to play       |
|                                                                                  | around with Mercurial and read the documentation given by hg help command. When  |
|                                                                                  | you are ready to move on, please proceed to the third tutorial on 'Version       |
|                                                                                  | Control using Hg'                                                                |
|                                                                                  |                                                                                  |
|                                                                                  | Thank you!                                                                       |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
