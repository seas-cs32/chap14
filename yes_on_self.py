### chap14/yes_on_self.py
import our_tools
from yes_on_s import yes_on_s   # pretend it exists

def yes_on_self(f):
    return yes_on_s(f, our_tools.grab_f(f))
