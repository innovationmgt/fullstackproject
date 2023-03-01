##################### Class Decorators
#Creating decorators using classes

import functools

class Debug(object):

    def __init__(self, function):
        self.function = function
        # functools.wraps for classes
        functools.update_wrapper(self, function)   #this is the functools.wraps for Classes 

    def __call__(self, *args, **kwargs):
        output = self.function(*args, **kwargs)
        print('%s(%r, %r): %r' % (
            self.function.__name__, args, kwargs, output))
        return output
@Debug  ##########Class Decorator is here
def spam(eggs):
    return 'spam' * (eggs % 5)
output = spam(3)


# Decorating class functions
import functools


def plus_one(function):
    @functools.wraps(function)
    def _plus_one(self, n):
        return function(self, n + 1)
    return _plus_one


class Spam(object):
    @plus_one
    def get_eggs(self, n=2):
        return n * 'eggs '


spam = Spam()
spam.get_eggs(3)


# Properties – smart descriptor usage
#property decorator

class Spam(object):

    def get_eggs(self):
        print('getting eggs')
        return self._eggs

    def set_eggs(self, eggs):
        print('setting eggs to %s' % eggs)
        self._eggs = eggs

    def delete_eggs(self):
        print('deleting eggs')
        del self._eggs

    eggs = property(get_eggs, set_eggs, delete_eggs)

    @property
    def spam(self):
        print('getting spam')
        return self._spam

    @spam.setter
    def spam(self, spam):
        print('setting spam to %s' % spam)
        self._spam = spam

    @spam.deleter
    def spam(self):
        print('deleting spam')
        del self._spam

spam = Spam()
spam.eggs = 123
spam.eggs
del spam.eggs


#Bare descriptors - for demostration purposes

class Property(object):
    def __init__(self, fget=None, fset=None, fdel=None,
                 doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        # If no specific documentation is available, copy it
        # from the getter
        if fget and not doc:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, instance, cls):
        if instance is None:
            # Redirect class (not instance) properties to
            # self
            return self
        elif self.fget:
            return self.fget(instance)
        else:
            raise AttributeError('unreadable attribute')

    def __set__(self, instance, value):
        if self.fset:
            self.fset(instance, value)
        else:
            raise AttributeError("can't set attribute")

    def __delete__(self, instance):
        if self.fdel:
            self.fdel(instance)
        else:
            raise AttributeError("can't delete attribute")

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel)

#------------------------------------------------------------------------------
#using getattr instead of bare descriptors

class Spam(object):
    def __init__(self):
        self.registry = {}

    def __getattr__(self, key):
        print('Getting %r' % key)
        return self.registry.get(key, 'Undefined')

    def __setattr__(self, key, value):
        if key == 'registry':
            object.__setattr__(self, key, value)
        else:
            print('Setting %r to %r' % (key, value))
            self.registry[key] = value

    def __delattr__(self, key):
        print('Deleting %r' % key)
        del self.registry[key]

#outplut
spam = Spam()

spam.a

spam.a = 1

spam.a

del spam.a


#Singletons!  When you only want one instance, like accessing a database, only one at a time!
import functools


def singleton(cls):
    instances = dict()
    @functools.wraps(cls)
    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton

@singleton
class Spam(object):
    def __init__(self):
        print('Executing init')


a = Spam()
b = Spam()

a is b
a.x = 123
b.x
