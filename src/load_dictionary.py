"""Load a test file as a list.

Arguments:
-text file name (and directory path, if needed)

Exceptions:
-IOError if file name not found.

Returns:
-A list of all words in a text file in lower case.

Requires-import sys

"""
import sys


def load(filename):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(
            "{}\nError opening {}. Terminating program.".format(e, filename),
            file=sys.stderr,
        )
        sys.exit(1)