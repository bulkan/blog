Using Custom Events With  LimeJS
################################

:tags: javascript, limejs
:date: 2012-04-29 23:04:43
:lang: en
:slug: using_custom_events_with_limejs
:status: published
:author: Bulkan Evcimen
:summary: Learn how to use custom events with LimeJS

.. _LimeJS: http://limejs.com/0-getting-started 
.. _here: LimeJS_

.. _EventTarget:  http://docs.closure-library.googlecode.com/git/class_goog_events_EventTarget.html
.. _goog.events.EventTarget: EventTarget_

.. _Event: http://docs.closure-library.googlecode.com/git/class_goog_events_Event.html
.. _goog.events.Event: Event_

.. _lime.Sprite: http://limejs.digitalfruit.ee/docs/symbols/lime.Sprite.html



LimeJS_ is an open source JavaScript HTML5 game creation framework built using Google Closure. In this article I will show you how to create a new event type and dispatch it, which is more so a Closure feature than LimeJS. I am going to assume you have installed LimeJS if not read the instructions here_.

We will create a simple *game* that will display a Sprite that will change color randomly when the user touches it. When the color chosen randomly is greater than 128 we will dispatch a custom event.

It is kind of a contrived example but I hope it will serve the purpose of helping you.

Create a new LimeJS project by typing the following, which will create a directory called :code:`events_tutorial` and two files in this directory, :code:`events_tutorial.html` and :code:`events_tutorial.js`

.. code-block:: bash
    :linenos:

    bin/lime.py create events_tutorial

I like to create a separete file to store all my event types and dispatcher so lets start with that file. 

Create a new new file in :code:`events_tutorial` called :code:`events.js` directory and paste in the following.

.. code-block:: javascript
    :linenos:

    goog.provide('events_tutorial.Events');

    goog.require('goog.events.Event');
    goog.require('goog.events.EventTarget');

    events_tutorial.Events = new goog.events.EventTarget();

    events_tutorial.Events.ChangeColorEvent = function() {
        goog.events.Event.call(this, 'CHANGECOLOR');
    };

    goog.inherits(events_tutorial.Events.ChangeColorEvent, goog.events.Event);

Closure provides goog.events.EventTarget_ for dispatching events and listening to them. For this purpose we create a
new instance on line 6 which we will use in the Sprite subclass we will create further down. We could have instead
subclassed from goog.events.EventTarget_ but just creating an instance will suffice.

To distguish between events we will need to create a subclass from goog.events.Event_ which is done on lines 8-10. 
The important part of that code is block is the call to the base class. Make sure you use pass a unique string as 
this will be the string that we use to identify the event type.

Time to use this event in a new Sprite.

Create a new new file in :code:`events_tutorial` called :code:`coloredsprite.js` directory and paste in the following.

.. code-block:: js
   :linenos:

    goog.provide('events_tutorial.ColoredSprite');

    goog.require('lime.Sprite');
    goog.require('lime.animation.ColorTo');

    goog.require('events_tutorial.Events');

    events_tutorial.ColoredSprite = function(width, height) {
        goog.base(this);

        this.setSize(width, height).
            setFill(100, 100, 100);
    };
    goog.inherits(events_tutorial.ColoredSprite, lime.Sprite);

    events_tutorial.ColoredSprite.prototype.changeColor = function() {
        var c = Math.floor(Math.random() * 256);

        if (c > 128 ) {
            events_tutorial.Events.dispatchEvent(
                new events_tutorial.Events.ChangeColorEvent()
            );
        }
        this.runAction(new lime.animation.ColorTo(c, c, c));
    }

Here we create a subclass from lime.Sprite_ in which the constructor requires the width and height parameters that define the size.
The changeColor method will be the callback method when the user touches or clicks on the Sprite. On line 20 we dispatch an event
by creating a new instance of our event type we defined in :code:`events.js`.

Let us now connect all of this together in :code:`events_tutorial.js` which will look like the following.


.. code-block:: js
    :linenos:

    goog.provide('events_tutorial');

    goog.require('lime.Director');
    goog.require('lime.Scene');
    goog.require('lime.Layer');
    goog.require('lime.Label');
    goog.require('lime.animation.FadeTo');
    goog.require('lime.animation.Spawn');
    goog.require('lime.animation.ScaleTo');

    goog.require('events_tutorial.ColoredSprite');
    goog.require('events_tutorial.Events');

    events_tutorial.start = function(){
        var director = new lime.Director(document.body,1024,768),
            scene = new lime.Scene(),
            target = new lime.Layer().setPosition(512,384);

        var cs = new events_tutorial.ColoredSprite(1024,768);
        target.appendChild(cs);
        scene.appendChild(target);
        director.makeMobileWebAppCapable();

        goog.events.listen(events_tutorial.Events, ['CHANGECOLOR'], function() {
            var pop = new lime.Label().
                    setSize(0,0).
                    setPosition(100, 100).
                    setText("Event Triggered").
                    setFontFamily('Comic Sans').
                    setFontColor("red").
                    setFontSize(35);

            target.appendChild(pop);
            var zoomOut = new lime.animation.Spawn(
                new lime.animation.ScaleTo(2).setDuration(1),
                new lime.animation.FadeTo(0).setDuration(1)
            );
            pop.runAction(zoomOut);
        });

        goog.events.listen(cs, ['mousedown','touchstart'], cs.changeColor);
        director.replaceScene(scene);
    }

    goog.exportSymbol('events_tutorial.start', events_tutorial.start);

Most of the code above is boiler plate. We create instance of Director, Scene and a Layer.
What is important is that we also create an instance of our ColoredSprite class and add it to the Layer called *target*. We then listen to the custom event that is being dispatched on line 24.

Hope this helped.
