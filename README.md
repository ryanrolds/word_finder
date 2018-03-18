# Word Finder

Take a word, including wildcard spaces, outputs a list of words that satisfy the input.

# English words

List of words copied from https://github.com/dwyl/english-words.

# Setup

Requires Python 2.7 (probably works on 3.x).

# Running

    $ python find_words.py

## Example

    $ python find_words.py
    $ > Query: wh_t
    $ > Result: 

# Design

The program first loads the list of english words and builds a tree. That tree is then traversed (depth-first). Any matching words are outputted to a list, which is returned when when traveral is completed.
