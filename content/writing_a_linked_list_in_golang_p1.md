Title: Writing a Linked List using Go - part one
Status: published
Date: 2013-05-30 16:45
Tags: linked list, golang, go
Category:
Slug: writing_linked_list_using_golang_part_one
lang: en
Author: Bulkan Evcimen
Summary:

In this article series I will briefly talk about Linked Lists then go about implementing one using [Go](http://golang.org). This is both a learning exercise for me to get comfortable using Go and to possibly help other developers transition into becoming a Go programmer. That being said please bare in mind I am still learning Go so excuse the code.

As Go already has a [linked list](http://golang.org/pkg/container/list/) implemented so dont peak.

Lets begin with a quick refresher on linked lists. Have a look at the following diagram;

<img src="http://i.imgur.com/gVLWlWn.jpg" width="50%" title="Drawn with a Faber-Castell Ambition in pearwood"/>

A linked list is a simple data structure that is used as the basis for other complex data structures. Linked lists are made up of _nodes_ each containing some _data_ attribute and the reference to the next node. In the diagram above or nodes contain an integer as the data. With this information let us write out the code for a node.

If we were using a Object Oriented language like say Python, then we could just create a class to represent the node. But Go is a procedural language and it does not support classes. That being said it does have [struct type](http://golang.org/ref/spec#Struct_types) which we can use to encapsulate the fields of a node.

```C
type node struct {
    data int
    next *node
}
```

