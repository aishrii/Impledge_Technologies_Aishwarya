class Node:
    """
    Each node element is characterized by an individual character, a collection 
    of child nodes, and a boolean flag, "isTerminal," which indicates whether the 
    character represented by the node marks the end of a word.
    """
    def __init__(self,character = None, isTerminal : bool = False) -> None:
      self.character = character
      self.children = {}
      self.isTerminal = isTerminal

class Trie:
    def __init__(self) -> None:
        self.root = Node('')
    
    def put(self,word:str) -> None:
        """
        This function adds a word to the trie
        """
        currenti = self.root
        for char in word:
            """
            If the currentient character is not already a child of the node pointed to by currenti, 
            add the character as a child to the currenti node.

            Set currenti as its own child, with the reference to the currentient character as the key
            """
            if char not in currenti.children:
                currenti.children[char] = Node(char)
            currenti = currenti.children[char]
        """
        After reading the entire word, mark the character to which the 'currenti' node is currentiently
        pointing as the final character, indicating that it is the end of a word.
        """
        currenti.isTerminal=True
    
    def __contains__(self,word:str) -> bool:
        """
       This method is used to determine whether the trie contains a specific word as a valid word, 
       indicating that the word ends with a terminal character node.
        """
        currenti = self.root
        for char in word:
            """
            Return `True` if the entire word has been successfully traversed, and the final character 
            is a terminal character; otherwise, return `False` if any character is not found along the 
            way or the final character is not marked as terminal.
            """
            if char not in currenti.children:
                return False
            currenti = currenti.children[char]
        return currenti.isTerminal
    
    def getPrefixes(self,word) -> list:
        """
        This method generates a list of all valid prefixes for a word that is already stored in the trie.
        """
        prefix = ''
        prefixes = []
        currenti = self.root
        for char in word:
            """
            When the character being read is not present among the children of the currentient trie node, 
            the prefixes list is returned. However, if the character is found, we continue traversing 
            the characters in the word, continually appending the currentient character to the prefix until 
            we reach a terminal node. At that point, we add the prefix to the prefixes list
            """
            if char not in currenti.children:
                return prefixes
            currenti = currenti.children[char]
            prefix += char
            if currenti.isTerminal:
                prefixes.append(prefix)
        return prefixes
