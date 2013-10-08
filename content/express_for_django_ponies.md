Title: Getting Started With Express.js for Django Ponies
Status: published
Date: 2013-09-27 15:00
Tags: node.js, express, django, python, javascript
Category:
Slug: getting_started_with_express_for_django_ponies
lang: en
Author: Bulkan Evcimen
Summary:


Introduction
------------

Express is the most popular _web_ framework in Node.js and It can be used along with a few other packages in a way that can be very similar to Django.

I have seen and read about places using Django with _tastypie_ or _Django REST Framework_ to create the backend API to be used with a frontend written with _Ember_, _Angular.js_ or _KnockoutJS_.

Personally I believe that `Node.js` is better suited for this use case.  Hopefully in this article I will show you how to get started with `Express.js`, `Mongoose`.

Install Node.js
---------------

If you have not installed `Node.js` go ahead and get it from [here](http://nodejs.org/download/). On OS X installation is quickly done via the package installer. On a Linux distribution I usually download the prebuilt binaries and extract them into `/usr/local/etc` then create symlinks for `node` and `npm`. You can do this via;


```
wget http://nodejs.org/dist/v0.10.18/node-v0.10.18-linux-x64.tar.gz
tar xvfz node-v0.10.18-linux-x64.tar.gz
sudo mv node-v0.10.18-linux-x64 /usr/local/etc
sudo ln -s /usr/local/etc/node/bin/node /usr/local/bin/node
sudo ln -s /usr/local/etc/node/bin/node_modules/npm/cli.js /usr/local/bin/node/npm
```

Once installed quickly test your installion with these commands.

`node --version` and `npm --version`

You should see version numbers for `node` & `npm`.

Express yourself
----------------

Install `express` using the following command.

`npm install express`

Here is the obligatory _Hello World_ web app.

Create a file called `hello_world.js` and copy paste the following.

```
var express = require('express')
  , app = express();

app.get('/', function(req, res){
  res.send('Hello World');
});

app.listen(8080, function(){
  console.log('started server on port 8080')';
});
```

Save the file. In a terminal type `node hello_world.js`

This will start a http server on port 8080. If you go to [http://localhost:8008/](http://localhost:8080) in a browser you sould see _Hello World_.

This usage of Express should remind you of Flask and Bottle.


Views
-----

In Django a view is a function that gets called with a HttpRequest object and returns a HttpResponse (or subclass) object.


ORM
---

For an ORM we will use `Mongoose` which is a Object Document Mapper for `MongoDB`.

Read the Mongo installation guide to install it.

`npm install mongoose`

A simple model;

```
var mongoose = require('mongoose');

```
