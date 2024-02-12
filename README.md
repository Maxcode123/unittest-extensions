# **unittest-extensions**
Extension of Python's standard unittest library  

# Introduction
If testing is not easy, you will not do it.  
If you do not test, bad things will happen.  
Thus, if testing is not easy, bad things will happen.  

This minimal library aims to simplify behavioural testing with Python's standard
 [`unittest`](https://docs.python.org/3/library/unittest.html) library by separating
 object and data creation from behaviour assertion. Furthermore, it is intended to serve users that want to write really small test functions where what is being asserted is quickly comprehended and easily visible.  

 `unittest-extensions` does not have any dependencies, it is solely based on the
 Python standard library and mainly inspired by Ruby's [`RSpec`](https://rspec.info/) framework.  

# Documentation
This project is documented at:  
https://maxcode123.github.io/unittest-extensions/


# Installation
```
pip install unittest-extensions
```
# Usage
Suppose you have some code that looks like this:

```py
from dataclasses import dataclass

@dataclass
class User:
    name: str
    surname: str

    def is_relative_to(self, user: "User") -> bool:
        return self.surname.casefold() == user.surname.casefold()
```
This is a dummy example, meaning that how exactly the User and their methods are implemented does not really matter; what we actually care about here is how to test this code given the above implementation.   
Say we'd like to test the `is_relative_to` method with pairs of User names and surnames using the standard `unittest` library.
So, here's an example of how we could do that as simply as possible:
## unittest

```py
from unittest import main, TestCase


class TestIsRelativeToSameName(TestCase):
    def test_same_name(self):
        user1 = User("Niklas", "Strindberg")
        user2 = User("Niklas", "Ibsen")
        self.assertFalse(user1.is_relative_to(user2))

    def test_same_empty_name(self):
        user1 = User("", "Stringberg")
        user2 = User("", "Ibsen")
        self.assertFalse(user1.is_relative_to(user2))


class TestIsRelativeToSameSurname(TestCase):
    def test_same_surname(self):
        user1 = User("August", "Nietzsche")
        user2 = User("Henrik", "Nietzsche")
        self.assertTrue(user1.is_relative_to(user2))

    def test_same_empty_surname(self):
        user1 = User("August", "")
        user2 = User("Henrik", "")
        self.assertTrue(user1.is_relative_to(user2))

    def test_same_surname_case_sensitive(self):
        user1 = User("August", "NiEtZsChE")
        user2 = User("Henrik", "nietzsche")
        self.assertTrue(user1.is_relative_to(user2))

    def test_surname1_contains_surname2(self):
        user1 = User("August", "Solzenietzsche")
        user2 = User("Henrik", "Nietzsche")
        self.assertFalse(user1.is_relative_to(user2))


if __name__ == "__main__":
    main()
```

The cases we check here are rather limited but still there is some duplication in our code; we use many lines to create our User subjects. Of course we can avoid that
by creating custom assertion methods that receive only the parameters that change
between tests, but that's why a testing library is here for.  
Here's how we could write the above code with `unittest-extensions`:

## unittest-extensions
```py
from unittest import main

from unittest_extensions import TestCase, args


class TestIsRelativeToSameName(TestCase):
    def subject(self, name1, name2):
        return User(name1, "Strindberg").is_relative_to(User(name2, "Ibsen"))

    @args({"name1": "Niklas", "name2": "Niklas"})
    def test_same_name(self):
        self.assertResultFalse()

    @args({"name1": "", "name2": ""})
    def test_same_empty_name(self):
        self.assertResultFalse()


class TestIsRelativeToSameSurname(TestCase):
    def subject(self, surname1, surname2):
        return User("August", surname1).is_relative_to(User("Henrik", surname2))

    @args({"surname1": "Nietzsche", "surname2": "Nietzsche"})
    def test_same_surname(self):
        self.assertResultTrue()

    @args({"surname1": "", "surname2": ""})
    def test_same_empty_surname(self):
        self.assertResultTrue()

    @args({"surname1": "NiEtZsChE", "surname2": "Nietzsche"})
    def test_same_surname_case_sensitive(self):
        self.assertResultTrue()

    @args({"surname1": "Nietzsche", "surname2": "Solszenietzsche"})
    def test_surname2_contains_surname1(self):
        self.assertResultFalse()


if __name__ == "__main__":
    main()
```

The number of lines is still the same, but the testing code has become clearer:  
1. The subject of our assertions in each test case is documented in the `subject` method
2. Each test method contains only information we care about, i.e. the input data (names/surnames) we test and the result of the assertion (true/false).

# License
[MIT License](https://opensource.org/license/mit/)