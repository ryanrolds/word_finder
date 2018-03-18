#!/usr/bin/python

import sys
from word_tree import WordTree

wordTree = WordTree();
count = 0

with open('./words_en/words.txt') as words:
    for line in words:
        # Lower case the line, make this thing case insensitive 
        line = line.lower().rstrip('\n\r')

        # The meat and potatos
        wordTree.add(line);

        # Count the number of words/lines we've processed
        count += 1

        # Output something as we process the words file
        if count % 10000 == 0:
            sys.stdout.write('*')
            sys.stdout.flush()
        elif count % 1000 == 0:
            sys.stdout.write('.')
            sys.stdout.flush()
    
    print(' Done')

print('Loaded %d words' % (count))

while True:
    print('What is your query? (underscores are wild)')
    # Gets typed in query the terminal/stdin
    query = sys.stdin.readline().rstrip('\n\r');

    # Provide way to cleanly exit program (avoiding Ctrl+C)
    if len(query) == 0:
        print('** Recived empty query **')
        break;

    # Perform the query and get the matches
    found = wordTree.query(query);

    if len(found) == 0:
        print('** Sorry, no matches **')
        continue

    print('Found: ')
    for word in found:
        print('* %s' % word)

# We are done
print('Exiting...')
exit()
