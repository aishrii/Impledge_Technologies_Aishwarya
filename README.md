# Problem Statement
To identify and display the longest compounded word and the second longest compounded word from the input files (Input_01.txt and Input_02.txt) containing alphabetically sorted words list. A compounded word is a word that is formed by concatenating shorter words.
# Approach
My first approach was to use a priority queue to efficiently store and retrieve the longest compounded word. And implement a recursive depth-first search (DFS) algorithm to traverse the tree of compounded words and add each new compounded word to the priority queue. But this solution was not very efficient as it did not work for larger inputs. In order to make the solution more optimised I then used ***Trie*** data structure.


The approach of my solution is that first, the word 'cat' is inserted into the trie. Then, the word 'cats' is added, and now we check for it and find that it has the prefix 'cat,' resulting in the addition of the pair ('cats', 's') to the processing queue. Now subsequently, the word 'catsdogcats' is inserted, revealing two prefixes, 'cat' and 'cats.' Therefore we add the two pairs ('catsdogcats', 'sdogcats') and ('catsdogcats', 'dogcats') to the queue, corresponding to the prefixes 'cat' and 'cats,' respectively. We continue this process and build the trie.


After building the trie and the queue, then we start processing the queue by popping a pair from the beginning. We check whether the suffix is a valid or compound word. If it’s a valid word and the original word is the longest up to now, we store the result. Otherwise we discard the pair. The suffix may be a compound word itself, so we check if the it has any prefixes. If it does, then we apply the above procedure by adding the original word and the new suffix to the queue. If the suffix of the original popped pair is neither a valid word nor has a prefix, we simply discard that pair.
