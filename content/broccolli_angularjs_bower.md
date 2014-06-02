Title: Broccoli and Angular.js
Status: published
Date: 2014-05-28 10:12
Tags: node.js, broccoli, angular
Category:
Slug: broccoli_and_angularjs
lang: en
Author: Bulkan Evcimen
Summary:

[Broccoli](http://www.solitr.com/blog/2014/02/broccoli-first-release/) is a relatively new asset builder. It is based on doing operations
on a trees of files.

Here is how I used it to concatenate frontend dependencies installed via 
bower and an angular.js app.

## Bower

First, let me show you the two files you need for bower.

### bower.json

Here is an example `bower.json` that lists the frontend dependencies. Note the `resolutions` property.

    {
      "dependencies": {
        "angular-ui-router": "0.2.8-bowratic-tedium",
        "angular-socket-io": "~0.6.0"
      },
      "resolutions": {
        "angular": "~1.2.16"
      }
    }

## .bowerrc

This is relative to your project and tells bower where to put the dependencies.

    {
        "directory": "public/vendor"
    }

## Broccoli

Now we need to install broccoli. I usually install the `broccoli-cli` globally and as per the
official [installation guide](https://github.com/broccolijs/broccoli#installation).

    npm install --save-dev broccoli
    npm install --global broccoli-cli

## Brocfile.js
