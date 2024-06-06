### chap14/trouble.py
import our_tools
from yes_on_s import yes_on_s   # pretend it exists

def trouble(f):
    if yes_on_s(f, our_tools.grab_f(f)) == "Yes":
        return "No"
    else:
        return "Yes"
