### chap14/yep.py

def yep(f, s):
    '''A null analysis function with a backdoor to
    some special functionality. Always returns Yes.'''
    if s == 'beVerbose':
        # Print the inputs
        print('*** f ***')
        print(f, end='\n\n')
        print('*** s ***')
        print(s, end='\n\n')

    # Default answer
    return "Yes"


def main():
    # Test function above
    import our_tools

    print(f"\nTEST #1: DON'T trip backdoor")
    s = 'world'
    print(yep(our_tools.grab_f('hello'), s))

    print('\nTEST #2: trip backdoor')
    s = 'beVerbose'
    print(yep(our_tools.grab_f('hello'), s))

if __name__ == '__main__':
    main()
