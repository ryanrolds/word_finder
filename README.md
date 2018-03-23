# Word Finder

Super simple program demonstrating trees and recursion. Takes known letters and a word with underscores for whildcards and outputs a list of words that satisfy the wildcards without using the known letters.

> This is PoC for a local high school teacher and his CS class.

## English words

List of words copied from https://github.com/dwyl/english-words.

## Setup

Requires Python 2.7 (probably works on 3.x too).

## Running

    $ python find_words.py

### Example

    $ python find_words.py
    What are your known letter? (e.g. "rstlne")
    a
    What is your query? (underscores are wild)
    wh_t
    Found:
    * whet
    * whit
    What are your known letter? (e.g. "rstlne")
    e
    What is your query? (underscores are wild)
    wh_t
    Found:
    * what
    * whit
    What are your known letter? (e.g. "rstlne")

    What is your query? (underscores are wild)

    ** Recived empty query **
    Exiting...

## Design

The program first loads the list of english words and builds a tree. That tree is then traversed (depth-first). Any matching words are outputted to a list, which is returned when when traversal is completed.
