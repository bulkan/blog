Title: Javascript....
Status:published
Date: 2007-05-16 20:05:00
Tags: javascript
Category: 
Slug: javascript
lang: en
Author: Bulkan Evcimen
Summary: 

<span style="color: rgb(0, 0, 153);">var myArray = new Array();</span><br /><span style="color: rgb(0, 0, 153);">myArray[0] = "hello";</span><br /><span style="color: rgb(0, 0, 153);">myArray[1] = "merhaba";</span><br /><span style="color: rgb(0, 0, 153);">myArray[2] = "ciao";</span><br /><br /><span style="color: rgb(0, 0, 153);">for (var i=0;i<myarray.length;i++)></myarray.length;i++)></span><br /><span style="color: rgb(0, 0, 153);">     alert(myArray[i]);</span><br /><br /><span style="color: rgb(0, 0, 153);">var myOtherArray = [];</span><br /><span style="color: rgb(0, 0, 153);">myOtherArray[0] = "hello";</span><br /><span style="color: rgb(0, 0, 153);"> myOtherArray[1] = "merhaba";</span><br /><span style="color: rgb(0, 0, 153);"> myOtherArray[2] = "ciao";</span><br /><br /><span style="color: rgb(0, 0, 153);"> for (var i=0;i<myotherarray.length;i++)></myotherarray.length;i++)></span><br /><span style="color: rgb(0, 0, 153);">      alert(myOtherArray[i]);</span><br /><br /><br
/><span style="font-style: italic;">Can someone tell me the difference in these Vectors....i mean Arrays that are dynamic in size but you can't delete a single element at index X.<br /><br /></span><span>EDIT:<br /><br />After all this pain and Googling, i found how to remove elements from an array in javascript.<br />A big fvcking round of applause for the splice method.<br /><br /><span style="color: rgb(0, 0, 153);">splice(index,length):</span> starting from index remove elements until length.<br /></span><br />
