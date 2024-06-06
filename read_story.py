### chap14/read_story.py

def read_story(s):
    '''Is the story s short enough to read?'''
    lines = s.split('\n')
    if len(lines) < 20:
        return "Yes"
    else:
        return "No"

def main():
    # Test function above

    print(f'\nTEST #1: 21 lines from "The Cat in the Hat"')
    s = """We looked!
Then we saw him step in on the mat!
We looked!
And we saw him!
The Cat in the Hat!
And he said to us,
"Why do you sit there like that?"

"I know it is wet
And the sun is not sunny.
But we can have
Lots of good fun that is funny!"

"I know some good games we could play,"
Said the cat.
"I know some new tricks,"
Said the Cat in the Hat.
"A lot of good tricks.
I will show them to you.
Your mother
Will not mind at all if I do."
"""
    print(read_story(s))

    print('\nTEST #2: lines in `read_story`')
    import inspect
    print(read_story(inspect.getsource(read_story)))

    print('\nTEST #3: empty string')
    print(read_story(''))

if __name__ == '__main__':
    main()
