Title: Running QTP tests using Python
Status:published
Date: 2009-09-18 16:37:50
Tags: qtp python com testing
Category: 
Slug: running_qtp_test_using_python
lang: en
Author: Bulkan Evcimen
Summary: 

QTP provides an interface called the **automation object model**. This **model** is essentially a COM interface providing a bunch of objects that can be used to automate QTP. The full object list is available in the **QuickTest Professional Automation** documentation.

Running QTP tests from the command line is useful for doing scheduled automatic testing. If you use a continuous integration system to do automatic builds of your software, you can run your QTP tests on the latest build. 

The following is a Python script that is able to run a test and print out *Passed* or *Failed*.  It is a direct port of example code in the documentation written in VBScript

<script src="http://gist.github.com/188917.js"></script>