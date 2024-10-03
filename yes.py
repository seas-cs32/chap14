### chap14/yes.py

def yes(f, s):
    '''An analysis function that no analysis
    and always returns Yes.'''
    return "Yes"


def main():
    # Tests for our `yes` function
    import our_tools

    print('\nTEST #1: short s')
    s = 'world'
    print(yes(our_tools.grab_f('hello'), s))

    print(f"\nTEST #2: long s")
    s = """We looked!
Then we saw him step in on the mat!
We looked!
And we saw him!
The Cat in the Hat!
"""
    print(yes(our_tools.grab_f('hello'), s))

if __name__ == '__main__':
    main()
