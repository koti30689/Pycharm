#import pytest

def func(n):
    s=0
    for i in range(1,n):
        return s+n
def test():
    assert func(157)/1==0
def test2():
    assert func(1)/1==0
def test3():
    assert func(0)/1==0



