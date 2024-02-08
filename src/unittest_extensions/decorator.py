def args(kwargs):
    """
    Decorate test methods to define arguments for your subject.
    """

    def wrapper(method):
        method._subjectKwargs = kwargs
        return method

    return wrapper
