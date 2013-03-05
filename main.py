'''
Created on Mar 5, 2013

@author: siebz0r
'''
class RecursiveAttr(object):
    def __getattr__(self, name):
        if '.' in name:
            split = name.split('.', 1)
            return getattr(object.__getattribute__(self, split[0]), split[1])
        else:
            return object.__getattribute__(self, name)
        
    def __setattr__(self, name, value):
        if '.' in name:
            split = name.split('.', 1)
            setattr(object.__getattribute__(self, split[0]), split[1], value)
        else:
            object.__setattr__(self, name, value)

class Baz(RecursiveAttr):
    qux = 'qux'

class Bar(RecursiveAttr):
    baz = Baz()

class Foo(RecursiveAttr):
    bar = Bar()

if __name__ == "__main__":
    foo = Foo()
    # Test hasattr
    print(hasattr(foo, 'bar.baz.qux'))
    # Test getattr
    print(getattr(foo, 'bar.baz.qux'))
    # Test setattr
    setattr(foo, 'bar.baz.qux', 'quux')
    print(getattr(foo, 'bar.baz.qux'))