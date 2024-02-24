`unittest_extensions.TestCase` extends `unittest.TestCase` with the below methods.  

**assertResult(self, value)**  
Fail if the result is unequal to the value as determined by the '==' operator.  
Equivalent to `assertEqual(self.result(), value)`.

**assertResultAlmost(self, value, places=None, delta=None)**  
Fail if the result is unequal to the value as determined by their difference rounded
to the given number of decimal places (default 7) and comparing to zero, or by
comparing that the difference between the two objects is more than the given delta.  
Equivalent to `assertAlmostEqual(self.result(), value, places, delta=delta)`.

**assertResultCount(self, iterable)**  
Assert that the result has the same elements as the iterable without regard to order.  
Equivalent to `assertCountEqual(self.result(), iterable)`.
     
**assertResultDict(self, dct)**  
Assert that the result is equal to dct.  
Equivalent to `assertDictEqual(self.result(), dct)`.

**assertResultFalse(self)**  
Check that the result is false.  
Equivalent to `assertFalse(self.result())`.

**assertResultGreater(self, value)**  
Just like self.assertTrue(self.result() > value), but with a nicer default message.
Equivalent to `assertGreater(self, result(), value)`.

**assertResultGreaterEqual(self, value)**  
Just like self.assertTrue(self.result() >= value), but with a nicer default message.  
Equivalent to `assertGreaterEqual(self.result(), value)`.

**assertResultIn(self, container)**  
Just like self.assertTrue(self.result() in container), but with a nicer default message.  
Equivalent to `assertIn(self.result(), container)`.

**assertResultIs(self, value)**  
Just like self.assertTrue(self.result() is value), but with a nicer default message.  
Equivalent to `assertIs(self.result(), value)`.

**assertResultIsInstance(self, cls)**  
Just like self.assertTrue(self.result() in container), but with a nicer default message.  
Equivalent to `assertIsInstance(self.result(), cls)`.

**assertResultIsNot(self, value)**  
Just like self.assertTrue(self.result() is not value), but with a nicer default message.  
Equivalent to `assertIsNot(self.result(), value)`.

**assertResultIsNotInstance(self, cls)**  
Just like self.assertTrue(self.result() not in container), but with a nicer default message.  
Equivalent to `assertNotIsInstance(self.result(), cls)`.

**assertResultLess(self, value)**  
Just like self.assertTrue(self.result() < value), but with a nicer default message.  
Equivalent to `assertLess(self.result(), value)`.

**assertResultLessEqual(self, value)**  
Just like self.assertTrue(self.result() <= value), but with a nicer default message.  
Equivalent to `assertLessEqual(self.result(), value)`.

**assertResultList(self, lst)**  
Assert that the result is equal to lst.  
Equivalent to `assertListEqual(self.result(), lst)`.

**assertResultNot(self, value)**  
Fail if the result is equal to the value as determined by the '==' operator.  
Equivalent to `assertNotEqual(self.result(), value)`.

**assertResultNotAlmost(self, value, places=None, delta=None)**  
Fail if the result is equal to the value as determined by their difference rounded
to the given number of decimal places (default 7) and comparing to zero, or by
comparing that the difference between the two objects is less than the given delta.  
Equivalent to `assertNotAlmostEqual(self.result(), value)`.

**assertResultNotIn(self, container)**  
Just like self.assertTrue(self.result() not in container), but with a nicer default message.  
Equivalent to `assertNotIn(self.result(), container)`.

**assertResultNotRegex(self, unexpected_regex)**  
Fail the test if the result matches the regular expression.  
Equivalent to `assertNotRegex(self.result(), unexpected_regex)`.

**assertResultRaises(self, expected_exception)**  
Fail unless an exception of class expected_exception is raised by the result. If
a different type of exception is raised, it will not be caught, and the test case
will be deemed to have suffered an error, exactly as for an unexpected exception.  
Equivalent to
```py
with self.assertRaises(expected_exception):
            self.result()
```

**assertResultRaisesRegex(self, expected_exception, expected_regex)**  
Fail unless an exception of class expected_exception is raised by the result and the message matches the regex.  
Equivalent to
```py
with self.assertRaisesRegex(expected_exception, expected_regex):
            self.result()
```

**assertResultRegex(self, expected_regex)**  
Fail the test unless the result matches the regular expression.  
Equivalent to `self.assertRegex(self.result(), expected_regex)`.

**assertResultSet(self, st)**  
Assert that the result is equal to st.  
Equivalent to `self.assertSetEqual(self.result(), st)`.

**assertResultTrue(self)**  
Check that the result is true.  
Equivalent to `self.assertTrue(self.result())`.

**assertResultTuple(self, tpl)**  
Assert that the result is equal to tpl.  
Equivalent to `self.assertTupleEqual(self.result(), tpl)`.

**cachedResult(self) -> Any**  
Return the result of the last `subject` call. Use this function when you want to
assert different attributes of your subject without executing it multiple times.  
  
Raises `unittest_extensions.TestError` if subject has not been called.

**result(self) -> Any**  
Result of the `subject` called with arguments defined by the `args` decorator.