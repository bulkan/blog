Title: Why i love Python
Status:draft
Date: 2008-07-03 16:44:03
Tags: python
Category: 
Slug: why-i-love-python
lang: en
Author: Bulkan Evcimen
Summary: 

The title might suggest that i might be a Python fanboy, the truth is i may be bordering very close to actually being one (See the Python tag count to the right). But Python is *awesome* and here is one reason why i think so.


The other day i was playing around with <a href="http://code.google.com/p/pydigg/">pydigg</a> the Python bindings for accessing the Digg API. Well i was actually looking for a particular story that i had dugg.

     from digg import *
     d=Digg(APPKEY)
     diggs = d.getUserDiggs('user')
<br>
The thing with pydigg is that each time you run;


    diggs = d.getUserDiggs('user')
<br>
it would re-retrieve the data in XML from digg again and this was slowing me down. So i thought, well you know what you can cache the results for each request. Instead of hacking in a new cache system i just searched on Python Cheeseshop for  *cache*.  The second hit on the result page was *GenericCache*. After downloading and installing it (which i could have probably easy_installed) i just added the following to *digg.py*


<b>to the top of the file</b>


    from GenericCache.GenericCache import GenericCache
    from GenericCache.decorators import cached
    cache = GenericCache(expiry=30)
<br>
</b>and decorated _get with</b>


    @cached(cache)
    def _get(self, endpoint, **params):
<br>
Now each and every request will be cached for 30 seconds (because _get is the internal *private* method that handles the digg IO). So for the following  
     

     diggs = d.getUserDiggs('userA')
     diggs = d.getUserDiggs('userB')
     
<br>
GenericCache will create two entries based on the parameters.
<br>
So how does this show why Python is awesome?  Well it took me no more than 10 minutes to add caching.