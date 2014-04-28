Title: Mocking a function that returns a (bluebird) Promise 
Status: published
Date: 2014-04-28 16:12
Tags: node.js, mocha, sinon.js, should.js, javascript, promise, bluebird
Category:
Slug: mocking_function_that_returns_promise
lang: en
Author: Bulkan Evcimen
Summary:

With Sinon.JS mocking functions are quite easy. Here is how to stub a function 
that returns a Promise. 

Study the following code (assume its a file name named `gh.js`);

var request = require('request')
  , Promise = require('bluebird')
  , getAsync = Promise.promisify(request.get);

module.exports.getProfile = function getProfile(username) {
  return getAsync('https://api.github.com/users/' + username);
}

We require `request` & `bluebird` then export out a single function `getProfile` from the module.
`getProfile` calls and returns the value from `getAsync` which is the [promisified](https://github.com/petkaantonov/bluebird/blob/master/API.md#promisepromisifyobject-target---object)
function for `request.get` and its return value is a [Promise](https://github.com/petkaantonov/bluebird/blob/master/API.md#thenfunction-fulfilledhandler--function-rejectedhandler---function-progresshandler----promise).

The mocha unit test for the above which stubs out `getAsync` in the `gh.js` module;


