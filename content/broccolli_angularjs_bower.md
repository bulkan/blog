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

Now we need to install broccoli. Ive installed the `broccoli-cli` globally and as per the
[installation guide](https://github.com/broccolijs/broccoli#installation).

    npm install --save-dev broccoli
    npm install --global broccoli-cli

We also need to install plugins for broccoli;

    npm install --saveDev broccoli-concat broccoli-gzip 

## Brocfile.js

Like all __task__ runners broccoli has its own file format to define its operations, though
its not really a __task__ runner but rather a build tool.

Here is the `brocfile.js` to concatenate all of the above bower dependencies


    var broccoli = require('broccoli');
    var gzipFiles = require('broccoli-gzip');
    var concat = require('broccoli-concat');


    var concatenated = concat('public/',  {
      inputFiles: [
        'vendor/jquery/jquery.min.js',
        'vendor/jquery-ui/ui/jquery-ui.js',
        'vendor/bootstrap/dist/js/bootstrap.min.js',
        'vendor/lodash/dist/lodash.min.js',
        'vendor/socket.io-client/socket.io.js',
        'vendor/angular/angular.js',
        'vendor/angular-flash/dist/angular-flash.min.js',
        'vendor/select2/select2.js',
        'vendor/angular-socket-io/socket.js',
        'vendor/angular-ui-select2/src/select2.js',
        'vendor/angular-ui-router/release/angular-ui-router.min.js',
        'vendor/angular-ui-slider/src/slider.js',
        'js/**/*.js',
      ],
      outputFile: '/assets/app.js',
      separator: '\n', // (optional, defaults to \n)
      wrapInEval: false // (optional, defaults to false)
    });


    module.exports =  gzipFiles(concatenated, {
      keepUncompressed: true,
      extensions: ['js', 'css'],
    });
