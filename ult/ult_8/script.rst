.. Objectives
.. ----------
   
   .. At the end of this tutorial, you will be able to:
   
   ..   1. Prepare a simple shell script. 
   ..   2. Run a script successfully and print it's result.
   ..   3. Understand what an environment variable is.

.. Prerequisites
.. -------------

..   1. Getting started with Linux
..   2. Basic file handling
..   3. Redirection and Piping
..   4. Text Processing


 
Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on 
'Shell scripts & Variables'.

.. L2

{{{ Show slide with objectives }}} 

.. R2

At the end of this tutorial, you will be able to,

1. Prepare a simple shell script. 
#. Run a script successfully and print it's result.
#. Understand what an environment variable is.

.. L3

{{{ Switch to the pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
previous tutorials as being displayed currently.

.. R4

Let us start with creating a simple shell script.
A shell script is simply a sequence of commands, that are put into a file,
instead of entering them one by one onto the shell. The script can then be
run, to execute the sequence of commands in a single shot instead of manually
running, each of the individual commands. 
For instance, let's say we wish to create a directory called ``marks`` in the
home folder and save the results of the students into a file
``results.txt``. 

.. L4

.. R5

We open an editor and save the following text to ``results.sh``

.. L5

{{{ Open an editor and type the following }}}
::

    #!/bin/bash
    mkdir ~/marks
    cut -d " " -f 2- marks1.txt | paste -d " " students.txt - | sort > ~/marks/
    results.txt

.. R6

We can now run the script as, 

.. L6

{{{ Open the terminal }}}
::

    ./results.sh

.. R7

We get an error saying, Permission denied! Why? Can you think of the
reason? Yes, the file doesn't have execute permissions.
We make the file executable and then run it. 

.. L7
::

    chmod u+x results.sh
    ./results.sh

.. R8

We get back the prompt. We can check the contents of the file
``results.txt`` to see if the script has run. 

So, here, we have our first shell script. The first line of the script is used 
to specify the interpreter or shell which should be used to execute the script. 
In this case, we are asking it to use the bash shell.
Once, the script has run, we get back the prompt. Here, we had to manually 
check, if the contents of the file are correct. It would be useful to have our 
script  print out messages. For this, we can use the ``echo`` command. We can 
edit ``results.sh`` script, as follows.

.. L8

{{{ Open an editor and type the following }}}
::

    #!/bin/bash
    mkdir ~/marks
    cut -d " " -f 2- marks1.txt | paste -d " " students.txt - | sort > ~/marks/
    results.txt
    echo "Results generated."

.. R9

Now, we get a message on the screen on running the script.

Let's now say, that we wish to let the user decide the file to which the
results should be written to. The results file, should be specifiable by an
argument in the command line. We can do so, by editing the file, as below. 

.. L9

{{{ Make the necessary changes in the previous script }}}

::

    #!/bin/bash
    mkdir ~/marks
    cut -d " " -f 2- marks1.txt|paste -d " " students.txt - | sort > ~/marks/$1
    echo "Results generated."


{{{ Highlight the text ``$1`` }}}

.. R10

The ``$1`` above, corresponds to the first command line argument in the
script. So, we can run the script as shown below, to save the results to
``grades.txt``. 

.. L10
::

    ./results.sh grades.txt    

.. R11

When we run the ``results.sh`` file, we are specifying the location of the
script by using ``./``(DOT FORWARD SLASH). But for any of the other commands, 
we didn't have to specify their locations. Why? The
shell has a set of locations where it searches, for the command that we are
trying to run. 

.. L11

.. L12

{{{ Show slide, PATH }}}

.. R12

These set of locations are saved in an "environment"
variable called PATH.let us look at what the value of the PATH variable is. 
To view the values of variables, we can use the echo command.

.. L13

{{{ Switch to the terminal }}}
::

    echo $PATH

.. R13

So, these are all the paths that are searched, when looking to execute a
command. If we put ``results.sh`` script in one of these locations, we
could simply run it, without using the ``./``(DOT FORWARD SLASH) at the 
beginning. 

.. R14

As expected, it is possible to define our own variables inside our shell
scripts. For example,

.. L14

{{{ Switch to the terminal }}}
::

    name="FOSSEE"

.. R15

It creates a new variable ``name`` whose value is ``FOSSEE``. To refer to this
variable, inside our shell script, we would refer to it, as ``$name``.
Note that, there is no space around the ``=`` sign. 

.. L15
::

    ls $name*


.. R16

It is possible to store the output of a command in a variable, by enclosing
the command in back-quotes. 

.. L16
::

    count=`wc -l wonderland.txt`

.. R17

It saves the number of lines in the file ``wonderland.txt`` in the variable
count. 

.. L17

.. L18

{{{ Show slide, variables & comments }}}

.. R18

The ``#`` character is used to comment out content from a shell script.
Anything that appears after the ``#`` character in a line, is ignored by
the bash shell. 

.. L19

{{{ Switch to 'Summary' slide }}}

.. R19

This brings us to the end of the end of this tutorial.
In this tutorial, we have learnt to, 

1. Prepare a shell script.
#. Display the result of a script, using the ``echo`` command.
#. Use the environment variable ``PATH``.
#. Create variables and comment out content using the ``#`` sign.

.. L20

{{{ Show self assessment questions slide }}}

.. R20

Here are some self assessment questions for you to solve

1. Which sign is used to comment out content from a shell script.
  
   - $
   - %
   - #
   - \* 

2. How will you add ``/data/myscripts`` directory to the beginning of the $PATH 
   environment variable ?

.. L21

{{{ Solution of self assessment questions on slide }}}

.. R21

And the answers,

1. We use the ``#`` sign to comment out the content from a shell script.

2. In order to add a directory to the beginning of the $PATH variable,we
   say,
::

    $PATH=/data/myscripts:$PATH

.. L22

{{{ Show the SDES & FOSSEE slide }}}

.. R22

Software Development techniques for Engineers and Scientists - SDES, is an 
initiative by FOSSEE. For more information, please visit the given link.

Free and Open-source Software for Science and Engineering Education - FOSSEE, is
based at IIT Bombay which is funded by MHRD as part of National Mission on 
Education through ICT.

.. L23

{{{ Show the ``About the Spoken Tutorial Project'' slide }}}

.. R23

Watch the video available at the following link. It summarises the Spoken 
Tutorial project.If you do not have good bandwidth, you can download and 
watch it. 

.. L24

{{{ Show the `` Spoken Tutorial Workshops'' slide }}}

.. R24

The Spoken Tutorial Project Team conducts workshops using spoken tutorials,
gives certificates to those who pass an online test.

For more details, contact contact@spoken-tutorial.org

.. L25

{{{ Show the ``Acknowledgements'' slide }}}

.. R25

Spoken Tutorial Project is a part of the "Talk to a Teacher" project.
It is supported by the National Mission on Education through ICT, MHRD, 
Government of India. More information on this mission is available at the 
given link.

.. L26

{{{ Show the Thank you slide }}}

.. R26

Hope you have enjoyed this tutorial and found it useful.
Thank you!


