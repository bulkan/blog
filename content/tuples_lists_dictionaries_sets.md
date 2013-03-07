Title: Tuples, Lists, Dictionaries and .... ? (sets)
Status:draft
Date: 2008-01-02 21:57:00
Tags: 
Category: 
Slug: Tuples_Lists_Dictionaries_sets
lang: en
Author: Bulkan Evcimen
Summary: 

So we all know about tuples (immutable sequences)
 
    emtpyTuple = (,) 
    names = ('bob','jane') 
    print names[0] 


Lists (mutable sequences)

    emtpyTuple = []
    names = ['bob','jane']
    print names[0]


and Dictionaries (mutable mapping)

    emptyDict = {} 
    numbers = { 'one':1, 'two':2, 'three':3}
    print numbers['two']`



But how many of you know of (and used) Sets ?
Sets were available in Python 2.3 from the set module but are now a built-in type since 2.4.

There are two types of sets;


   1. set (mutable, unordered collection of immutable values)

   2. frozenset (immutable, unordered collection of immutable values)

Sets can hold any data type as long as they're hashable (sets are implemented using hash tables)


<a href="http://docs.python.org/lib/types-set.html">Python Docs for Set Types</a><br /><br /><br /><br><br /><a href="http://technorati.com/tag/python" rel="tag"><img style="border:0;vertical-align:middle;margin-left:.4em" src="http://static.technorati.com/static/img/pub/icon-utag-16x13.png?tag=python" alt=" " />python</a>