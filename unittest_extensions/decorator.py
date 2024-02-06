from typing import Callable, TypeVar, TypeAlias

TestClass = TypeVar("TestClass")
TestMethod: TypeAlias = Callable[[TestClass], None]


def args(kwargs) -> TestMethod:
    """
    Decorate test methods to define arguments for your subject.
    """

    def wrapper(method) -> TestMethod:
        method._subjectKwargs = kwargs
        return method

    return wrapper
