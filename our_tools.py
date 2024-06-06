### chap14/our_tools.py
import importlib
import inspect

def grab_f(fun_name):
    '''A utility function that returns a string containing the
    statements for `fun_name`. Its implementation assumes that
    the function `fun_name` is in a Python script of the same
    name (i.e., `fun_name.py`).'''
    try:
        fun_module = importlib.import_module(fun_name)
        fun = getattr(fun_module, fun_name)
        f = inspect.getsource(fun)
    except SyntaxError:
        # Use the helper function instead
        f = grab_f_with_error(fun_name)
    return f


def grab_f_with_error(fun_name):
    '''A helper function that handles the work of `grab_f`
    when `fun_name` contains a syntax error.'''
    mod_name = fun_name + '.py'
    f = ''
    the_line = ' '

    # What we're searching for
    prefix = f'def {fun_name}('
    prefix_len = len(prefix)

    with open(mod_name) as fin:
        # Search for start of fun_name definition
        while the_line != '':
            the_line = fin.readline()
            if the_line[:prefix_len] == prefix:
                f += the_line
                break

        # Grab entire body of f
        the_line = fin.readline()
        while the_line != '' and the_line[0] == ' ':
            f += the_line
            the_line = fin.readline()

    assert f != '', f"Didn't find {fun_name} in {mod_name}"
    return f
