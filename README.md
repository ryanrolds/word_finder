# Word Finder

Super simple program demonstrating trees and recursion. Takes a word with underscores for whildcards and outputs a list of words that satisfy the wildcards.

## English words

List of words copied from https://github.com/dwyl/english-words.

## Setup

Requires Python 2.7 (probably works on 3.x too).

## Running

    $ python find_words.py

### Example

    $ python find_words.py
    What is your query? (underscores are wild)
    wh_t
    Found:
    * what
    * whet
    * whit
    What is your query? (underscores are wild)

    ** Recived empty query **
    Exiting...

## Design

The program first loads the list of english words and builds a tree. That tree is then traversed (depth-first). Any matching words are outputted to a list, which is returned when when traversal is completed.
