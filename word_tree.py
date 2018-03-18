
# Nodes of our tree, they can have children (letters) and be a leaf
# node (the end of a word)
class Node:
    def __init__(self):
        self.letters = {}
        self.leaf = None 
  
    # Gets the node for a letter, makes a node if does not exist
    def getLetter(self, letter):
        if letter not in self.letters:
            self.letters[letter] = Node()

        return self.letters[letter]

    # Adds the letter or sets the leaf attribute to the word
    def addWord(self, word, index):
        if index >= len(word):
            self.leaf = word
            return

        nextNode = self.getLetter(word[index])
        nextNode.addWord(word, index + 1)

    # Performs the tree traveral and adds found words to an array
    def query(self, query, known, index, found):
        if index >= len(query):
            if self.leaf != None:
                found.append(self.leaf)
            return

        letter = query[index]

        if letter == '_': 
            for letter in self.letters:
                if letter not in known:
                    self.letters[letter].query(query, known, index + 1, found)

        if letter in self.letters:
            self.letters[letter].query(query, known, index + 1, found)

# A little redundant, only here to hide the nodes
# from the main part of the program. Made some refactoring easier
class WordTree:
    root = Node()
 
    def add(self, word):
        self.root.addWord(word, 0)

    def query(self, query, known):
        found = []
        self.root.query(query, known, 0, found)
        return found
