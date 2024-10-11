import functools


def args(*args, **kwargs):
    """
    Decorate test methods to define positional and/or keyword arguments for your
    `subject` method.

    Examples:
        >>> from unittest_extensions import TestCase, args

        >>> class MyClass:
        ...     def my_method(self, a, b):
        ...         return a + b

        >>> class TestMyMethod(TestCase):
        ...     def subject(self, a, b):
        ...         return MyClass().my_method(a, b)

        ...     @args(None, 2)
        ...     def test_none_plus_int(self):
        ...         self.assertResultRaises(TypeError)

        ...     @args(a=10, b=22.1)
        ...     def test_int_plus_float(self):
        ...         self.assertResult(32.1)

        ...     @args("1", b="2")
        ...     def test_str_plus_str(self):
        ...         self.assertResult("12")
    """

    def args_decorator(test_method):
        test_method._subjectArgs = args
        test_method._subjectKwargs = kwargs

        @functools.wraps(test_method)
        def wrapped_test_method(*_args, **_kwargs):
            return test_method(*_args, **_kwargs)

        return wrapped_test_method

    return args_decorator
