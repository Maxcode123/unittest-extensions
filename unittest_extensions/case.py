from unittest import TestCase as BaseTestCase
from typing import Any
from abc import abstractmethod
from warnings import warn

from unittest_extensions.error import TestError


class TestCase(BaseTestCase):
    """
    Extends unittest.TestCase with methods that assert the result of a defined
    `subject` method.

    ```
    from unittest_extensions import TestCase, args


    class MyClass:
        def my_method(self, a, b):
            return a + b


    class TestMyMethod(TestCase):
        def subject(self, a, b):
            return MyClass().my_method(a, b)

        @args({"a": None, "b": 2})
        def test_none_plus_int(self):
            self.assertResultRaises(TypeError)

        @args({"a": 10, "b": 22.1})
        def test_int_plus_float(self):
            self.assertResult(32.1)
    ```
    """

    @abstractmethod
    def subject(self, **kwargs) -> Any: ...

    def result(self) -> Any:
        """
        Result of the `subject` called with arguments defined by the `args`
        decorator.
        """
        try:
            return self.subject(**self._subjectKwargs)
        except TypeError as e:
            msg = e.args[0]
            if "unexpected keyword argument" in msg:
                raise TestError(
                    "Subject received "
                    + msg.split("subject() got ")[1]
                    + ". Did you decorate a test method with the wrong 'args'?"
                )
            elif "required positional argument" in msg:
                raise TestError(
                    "Subject misses "
                    + msg.split("subject() missing ")[1]
                    + ". Did you decorate all test methods with 'args'?"
                )
            raise e

    def assertResult(self, value):
        """
        Fail if the result is unequal to the value as determined by the '=='
        operator.
        """
        self.assertEqual(self.result(), value)

    def assertResultNot(self, value):
        """
        Fail if the result is equal to the value as determined by the '=='
        operator.
        """
        self.assertNotEqual(self.result(), value)

    def assertResultTrue(self):
        """
        Check that the result is true.
        """
        self.assertTrue(self.result())

    def assertResultFalse(self):
        """
        Check that the result is false.
        """
        self.assertFalse(self.result())

    def assertResultIs(self, value):
        """
        Just like self.assertTrue(self.result() is value), but with a
        nicer default message.
        """
        self.assertIs(self.result(), value)

    def assertResultIsNot(self, value):
        """
        Just like self.assertTrue(self.result() is not value), but with a
        nicer default message.
        """
        self.assertIsNot(self.result(), value)

    def assertResultIn(self, container):
        """
        Just like self.assertTrue(self.result() in container), but with a
        nicer default message.
        """
        self.assertIn(self.result(), container)

    def assertResultNotIn(self, container):
        """
        Just like self.assertTrue(self.result() not in container), but
        with a nicer default message.
        """
        self.assertNotIn(self.result(), container)

    def assertResultIsInstance(self, cls):
        """
        Just like self.assertTrue(self.result() in container), but with a
        nicer default message.
        """
        self.assertIsInstance(self.result(), cls)

    def assertResultIsNotInstance(self, cls):
        """
        Just like self.assertTrue(self.result() not in container), but with a
        nicer default message.
        """
        self.assertNotIsInstance(self.result(), cls)

    def assertResultRaises(self, expected_exception):
        """
        Fail unless an exception of class expected_exception is raised by the
        result. If a different type of exception is raised, it will not be
        caught, and the test case will be deemed to have suffered an error,
        exactly as for an unexpected exception.
        """
        with self.assertRaises(expected_exception):
            self.result()

    def assertResultAlmost(self, value):
        self.assertAlmostEqual(self.result(), value)

    def assertResultNotAlmost(self, value):
        self.assertNotAlmostEqual(self.result(), value)

    def assertResultGreater(self, value):
        self.assertGreater(self.result(), value)

    def assertResultGreaterEqual(self, value):
        self.assertGreaterEqual(self.result(), value)

    def assertResultLess(self, value):
        self.assertLess(self.result(), value)

    def assertResultLessEqual(self, value):
        self.assertLessEqual(self.result(), value)

    def assertResultRegex(self, expected_regex):
        self.assertRegex(self.result(), expected_regex)

    def assertResultNotRegex(self, unexpected_regex):
        self.assertNotRegex(self.result(), unexpected_regex)

    def assertResultCount(self, iterable):
        self.assertCountEqual(self.result(), iterable)

    def assertResultSequence(self, sequence):
        self.assertSequenceEqual(self.result(), sequence)

    def assertResultList(self, lst):
        self.assertListEqual(self.result(), lst)

    def assertResultTuple(self, tpl):
        self.assertTupleEqual(self.result(), tpl)

    def assertResultSet(self, st):
        self.assertSetEqual(self.result(), st)

    def assertResultDict(self, dct):
        self.assertDictEqual(self.result(), dct)

    def _callTestMethod(self, method):
        if hasattr(method, "_subjectKwargs"):
            self._subjectKwargs = method._subjectKwargs
        else:
            self._subjectKwargs = {}

        if method() is not None:
            warn(
                f"It is deprecated to return a value that is not None from a "
                f"test case ({method})",
                DeprecationWarning,
                stacklevel=3,
            )
        self._subjectKwargs = {}
