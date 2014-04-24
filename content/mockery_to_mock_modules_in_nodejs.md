Title: Using mockery to mock modules for Node.js testing  
Status: published
Date: 2014-04-24 16:12
Tags: node.js, mocha, sinon.js, should.js, request, javascript, mockery
Category:
Slug: using_mockery_to_mock_modules_nodejs
lang: en
Author: Bulkan Evcimen
Summary:


In a [previous article](http://bulkan-evcimen.com/testing_with_mocha_sinon) I wrote about mocking methods on the [request module](https://github.com/mikeal/request).

`request` also supports another workflow in which you directly call the imported module;

    var request = require('request');

    request({
      method: 'GET',
      url: 'https://api.github.com/users/bulkan'
    }, function(err, response, body){
      if (err) {
        return console.err(err);
      }

      console.log(body);
    })


You pass in an [options object](https://github.com/mikeal/request#requestoptions-callback) specifying properties like the HTTP method
to use and other properties such as `url`, `body` & `json`.

Here is the example from the [previous article](http://bulkan-evcimen.com/testing_with_mocha_sinon) using but updated to use `request(options)`;


    var request = require('request')
      , async   = require('async');

    function getProfile(username, cb){
      async.waterfall([
        function(callback){
          request({method: 'GET', url: 'https://api.github.com/users/' + username}, function(err, response, body){
            if (err) {
              return callback(err);
            }
            callback(null, body);
          });
        }
      ], cb)
    }

    module.exports = getProfile;

Its not that big of a change. To unit test the `getProfile` function we will need 
to mock out `request` module that is being imported by the module that `getProfile` 
is defined in.  This where [mockery](https://github.com/mfncooper/mockery) comes in. 
It allows us to change what gets returned when a module is imported.

Here is a mocha test case using mockery. This assumes that the above code is in a file named `gh.js`.

    var request = require('request')
      , sinon = require('sinon')
      , mockery = require('mockery')
      , getProfile = require('./gh');

    describe('User Profile', function(){
      var requestStub;

      before(function(){
        mockery.enable({
          warnOnReplace: false,
          warnOnUnregistered: false,
          useCleanCache: true
        });

        var requestStub = sinon.stub();

        // replace the module `request` with a stub object
        mockery.registerMock('request', requestStub);
        
      });

      after(function(){
        request.get.restore();
        mockery.disable();
      });

      it('can get user profile', function(done){
        requestStub.yields(null, {statusCode: 200}, {login: "bulkan"});

        getProfile('bulkan', function(err, result){
          if(err) {
            return done(err);
          }
          requestStub.called.should.be.equal(true);
          result.should.not.be.empty;
          done();
        });
      });
    })


`mockery` _hijacks_ the `require` function and replaces modules with our mocks. In the above code
we register a `sinon` stub to be returned when `require('request')` is called. Then we configure 
the mock in the test using the method `.yield` on the stub to a call the callback
function passed to `request` with `null` for the _error_, an object for the `response` and another object
for the `body`.

You can write more tests


Hope this helps.
