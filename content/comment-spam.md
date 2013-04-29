Title: Comment Spam
Status:published
Date: 2008-07-01 14:46:33
Tags: spam
Category: 
Slug: comment-spam
lang: en
Author: Bulkan Evcimen
Summary: 

So, this is my new blog written by me using Django and a free template from Rambling Soul. The other day i went *live* by changing DNS settings by pointing http://blog.bulkan-evcimen.com to the IP address of my VPS. Two days later some posts had comment spam! Im working on adding a new field to comment  form to find out if you are human or not.

*EDIT*: So no more comment spam. how did i fix it ? Easy, i just removed the code inside of the individual Post handling view function which checked for POST requests and the comment form fields and then created a new comment.

