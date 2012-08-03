.. Objectives
.. ----------
   
   .. At the end of this tutorial, you will be able to:
   
   ..   1. Know what is TDD.
   ..   2. Understand the use of test cases.
   ..   3. Write simple tests for a function.

.. Prerequisites
.. -------------

..   1. Getting started with functions

 
Script
------

.. L1

{{{ Show the  first slide containing title, name of the production
team along with the logo of MHRD }}}

.. R1

Hello friends and Welcome to the tutorial on 
'Test driven development - Part 1'.

.. L2

{{{ Show slide with objectives }}} 

.. R2

At the end of this tutorial, you will be able to,

 1. understand basics of Test Driven Development.
 #. understand the use test cases.
 #. write simple tests for a function.

.. L3

{{{ Switch to the slide3, pre-requisite slide }}}

.. R3

Before beginning this tutorial,we would suggest you to complete the 
tutorial on "Getting started with functions".

.. R4

Test-driven development is a software development 
process that relies on the repetition of a very short 
development cycle.
In TDD,one writes a failing automated test case that 
defines a desired improvement or new function, then produces
code to pass that test and finally refactors the new code to
acceptable standards.


.. L4

{{{ Switch to slide4 ,What is TDD?}}}


.. R5

To illustrate TDD, lets take a simple program. Consider a 
function ``fibonacci``, that takes one argument and returns 
the nth number of ``fibonacci`` series.

.. L5

{{{ Switch to slide5, First test- fibonacci }}}

.. R6 

To test ``fibonacci`` function, we need test
cases.
As shown in this slide,
test cases are expected outputs for a given set of inputs.


.. L6

{{{ Switch to slide6, Test cases }}}

.. R7

The sample code for test cases is shown here. Observe that if 
any ``if`` statement is executed, test aborts after printing the
error message.

.. L7
 
{{{ Switch to slide7, Test cases-Code }}}

.. R8

The ``fibonacci`` function is written just enough so that 
test can run.


.. L8

{{{ switch to slide8, Stubs }}}

.. R9

Combine the function and test cases and put them together in 
``fibonacci.py`` file.Add the test cases after name=main idiom.

.. L9

{{{ Switch to slide9, fibonacci.py }}}

.. R10

Lets run fibonacci.py by typing ``python fibonacci.py``.
As we haven't written any meaningful code in our ``fibonacci``
function, it fails immediately.
Our next step is to write just minimum code to pass our tests.

.. L10

{{{ Run the fibonacci.py in terminal and show the error output.}}}
::
     
    python fibonacci.py

.. R11

Modify the fibonacci stub function with given code. 
Save and run it again as `` python fibonacci.py``. 
{{{ pause }}}
Observe that, there will be no errors, as 
the test passes successfully.

.. L11

{{{ switch to slide-11, Euclidean Algorithm }}}
Switch to terminal and modify fibonacci function in ``nano``
editor and run.
::

    python fibonacci.py
   
.. R12

The same ``fibonacci`` function is modified to make it more readable
and easy to understand using recursion.
Pause this video here.Replace the ``fibonacci`` function with recursive one.
Run the modified ``fibonacci.py`` file. The test should pass again 
without any errors.
After successfully achieving this result, you can resume the video.

.. L12

{{{ Show slide12, Euclidean Algorithm- Recursive}}}


.. R13

This brings us to the end of the tutorial.In this tutorial,
 we have learnt to,
 
 1. Undestand the basic steps involved in Test driven development.
 #. Design a Test driven approach for a given ``fibonacci`` function.


.. L13

{{{ switch to slide-13,Summary }}}

.. R14

Here are some self assessment questions for you to solve

 1. Design a TDD approach for a factorial function.
 2. Design a TDD approach for an armstrong function. 

.. L14

{{{ switch to slide-14, Evaluation }}}

.. R15

And the answers are,
 1. {{{ show answer slide-1 }}}

 2. {{{ show answer slide-2 }}}

.. L15

{{{ switch to slide-15 ,Solutions}}}

.. R16

Hope you have enjoyed this tutorial and found it useful.
Thank you!

.. L16

{{{ Switch to slide-16, Thankyou}}}

