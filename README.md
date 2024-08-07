This directory contains everything needed for
**Chapter 14 (The Dream of Bug Fixing)** in
[*Computational Thinking and Problem Solving (CTPS)*](https://profsmith89.github.io/ctps/ctps.html)
by Michael D. Smith.

`analyze.py`: A script that allows us to easily apply an analysis
function to a function (possibly coupled with a function input) that
we'd like to analyze. This tool automates the work we'll do over and
over again in this chapter.

`our_tools.py`: Two utility functions used in `analyze.py`, which
take the name of a function (as a string) and return a string
containing the source code for that function. These functions expect
that the name of the function is the same as the name of the module
in which you can find the function.

`hello.py`: A script containing a hello-world-like function
and two ways to create a string of that function.

`hellu.py`: The same hello-world-like function found in `hello.py`
except this version contains a syntax error (i.e., the string
literal in it isn't terminated correctly).


`contains_dquote.py`: A script containing a simple decision function
that answers yes if its input string contains a double-quote character.

`read_story.py`: A script containing another simple decision function
that answers yes if its input string is under 20 lines long.

`string_bug.py`: A script containing a decision function that assumes
its input string is the source code of a function and analyzes that
code looking for string literals with unmatched double-quote character
deliminters. If it finds one, it returns `"Yes"`.

`yes.py`: A script containing a trivial decision function that always
returns `"Yes"`.

`yep.py`: A script containing a modified version of the `yes` function.
This function includes a backdoor, which when triggered prints the
function's inputs.

`yex.py`: A script containing yet another modified version of the
`yes` function, except this version hides an infinite loop behind
an if-statement.

`yes_on_self.py`: A script of a decision problem involving a function
we haven't written (i.e., we know only its behavior) and self-analysis.

`trouble.py`: A script that inverts the output of the decision
function `yes_on_self` to produce a program that cannot exist.
