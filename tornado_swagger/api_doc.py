def api_doc(api_description: str):
    """
    Decorator to attach an f-string based docstring to the function.
    :param api_description: API description in yaml format
    """
    def decorator(func):
        # Attach the docstring as a function attribute
        func.__apidoc__ = api_description
        return func
    return decorator
