Title: Express.js for Django Ponies 
Status: published
Date: 2013-09-27 15:00
Tags: node.js, express, django, python, javascript
Category:
Slug: express_for_django_ponies
lang: en
Author: Bulkan Evcimen
Summary:


Introduction
------------

Express is the most popular _web_ framework in Node.js and It can be used in a way that can be very similar to Django. Hopefully in this article I will show you how to do this.


Install Node.js
---------------

If you have not installed `Node.js` go ahead and get it from [here](http://nodejs.org/download/). On OS X installation is quickly done via the package installer. On a linux distribution I usually download the prebuilt binaries and extract them into `/usr/local/etc` then create symlinks for `node` and `npm`. You can do this via;


```
wget http://nodejs.org/dist/v0.10.18/node-v0.10.18-linux-x64.tar.gz
tar xvfz node-v0.10.18-linux-x64.tar.gz
sudo mv node-v0.10.18-linux-x64 /usr/local/etc
sudo ln -s /usr/local/etc/node/bin/node /usr/local/bin/node
sudo ln -s /usr/local/etc/node/bin/node_modules/npm/cli.js /usr/local/bin/node/npm
```

Once installed quickly test your installion via these commands.

`node --version` and `npm --version`

You should see version numbers for `node` & `npm`.


Express yourself
----------------

Install `express` using the following command.

`npm install express`

Remember `virtualenv` in Python to keep package versions seperate.
