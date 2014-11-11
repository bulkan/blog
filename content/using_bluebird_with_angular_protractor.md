Title: Using Bluebird With Angular Protractor
Status: published
Date: 2014-11-11 10:00
Tags: node.js, angularjs, bluebird, promise, protractor
Category: 
Slug: using_bluebird_with_angular_protractor
lang: en
Author: Bulkan Evcimen
Summary:

## Async control flow

Just return a Promise from a function named `onPrepare` in your config.js

  onPrepare: function(){
    var Promise = require('bluebird');

    return Promise.delay(2000);
  }

 
This can be used to perform some async setup task like creating a fake User in your database
to be able to login.


    var User = require('./models/User');
    
    onPrepare: function() {
        return User.create({
            username: 'bulkan',
            password': 'igotdis'
        });
    }


## Test structure 

Protractor uses [Jasmine 1.3](https://github.com/juliemr/minijasminenode) and has updated it to [automatically resolve Promises](https://github.com/angular/jasminewd).


    describe('Home page', function(){
      it('should have username input', function(){
        var username = element(by.css('#username'));
        expect(username).not.toBeNull();
      });
    });


`expect` automatically resolves the Promise. This can be confusing especially if you're coming from Mocha. 

What do you do if you need to do an async task that returns a Promise ? Here is an example of a tests case 
that will verify that the home page is rendering Post titles.


    var Promise = require('bluebird'),
        Posts = require('./models/Posts');

    describe('Home Page', function(){
      it('should have a list of posts', function(done){

        browser.get('/');

        var posts = element(by.repeater('post in posts').column('post.title'));

        Promise.cast(posts).map(function(elm){
          return elm.getInnerHtml();
        })
        .then(function(titles){
          return titles.sort();
        })
        .then(function(titles){
          return Posts.findAll({attributes: 'title', order: 'title'})
            .tap(function(_titles){
              expect(titles).toEqual(_titles);
            })
         })
         .nodeify(done);
      });
    });


Jasmine supports asynchronous tests by passing in a callback function to an `it`, just like in Mocha. 
In the test above we find elements by the repeater the template might look like;


    <div ng-repeat="post in posts">
        <h1> {{:post.title}} </h1>
    </div>

and workout the innerHtml. We need to `Promise.cast` the `posts` as we call `.nodeify` which is a bluebird
function.

The post titles in the rendered template is compared to post titles from the database. There might be an easier/simpler
way to do this so please let me know.
