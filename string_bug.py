### chap14/string_bug.py

# Constant definition so that we can feed `string_bug` to
# itself without violating the restrictions on the form
# of the input it handles.
DQC = '"'

def string_bug(f):
    '''An baby version of `found_bug`, which analyzes a
    function f, passed as a string, for unpaired double-quote
    characters in the definition of a string literal. It's 
    not smart enough to deal with double-quote characters in
    a comment, or instances of themselves in a string literal.'''
    # Create a worklist of the form: non-string, string, ...
    work_list = f.split(DQC)
    items = len(work_list)
    
    # Handle the case of a function f that doesn't
    # contain any string literals
    if items == 1:
        # No double-quote string literals in f
        return "No"

    # Process just the strings in the worklist. String literals
    # defined using a single double-quote character cannot
    # contain a newline character.
    for i in range(1, items, 2):
        if '\n' in work_list[i]:
            return "Yes" 

    # Make sure the last string ended with a double quote, which
    # means the length of work_list should be odd.
    if items & 1 != 1:
        return "Yes"
    
    return "No"

def main():
    # Tests for our `string_bug` function

    # Should print `No`
    print('\nTEST #1')
    hello_str = '''def hello(s):
    print("Hello", s)
'''
    print(string_bug(hello_str))

    # Should print `Yes`
    print('\nTEST #2')
    hellu_str = '''def hellu(s):
    print("Hello, s)
'''
    print(string_bug(hellu_str))

    # Should print `No`
    print('\nTEST #3')
    print(string_bug(''))

if __name__ == '__main__':
    main()
