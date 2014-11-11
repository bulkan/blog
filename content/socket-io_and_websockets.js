
Title: Socket.IO and WebSockets
Status: draft
Date: 2014-06-28 16:00
Tags: node.js, socketio, websockets
Category: 
Slug: socket_io_and_websockets
lang: en
Author: Bulkan Evcimen
Summary:



I am not sure if everyone feels this way but socket.io has become synonomous with WebSockets. 

This is not true. What I mean is that if you expect a vanilla WebSocket to connect  to a socket.io
server it won't work. Socket.io version 1.x.x is a wrapper around Engine.io 1.x.x. Engine.io provides
fallbacks for __realtime__ transports. In browsers that support WebSockets thats what will be used. If 
not it will be used for 


* socket.io v1.x.x is a wrapper around engine.io
* synonomous with "websockets" or "real time"
* what are websockets ?
* [websockets rfc 6455](http://tools.ietf.org/html/rfc6455) is what chrome implements 
  * socket.io does not seem to implement this rfc
