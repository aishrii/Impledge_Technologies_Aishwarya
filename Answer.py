import Trie as T
from collections import deque
import time

class answer:
    def __init__(self) -> None:
      self.trie = T.Trie()
      self.queue = deque()

    def bTrie(self,filePath : str = None) -> None:
        """
        Builds the trie. 
        """
        try:
            with open(filePath, mode = 'r') as f:
                for line in f:
                    """
                    Remove the newline character from the end of each letter and check if there 
                    are any prefixes of the letter within the trie. If prefixes are discovered, 
                    split the letter into its corresponding suffix and add the pair (letter, suffix) 
                    to the deque. Lastly, insert the letter into the trie.
                    """
                    letter = line.rstrip('\n')
                    prefixes = self.trie.getPrefixes(letter)
                    for prefix in prefixes:
                        self.queue.append((letter, letter[len(prefix):]))
                    self.trie.insert(letter)
        except:
            print("There was some error with the file!")
            exit(0)
    
    def getLCL(self) -> tuple:
        """
        Retrieve the two highest compound letters from the trie and return them as a tuple, 
        where the first element is the highest letter, and the second element is the second highest letter.
        """
        highest_letter = ''
        highest_length = 0
        second_highest = ''
        #Iterate the dequeue while it is not empty
        while self.queue:
            #Pop out the first tuple from the front side of the dequeue
            #In this way only the compound letters are taken into account
            letter, suffix = self.queue.popleft()
            """
            When a letter's suffix is an existing valid letter within the trie, 
            and the letter's length exceeds the length of the previous highest 
            letter, update both the second highest and highest letters, and keep 
            a record of the updated highest letter's length.
            """
            if suffix in self.trie and len(letter) > highest_length:
                second_highest = highest_letter
                highest_letter = letter
                highest_length = len(letter)
            else:
                """
                If prefixes are identified, the letter is separated into its main part 
                and the remaining suffix, and then the pair (letter, suffix) is added to the deque.
                """ 
                prefixes = self.trie.getPrefixes(suffix)
                for prefix in prefixes:
                    self.queue.append((letter, suffix[len(prefix):]))

        return (highest_letter,second_highest)

if __name__ == "__main__":
    sol = answer()
    start = time.time()
    sol.bTrie("Input_02.txt")
    first,second = sol.getLCL()
    end = time.time()
    print("highest Compound letter:",first)
    print("Second highest Compound letter:",second)
    print("Time taken: ",str(end - start), "seconds")
