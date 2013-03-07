Title: Django forms
Status:draft
Date: 2012-12-06 14:56:12
Tags: django python forms
Category: 
Slug: Django_forms
lang: en
Author: Bulkan Evcimen
Summary: 

Out of all the parts of Django I struggle with forms, especially when you want to customize it. Did you ever try to change the rendering of a django.forms.ChoiceField that uses a RadioSelect as it's widget ? If you have then you know the pain.

### Diagram 

Here is a diagram to show the hierarchy of how forms, fields and widget fit together. 

<img src="http://i.imgur.com/8Gire.jpg" alt="I used a Noodlers Ink Fountain Pen and Lamy Turqoise Ink" width="350px"/>


in code this looks like the following example; 


    from django.forms import Form, CharField, TextInput

    class ContactForm(django.forms.Form):
          name = CharField(widget=TextInput(attrs={"value": "Enter text"}))




        
