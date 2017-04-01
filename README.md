# particle-simulation (not done yet)

Code's pretty gross right now. Need to implement some OO design, refactor, etc.

## Usage

### Run the program

You can either put a file path on the commandline as an argument:

    python rock_drop.py data/1x1_empty_in.txt 

Or pipe input:

    cat data/1x1_empty_in.txt | python rock_drop.py

### Run the tests

Inside the directory holding the .py files:

    python -m unittest discover 1> /dev/null

(that last bit just suppresses the program's normal STDOUT output for a cleaner
test results display)

## Implementation notes

0. The nature of the problem practically insists on multi-threading the gravity
   simulation, since "columns" in the particle field are independent. If I were
   to spend more time on it, that's one thing I'd improve. You could use timeit
   or a timing decorator to measure if there was a performance improvement.

1. I considered mocking or monkey-patching STDIN for the unit testing, but it
   was an unproductive rabbit hole. I settled on a couple methods in the test
   file that read from a file and output to the appropriate data type instead.
   It's a little duplicative of what's going on in the main program, but felt
   less hacky than some of the really strange ways of redirecting STDIN/STDOUT.

2. For transposing the 2D particle field (making the vertical "columns" in the
   simulator become "rows" for the writer), I probably should have used
   numpy.transpose(), but I'd already gone down the route of implementing it
   myself by the time I thought of googling for it. Woops. :-D

3. From my C# days, I thought that the object classes should inherit from an
   abstract base class Thing, which would enforce the implmentation of its
   properties. But, 1) it's unclear how Pythonic this is, and 2) it would break
   Python 2.x compatibility so I left it alone.
