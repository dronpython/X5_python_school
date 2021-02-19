class ContractError(Exception):
    """We use this error when someone breaks our contract."""
    pass


#: Special value, that indicates that validation for this type is not required.
Any = object


def contract(arg_types=None, return_type=None, raises=None):

    def decorator(func):

        def wrapped(*func_args):
            if arg_types:
                for arg, types in zip(func_args, arg_types):
                    if not isinstance(arg, types):
                        raise ContractError('Value is incorrect')
            try:
                result = func(*func_args)
            except Exception as e:
                if type(e) in raises:
                    raise
                else:
                    raise ContractError('Value is incorrect') from e

            if return_type:
                if not isinstance(result, return_type):
                    raise ContractError('Value is incorrect')

            return func(*func_args)
        return wrapped
    return decorator


@contract(arg_types=(int, Any), return_type=float, raises=(ZeroDivisionError,))
def some_func(first_arg, second_arg):
    return first_arg / second_arg


print(some_func(2, 1))
