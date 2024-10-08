from unittest_extensions import TestCase, args
from unittest_extensions.error import TestError


class TestClass:
    def __init__(self, state_var: int = 1) -> None:
        self.state_var = state_var

    def add(self, a, b):
        return a + b

    def append(self, lst, a) -> None:
        lst.append(a)

    def raises(self, exc) -> None:
        raise exc

    def change_state(self) -> None:
        self.state_var += 1


class TestAdd(TestCase):
    def instance(self) -> TestClass:
        return TestClass()

    def subject(self, a, b):
        return self.instance().add(a, b)

    @args({"a": None, "b": 2})
    def test_add_none_to_int_raises(self):
        self.assertResultRaises(TypeError)

    @args({"a": "somthing", "b": 5})
    def test_add_str_to_int_raises(self):
        self.assertResultRaises(TypeError)

    @args({"a": "adgsa", "b": None})
    def test_add_str_to_none_raises(self):
        self.assertResultRaises(TypeError)

    @args({"a": 2, "b": -6})
    def test_add_int_to_int(self):
        self.assertResult(-4)

    @args({"a": 2.5, "b": 29.0367})
    def test_add_float_to_float(self):
        self.assertResultAlmost(31.5367)

    @args({"a": "1-", "b": "3-"})
    def test_add_str_to_str(self):
        self.assertResult("1-3-")

    @args({"a": 1, "c": 2})
    def test_wrong_kwargs_raises(self):
        self.assertResultRaisesRegex(
            TestError, "Subject received an unexpected keyword argument."
        )

    @args({"a": 1})
    def test_missing_arg_raises(self):
        self.assertResultRaisesRegex(
            TestError, "Subject misses 1 required positional argument."
        )

    @args({"a": 1, "b": 2})
    def test_cachedResult_raises(self):
        with self.assertRaisesRegex(
            TestError, "Cannot call 'cachedResult' before calling 'result'"
        ):
            self.cachedResult()


class TestSubjectMissingRequiredPositionalArguments(TestCase):
    def subject(self, a, b, c, d):
        return 1

    @args({"a": 1, "b": 2})
    def test_raises_test_error(self):
        self.assertResultRaisesRegex(
            TestError, "Subject misses 2 required positional arguments"
        )


class TestAppend(TestCase):
    def instance(self) -> TestClass:
        return TestClass()

    def subject(self, lst, a):
        self.instance().append(lst, a)
        return lst

    @args({"lst": [], "a": None})
    def test_append_to_empty_list(self):
        self.assertResultList([None])

    @args({"lst": ["1"], "a": 2})
    def test_append(self):
        self.assertResultList(["1", 2])

    @args({"lst": [-0.2, 1], "a": 3})
    def test_append_twice(self):
        self.assertResultList([-0.2, 1, 3])
        self.assertResultList([-0.2, 1, 3, 3])

    @args({"lst": None, "a": None})
    def test_append_to_none_raises(self):
        self.assertResultRaises(AttributeError)


class TestRaises(TestCase):
    def instance(self) -> TestClass:
        return TestClass()

    def subject(self, exc):
        self.instance().raises(exc)

    @args({"exc": TypeError})
    def raises_type_error(self):
        self.assertResultRaises(TypeError)

    @args({"exc": Exception})
    def raises_exception(self):
        self.assertResultRaises(Exception)


class TestChangeState(TestCase):
    def setUp(self) -> None:
        self.instance = TestClass()

    def tearDown(self) -> None:
        self.instance = None

    def subject(self):
        self.instance.change_state()
        return self.instance.state_var

    def test_change_state(self):
        self.assertResult(2)

    def test_change_state_twice(self):
        self.assertResult(2)
        self.assertResult(3)

    def test_change_state_cached_result(self):
        self.result()
        self.assertEqual(self.cachedResult(), 2)
        self.result()
        self.assertEqual(self.cachedResult(), 3)

    def test_manually_change_state_cached_result(self):
        self.result()
        self.assertEqual(self.cachedResult(), 2)
        self.instance.state_var += 1
        self.assertEqual(self.cachedResult(), 2)


class TestSubjectKwargs(TestCase):
    def subject(self, a, b):
        return a + b

    @args({"a": 1, "b": 2})
    def test_kwarg_values(self):
        self.assertDictEqual(self.subjectKwargs(), {"a": 1, "b": 2})

    @args({"a": 3, "b": 4})
    def test_different_kwarg_values(self):
        self.assertDictEqual(self.subjectKwargs(), {"a": 3, "b": 4})

    @args({"a": 1, "b": 2})
    def test_kwargs_are_not_mutated(self):
        self.subjectKwargs()["b"] = None
        self.assertDictEqual(self._subjectKwargs, {"a": 1, "b": 2})
        self.assertDictEqual(self.subjectKwargs(), {"a": 1, "b": 2})


class TestSubjectMutableKwargs(TestCase):
    def subject(self, lst):
        return lst

    @args({"lst": [1, 2]})
    def test_mutable_kwargs(self):
        self.subjectKwargs()["lst"].append(3)
        self.assertDictEqual(self._subjectKwargs, {"lst": [1, 2]})


class TestCachedResult(TestCase):
    def subject(self, lst):
        return lst

    @args({"lst": [1, 2]})
    def test_mutate_cached_result(self):
        self.assertResult([1, 2])
        self.cachedResult().append(3)
        self.assertListEqual(self.cachedResult(), [1, 2])


class TestRaiseEmptyException(TestCase):
    class MyError(Exception):
        pass

    def subject(self):
        raise self.MyError()  # exception should be empty, i.e. no args

    def test_reraises_empty_exception(self):
        self.assertResultRaises(self.MyError)


class TestRaiseExceptionWithNonStrArgs(TestCase):
    def subject(self):
        raise KeyError(2)

    def test_reraises_error(self):
        self.assertResultRaises(KeyError)
