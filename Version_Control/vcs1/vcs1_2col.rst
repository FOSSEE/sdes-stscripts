.. Prerequisites
.. -------------

.. None

.. Author : Primal Pappachan
   Internal Reviewer : Kiran Isukapatla
   Date: May 10 2012

--------
Script
--------



+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the first slide containing title, name of the production team along     | Hello friends and welcome to the tutorial on 'Version Control with Hg'           |
| with the logo of MHRD}}}                                                         |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{Show the slide containing the objectives}}}                                   | At the end of this tutorial you will be able to                                  |
|                                                                                  |                                                                                  |
|                                                                                  | 1. Understand what is Version Control.                                           |
|                                                                                  |                                                                                  |
|                                                                                  | #. Identify the need for using Version Control.                                  |
|                                                                                  |                                                                                  |
|                                                                                  | #. Install Mercurial.                                                            |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{Show the slide 'what is version control'}}}                                   | First, let's understand what 'Version Control' is.                               |
|                                                                                  |                                                                                  |
|                                                                                  | 'Version control' is a way to track files over time and share them.              |
|                                                                                  | This allows access to earlier versions of a file(s) if and when required.        |
|                                                                                  | It therefore enables us to make changes to the content of a file, view it's      |
|                                                                                  | change log and collaborate on a single piece of work with a team of people.      |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{Show the slide 'Home-brewed'}}}                                               | Lets look at an example of home-brewed Version Control system.Version control    |
|                                                                                  | is a way of backing up files, before making changes. Most people would have      |
|                                                                                  | cooked up their own version control system.                                      |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{Show the next slide 'Home-brewed'}}}                                          | Listing the files in the folder we observe that after a point of time it         |
|                                                                                  | becomes difficult to maintain proper names for different versions of a file.     |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{Show the slide 'Problems'}}}                                                  | Let's look at the various problems associated with this set-up.                  |
|                                                                                  |                                                                                  |
|                                                                                  | 1. Name and changes made are not related or linked.                              |
|                                                                                  |                                                                                  |
|                                                                                  | #. Can't track sequence of changes made to a file.                               |
|                                                                                  |                                                                                  |
|                                                                                  | #. Does not scale.                                                               |
|                                                                                  |                                                                                  |
|                                                                                  | To overcome this problems there are more general purpose tools which can         |
|                                                                                  | do this task in an organized way.                                                |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{Show the slide 'The need for Version Control'}}}                              | Now, let's move to identifying the needs for a 'Version Control System'.         |
|                                                                                  |                                                                                  |
|                                                                                  | We have seen that one of the main motivations to use a Version Control system    |
|                                                                                  | is the ability to go back to a working version of a file, when something         |
|                                                                                  | goes wrong. Below are a few more advantages of using an automated version        |
|                                                                                  | control system.                                                                  |
|                                                                                  |                                                                                  |
|                                                                                  | 1. By tracking the history of a project, any person may see the evolution        |
|                                                                                  | of a project.                                                                    |
|                                                                                  |                                                                                  |
|                                                                                  | 2. Allows for effective collaboration on a project, as everything is shared.     |
|                                                                                  |                                                                                  |
|                                                                                  | 3. Helps to identify which additions have broken down a project and thus         |
|                                                                                  | aids in efficient tracking down of the bugs.                                     |
|                                                                                  |                                                                                  |
|                                                                                  | 4. It is good for a one man show as it is for a big group of people working      |
|                                                                                  | on a project.                                                                    |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{Show the slide 'How does it work? - Analogy}}}                                | It is, in some ways, similar to playing a video game. We generally play games    |
|                                                                                  | in stages. While playing, we save the game at some instances as per our choice.  |
|                                                                                  | We continue playing, but we could, if necessary, choose to go back to one of the |
|                                                                                  | saved states and start over. In this manner, we could change the state of        |
|                                                                                  | the game.                                                                        |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{Show the slide 'Mercurial or hg'}}}                                           | Some of the Version Control tools available and used widely are: cvs, svn,       |
|                                                                                  | git and so on.                                                                   |
|                                                                                  |                                                                                  |
|                                                                                  | Each of these tools have their own merits and demerits. In this tutorial we      |
|                                                                                  | shall learn how to use mercurial or hg.                                          |
|                                                                                  |                                                                                  |
|                                                                                  | Mercurial or hg is:                                                              |
|                                                                                  |                                                                                  |
|                                                                                  | 1. Easy to learn and use                                                         |
|                                                                                  |                                                                                  |
|                                                                                  | #. Lightweight                                                                   |
|                                                                                  |                                                                                  |
|                                                                                  | #. Scales excellently                                                            |
|                                                                                  |                                                                                  |
|                                                                                  | #. Written in Python                                                             |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{Switch to terminal}}}                                                         | Type sudo apt-get install mercurial                                              |
| ::                                                                               |                                                                                  |
|                                                                                  | Type hg                                                                          |
|     $sudo apt-get install mercurial                                              |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
|                                                                                  |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ::                                                                               | It will give you the list of basic commands.                                     |
|                                                                                  |                                                                                  |
|     $hg                                                                          |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ::                                                                               | and 'hg version' gives the version number of mercurial you are presently using.  |
|                                                                                  |                                                                                  |
|     $hg version                                                                  |                                                                                  |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{Show the 'summary' slide'}}}                                                  | This brings us to the end of the tutorial. In this tutorial, we have             |
|                                                                                  | learnt:                                                                          |
|                                                                                  |                                                                                  |
|                                                                                  | 1. What is Version Control.                                                      |
|                                                                                  |                                                                                  |
|                                                                                  | #. Identify the need for using Version Control                                   |
|                                                                                  |                                                                                  |
|                                                                                  | #. Install Mercurial.                                                            |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{Show self assessment questions slide}}}                                       | Here are some self assessment questions for you to solve                         |
|                                                                                  |                                                                                  |
|                                                                                  | 1. Is Mercurial a Centralized VCS or Distributed Version Control System?         |
|                                                                                  |                                                                                  |
|                                                                                  | #. How can you retrive the version of Mercurial installed?                       |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{Show the solutions slide to self assessment questions }}}                     | And the answers,                                                                 |
|                                                                                  |                                                                                  |
|                                                                                  | 1. Mercurial is a Distributed Version Control system.                            |
|                                                                                  |                                                                                  |
|                                                                                  | #. hg version                                                                    |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the SDES & FOSSEE slide }}}                                             | Software Development techniques for Engineers and Scientists - SDES, is an       |
|                                                                                  | initiative by FOSSEE. For more information, please visit the given link.         |
|                                                                                  |                                                                                  |
|                                                                                  | Free and Open-source Software for Science and Engineering Education - FOSSEE, is |
|                                                                                  | based at IIT Bombay which is funded by MHRD as part of National Mission on       |
|                                                                                  | Education through ICT.                                                           |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the ``About the Spoken Tutorial Project'' slide }}}                     | Watch the video available at the following link. It summarises the Spoken        |
|                                                                                  | Tutorial project.If you do not have good bandwidth, you can download and         |
|                                                                                  | watch it.                                                                        |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the `` Spoken Tutorial Workshops'' slide }}}                            | The Spoken Tutorial Project Team conducts workshops using spoken tutorials,      |
|                                                                                  | gives certificates to those who pass an online test.                             |
|                                                                                  |                                                                                  |
|                                                                                  | For more details, contact contact@spoken-tutorial.org                            |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{ Show the ``Acknowledgements'' slide }}}                                      | Spoken Tutorial Project is a part of the "Talk to a Teacher" project.            |
|                                                                                  | It is supported by the National Mission on Education through ICT, MHRD,          |
|                                                                                  | Government of India. More information on this mission is available at the        |
|                                                                                  | given link.                                                                      |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| {{{Show the thank you slide}}}                                                   | Hope you have enjoyed this tutorial and found it useful.                         |
|                                                                                  | Thank you                                                                        |
+----------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
