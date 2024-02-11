# unittest-extensions

Extension of Python's standard unittest library.

This minimal library aims to simplify behavioural testing with Python's standard
 [`unittest`](https://docs.python.org/3/library/unittest.html) library by separating
 object and data creation from behaviour assertion. Furthermore, it is intended to serve users that want to write really small test functions where what is being asserted is quickly comprehended and easily visible.

 `unittest-extensions` does not have any dependencies, it is solely based on the
 Python standard library.

### Usage
In order to make use of `unittest-extensions`' methods, each `TestCase` must define
a `subject` method. The subject is what you would like to assert in each case.
Moreover, each test method should be decorated with the `args` decorator, whereby the arguments
to your `subject` method are defined. Then, you can use the `assertResult*` methods ([API Reference](api_reference.md))
to assert your subject.  
