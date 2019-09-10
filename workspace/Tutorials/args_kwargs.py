#!/usr/bin/env python3

def arg_func(*args, **kwargs):
    for arg in args:
        print arg
    for kwarg in kwargs:
        print kwarg

    print("Received in *args: {}".format(args))
    print("Received in *kwargs: {}".format(kwargs))

arg_func(1, "two", 3.0, hello="world", dog="cat", up="down")
