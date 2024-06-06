### chap14/contains_dquote.py

def contains_dquote(s):
    '''Does s contain a double-quote character?'''
    if '"' in s:
        return "Yes"
    else:
        return "No"

def main():
    # Test function above

    print(f'\nTEST #1: 5 lines from "The Cat in the Hat"')
    s = """We looked!
Then we saw him step in on the mat!
We looked!
And we saw him!
The Cat in the Hat!
"""
    print(contains_dquote(s))

    print('\nTEST #2: lines in `contains_dquote`')
    import inspect
    print(contains_dquote(inspect.getsource(contains_dquote)))

    print('\nTEST #3: empty string')
    print(contains_dquote(''))

    print('\nTEST #4: lines in `read_story`')
    from read_story import read_story
    print(contains_dquote(inspect.getsource(read_story)))

if __name__ == '__main__':
    main()
