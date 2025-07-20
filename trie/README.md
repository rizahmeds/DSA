# Trie Data Structure

## Overview
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
There are various applications of this data structure, such as autocomplete and spellchecker.

## Visual Representation

                    ROOT
                   /    \
                  C      D
                  |      |
                  A      O
                 /|\     |
                T R E    G*
               *  |      
                 /|\     
                D E F    
               *  |      
                  U      
                  |      
                  L*     
    Words stored: CAT*, CAR, CARD*, CARE, CAREFUL*, DOG*
    * = End of word marker

## Detailed Structure
    ROOT
    ├── C
    │   └── A
    │       ├── T (END) → "CAT"
    │       └── R
    │           ├── (END) → "CAR" 
    │           ├── D (END) → "CARD"
    │           └── E
    │               ├── (END) → "CARE"
    │               └── F
    │                   └── U
    │                       └── L (END) → "CAREFUL"
    └── D
        └── O
            ├── G (END) → "DOG"
            └── D
                └── G
                    └── E (END) → "DODGE"

## Key Properties

- Efficient Prefix Operations: Find all words with a given prefix in O(p) time where p is prefix length
- Space Optimization: Common prefixes are stored only once
- Sorted Order: In-order traversal gives lexicographically sorted words
- Fast Lookups: Word search in O(m) time where m is word length

## Common Operations

| Operation | Time Complexity | Description |
|-----------|----------------|-------------|
| Insert | O(m) | Insert word of length m |
| Search | O(m) | Search for word of length m |
| Delete | O(m) | Delete word of length m |
| Prefix Search | O(p + n) | Find all words with prefix of length p, return n words |
| Auto-complete | O(p + n) | Get suggestions for prefix of length p |

## Use Cases
- Autocomplete Systems: Search engines, IDE code completion
- Spell Checkers: Dictionary lookups and suggestions
- IP Routing Tables: Longest prefix matching
- Phone Directories: Efficient contact search
- Word Games: Boggle, Scrabble word validation

## Memory Consideration

- Worst Case: O(ALPHABET_SIZE × N × M) where N is number of words, M is average length
- Best Case: O(Total characters in all unique prefixes)
- Practical: Much better than storing each word separately due to shared prefixes

## When to Use Trie
✅ Good for:

- Large dictionary with many common prefixes
- Need fast prefix-based operations
- Auto-complete functionality
- Pattern matching applications

❌ Not ideal for:

- Small datasets (overhead not worth it)
- No common prefixes between strings
- Memory-constrained environments
- Simple existence checks (hash table is better)
  
## Refrence
https://leetcode.com/problems/implement-trie-prefix-tree/description/
