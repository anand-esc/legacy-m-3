# all_around_test.py

import sys
import cPickle as pickle  # Py3 uses 'pickle' instead of 'cPickle'
import Queue              # Py3 uses 'queue'
import ConfigParser       # Py3 uses 'configparser'

# 1. Old-style class (inherits from nothing, Python 2 specific behavior)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print "I am an animal named %s" % self.name

# 2. New-style class with Python 2 super() syntax
class Dog(Animal, object):
    def __init__(self, name, breed):
        super(Dog, self).__init__(name)
        self.breed = breed

    def speak(self):
        print "Woof! I am %s, a %s" % (self.name, self.breed)

def string_and_type_checks(var):
    # 3. basestring and unicode checks
    if isinstance(var, basestring):
        if isinstance(var, unicode):
            print "It's a unicode string"
        else:
            print "It's a byte string"
    elif type(var) == type(100L): # 4. Long integer literal
        print "It's a long integer"

def dictionary_methods():
    d = {'a': 1, 'b': 2, 'c': 3}
    # 5. has_key and iter methods
    if d.has_key('b'):
        keys = d.iterkeys()
        values = d.itervalues()
        items = d.iteritems()
        return list(keys), list(values), list(items)

def mathematical_and_functional():
    # 6. xrange, integer division, and builtins returning lists
    numbers = xrange(10)
    halves = map(lambda x: x / 2, numbers)
    evens = filter(lambda x: x % 2 == 0, numbers)
    
    # 7. reduce is builtin in Python 2
    sum_evens = reduce(lambda a, b: a + b, evens)
    
    # 8. cmp builtin function
    comparison = cmp(sum_evens, 10)
    
    return halves, evens, sum_evens, comparison

def exception_and_exec():
    # 9. Old-style exception catching
    try:
        # 10. exec as a statement
        exec "x = 10 / 0"
    except ZeroDivisionError, e:
        print "Caught a division error:", e
    except (ValueError, TypeError), e:
        print "Caught a value or type error:", e

def file_io_and_input():
    # 11. file() builtin is Py2 only (alias for open)
    try:
        f = file('dummy.txt', 'w')
        f.write('test')
        f.close()
    except IOError:
        pass
    
    # 12. raw_input is Py2 only
    # Note: disabled for automated testing so it doesn't block
    # user_text = raw_input("Enter something: ")
    # return user_text
    return None

def max_integer():
    # 13. sys.maxint exists in Py2, removed in Py3 (sys.maxsize remains)
    return sys.maxint

def octal_and_inequality():
    # 14. Old octal literals and <> operator
    perms = 0755
    if perms <> 0644:
        return True
    return False

if __name__ == '__main__':
    dog = Dog("Rex", "German Shepherd")
    dog.speak()
    string_and_type_checks(u"Hello")
    dictionary_methods()
    mathematical_and_functional()
    exception_and_exec()
