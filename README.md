Dogecode
========

By Rhea Myers.

Brainfuck interpreter by Sebastian Kaspari under the WTFPL. 

A system for representing and running programs as Dogeparty tokens.

Read the whitepaper in doc/ for details of how the system works now and how it is planned to be extended.

Installation
============

     python setup.py install

Usage
=====

Local
=====

You will need a running and correctly configured DogeParty Node in order to run these commands.

To compile a program, run e.g.:

    dcc -o test.csv hello-world.bf

This will convert the Brainfuck code to a csv file of token runs.

To upload a program, run e.g.:

    dcsend -u rpcuser -w rpcpassword FROMADDRESS TOADDRESS hello-world.csv

You must control FROMADDRESS, and TOADDRESS should be a newly created address with no existing asset tokens attached. You should also probably control it.

Sending will take a very long time (see the whitepaper), and will transfer lots of tokens from FROMADDRESS. Make sure you got the addresses right and that the program ran OK when tested locally by dcc. And don't quit dcsend, restarting is not yet supported. 

To execute a program, run e.g.:

    dcrun -u rpcuser -w rpcpassword TOADDRESS

This will fetch the program from TOADDRESS, run it locally, and output the results (if any) to the console.

Via Web API
-----------

These commands access a remote blockchain explorer over the network.

To execute a program, run e.g.:

    dcrunw ADDRESS

This will fetch the program from ADDRESS, run it locally, and output the results (if any) to the console.

Warning
=======

 Be careful when writing and uploading Dogecode programs. You are responsible for ensuring that programs run as expected and that you send the correct tokens to the correct addresses. Expense and sadness will accompany any errors.
