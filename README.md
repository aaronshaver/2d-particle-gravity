# rock_drop (not done yet!!!!!)

## Usage

### Run the program

You can either put a file path on the commandline as an argument:

    python rock_drop.py data/3x7_your_file_in.txt 

Or pipe input:

    cat data/3x7_your_file_in.txt | python rock_drop.py

It works in Python 2.7.12+ and 3.5.2+.

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
   simulator become "rows" for the writer -- and the reverse situation for
   input), I probably should have used
   numpy.transpose(), but I'd already gone down the route of implementing it
   myself by the time I thought of googling for it. Woops. :-D The one good
   thing to come out of it is that this reduces dependencies.

3. From my C# days, I thought that the object classes should inherit from an
   abstract base class Thing, which would enforce the implmentation of its
   properties. But, 1) it's unclear how Pythonic this is, and 2) it would break
   Python 2.x compatibility so I left it alone.

4. It wasn't perfectly clear from the problem description whether rocks could
   start out underneath tables. If they can't, there might be an opportunity
   for optimization (by ignoring everything underneath a table). I chose to
   make the input maximally flexible, but if this were a work assignment, I'd
   push for clarity in what the client wants/needs.
