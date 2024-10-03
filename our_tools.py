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
        fun_object = getattr(fun_module, fun_name)
        fun_src = inspect.getsource(fun_object)
    except SyntaxError:
        # Use the helper function instead
        fun_src = grab_f_with_error(fun_name)
    return fun_src


def grab_f_with_error(fun_name):
    '''A helper function that handles the work of `grab_f`
    when `fun_name` contains a syntax error.'''
    mod_name = fun_name + '.py'
    fun_src = ''
    the_line = ' '

    # What we're searching for
    prefix = f'def {fun_name}('
    prefix_len = len(prefix)

    with open(mod_name) as fin:
        # Search for start of fun_name definition
        while the_line != '':
            the_line = fin.readline()
            if the_line[:prefix_len] == prefix:
                fun_src += the_line
                break

        # Grab entire body of f
        the_line = fin.readline()
        while the_line != '' and the_line[0] == ' ':
            fun_src += the_line
            the_line = fin.readline()

    assert fun_src != '', f"Didn't find {fun_name} in {mod_name}"
    return fun_src
