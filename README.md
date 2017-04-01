# particle-simulation

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

1. I considered mocking or monkey-patching STDIN for the unit testing, but it
   was an unproductive rabbit hole. I settled on a couple methods in the test
   file that read from a file and output to the appropriate data type instead.
   It's a little duplicative of what's going on in the main program, but felt
   less hacky than some of the really strange ways of redirecting STDIN.


