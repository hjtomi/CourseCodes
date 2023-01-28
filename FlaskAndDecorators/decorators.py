def logging_decorator(function):
    def inner_function(*args, **kwargs):
        returned_value = function(*args, **kwargs)
        arg_str = ""
        for arg in args:
            if type(arg) != str:
                arg_str += f", {arg}"
            else:
                arg_str += f'", {arg}"'

        kwarg_str = ""
        for key, value in kwargs.items():
            if type(value) != str:
                kwarg_str += f', {key}={value}'
            else:
                kwarg_str += f', {key}="{value}"'

        print(f"You called: {function.__name__}({arg_str.removeprefix(', ')}{kwarg_str.removeprefix(', ')})")
        print(f"It returned: {returned_value}")

    return inner_function


@logging_decorator
def test_function(n1, n2, operation):
    if operation == "+":
        return n1 + n2


test_function(1, 2, operation="+")


@logging_decorator
def word_builder(letter_list):
    return ''.join(letter_list)


word_builder(["a", "p", "p", "l", "e"])
