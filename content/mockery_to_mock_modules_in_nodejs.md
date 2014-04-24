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
`request` supports another workflow;

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


It allows you to pass in an [options object](https://github.com/mikeal/request#requestoptions-callback) specifying the HTTP method
and other properties such as `url`, `body` & `json` etc...

Here is the example from [previous article](http://bulkan-evcimen.com/testing_with_mocha_sinon);


    var request = require('request')
      , async   = require('async');

    function getProfile(username, cb){
      async.waterfall([
        function(callback){
          request({method: 'GET', url: 'https://api.github.com/users/' + username}, function(err, response, body){
            if (err) return callback(err);
            callback(null, body);
          });
        }
      ], cb)
    }

    module.exports = getProfile;


To unit test the `getProfile` function we will need to mock out `request` that is being `require`d by the module that `getProfile` is defined in.
To mock out  modules function we will use [mockery](https://github.com/padraic/mockery) here is the code assuming the above code is in a file named `gh.js`.

    var request = require('request')
      , sinon = require('sinon')
      , mockery = require('mockery')
      , getProfile = require('./gh');

    describe('User Profile', function(){
      before(function(){

        // mockery hijacks the `require` function and replaces modules with mocks
        mockery.enable({
          warnOnReplace: false,
          warnOnUnregistered: false,
          useCleanCache: true
        });

        var requestStub = sinon.stub().yields(null, null, JSON.stringify({login: "bulkan"}));

        // replace the module `request` with a stub object
        mockery.registerMock('request', requestStub);
        
      });

      after(function(){
        request.get.restore();
        mockery.disable();
      });

      it('can get user profile', function(done){
        getProfile('bulkan', function(err, result){
          if(err) return done(err);
          request.get.called.should.be.equal(true);
          result.should.not.be.empty;
          done();
        });
      });
    })



Bonus
-----
