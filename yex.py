### chap14/yex.py

def yex(f, s):
    '''A null analysis function with a runtime error
    in its backdoor. Meant to always return Yes.'''
    if s != 'beQuick':
        # Waste some time so it looks like we're
        # doing some analysis.
        cnt = 0
        while cnt < 1000000:
            cnt -= 1

    # Default answer
    return "Yes"


def main():
    # Tests for our `yex` function
    import our_tools

    # Should print `Yes`
    print("\nTEST #1: DON'T trip backdoor")
    s = 'beQuick'
    print(yex(our_tools.grab_f('hello'), s))

    # Should get caught in an infinite loop
    print(f"\nTEST #2: trip backdoor")
    s = 'world'
    print(yex(our_tools.grab_f('hello'), s))

if __name__ == '__main__':
    main()
