### chap14/analyze.py
import sys
import importlib
import our_tools

def analyze(analysis_name, fun_name, s=None):
    # Grab the analysis function from its module. This code assumes that the
    # `analysis_name` is in `analysis_name.py`.
    analysis_mod = importlib.import_module(analysis_name)
    analysis_fun = getattr(analysis_mod, analysis_name)

    # Grab function to analyze. The utility used assumes that
    # the function `fun_name` is in `fun_name.py`.
    f = our_tools.grab_f(fun_name)

    # Do the analysis
    if s == None:
        ans = analysis_fun(f)
    else:
        ans = analysis_fun(f, s)
    print(ans)


def main():
    if  len(sys.argv) != 3 and len(sys.argv) != 4:
        sys.exit('Usage: python3 analyze.py analysis_fun analyzed_fun [s]')

    analysis_name = sys.argv[1]
    fun_name = sys.argv[2]
    if len(sys.argv) == 4:
        fun_input = sys.argv[3]
    else:
        fun_input = None
    analyze(analysis_name, fun_name, fun_input)

if __name__ == '__main__':
    main()
    