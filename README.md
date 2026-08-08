# Legacy Python 3 - Comprehensive Testbed

This repository provides a comprehensive suite of Python 2.x specific syntax, types, and standard library behaviors. It is designed to thoroughly test the boundaries of a Python 2 to 3 conversion tool, checking if it catches everything from structural syntax changes to nuanced standard library renames.

## Covered Python 2 Features

This repository includes tests for:
1. **Classes**: Old-style classes vs new-style classes (`object` inheritance).
2. **Standard Library Renames**: `cPickle`, `Queue`, `ConfigParser`.
3. **Strings and Types**: `unicode`, `basestring`, `long` integers (`100L`).
4. **Dictionaries**: `.has_key()`, `.iterkeys()`, `.itervalues()`, `.iteritems()`.
5. **Functional Builtins**: `xrange()`, `map()`, `filter()`, `reduce()` (which was moved to `functools` in Py3).
6. **Builtin Functions**: `cmp()`, `file()` as an alias for `open()`.
7. **Syntax and Operators**: `exec` statement, old exception catching `except Exception, e:`, `<>` inequality operator.
8. **Literals**: Old octal literals (`0755`).
9. **Environment**: `sys.maxint` (removed in Py3 in favor of `sys.maxsize`).

This is the ultimate test file for your `Parser & Classifier` and `Verifier` agents!
