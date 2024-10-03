### chap14/hello.py
import inspect

def hello(s):
    print("Hello", s)

hello_str = '''def hello(s):
    print("Hello", s)
'''

hello_src = inspect.getsource(hello)

def main():
    # Tests for our `yes` function
    
    print('\nTEST #1')
    hello("world")

    print('\nTEST #2')
    print(hello_str)

    print('\nTEST #3')
    print(hello_src)

if __name__ == '__main__':
    main()
