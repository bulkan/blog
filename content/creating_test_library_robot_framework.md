Title: Creating a Robot Framework Test Library
Status:draft
Date: 2011-08-16 15:01:35
Tags: python robotframework
Category: 
Slug: creating_test_library_robot_framework
lang: en
Author: Bulkan Evcimen
Summary: 

If you are not familiar with Robot Framework (RF) here is a quote from the homepage;

> Robot Framework is a Python-based, extensible keyword-driven test automation framework for end-to-end acceptance testing and acceptance-test-driven development (ATDD). It can be used for testing distributed, heterogeneous applications, where verification requires touching several technologies and interfaces.

Robot Framework comes with a great set of built-in keywords that will help you get started in writing test cases for all sort programs. You have Selenium Library to test web applications. There is also keyword libraries for Sikuli and AutoIt for desktop application testing. This post will show give a quick example of how to create your own custom keyword library using Python.

A keyword library is just a Python file containing a class with the same name as the file. For example the OperatingSystem that comes with RF is in a file called OperatingSystem.py and contains a class with the same name.  


[See here for more information](http://robotframework.googlecode.com/svn/tags/robotframework-2.5.6/doc/userguide/RobotFrameworkUserGuide.html#creating-test-libraries)










