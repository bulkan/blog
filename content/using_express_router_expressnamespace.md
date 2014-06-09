Title: Using Express Router instead of express-namespace
Status: draft
Date: 2014-06-09 15:00
Tags: node.js, express, javascript
Category:
Slug: using_express_router_instead_of_express_namespace
lang: en
Author: Bulkan Evcimen
Summary:

express 4.0 has been out for a while and it seems people are still using
[express-namespace](https://www.npmjs.org/package/express-namespace). According to
npm it had 183 downloads on the 8th of June.

express-namespace can be easilly replaced with the Router that comes with express 4
as it hasn't been updated in 2 years ! 

Also I've found that the middleware mounting on namespace roots would mount it
at the the application level. This is what the router solves.

The router is quite handy. It allows you to seperate out __routes__ into different 
modules with its own middleware. 

Here is the example from express-namespace written using express 4.0 using the Router.

    var express = require('express'),
        forumRouter = express.Router(),
        threadRouter = express.Router(),
        app = express();

    forumRouter.get('/:id/((view)?)', function(req, res){
      res.send('GET forum ' + req.params.id);
    });

    forumRouter.get('/:id/edit', function(req, res){
      res.send('GET forum ' + req.params.id + ' edit page');
    });

    forumRouter.delete('/', function(req, res){
      res.send('DELETE forum ' + req.params.id);
    });

    app.use('/forum', forumRouter);

    threadRouter.get('/:id/thread/:tid', function(req, res){
      res.send('GET forum ' + req.params.id + ' thread ' + req.params.tid);
    });

    app.use('/forum', threadRouter);

    app.listen(3333);

A little bit more typing but easier to explain to others and no monkey patching
weirdness of express-namespace.


Hope this helps