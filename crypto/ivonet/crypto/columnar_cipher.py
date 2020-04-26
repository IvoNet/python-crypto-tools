#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__doc__="""

# Columnar Cipher

The Columnar Cipher is a type of transposition cipher.

1. Get Keyword
2. If your keyword is Zebras, that is 6 letters. 
   You would write 632415 because Z is the 6th highest letter in the word and E is the 3rd highest letter and so on
3. Then message under the numbers in rows of 6, because Zebra is a 6 letter word.
4. Write out 123456. Under the number write the letters from each column that 
   match the numbers in the original line of numbers.

    F A N C Y   <- the key (doubles removed)
    3 1 4 2 5   <- order in alphabet 1 indexed
    m e e t m
    e a t m e
    x t m i d
    n i g h t
    
      ^ 
      ciphertext is read collumn-wise, starting with 1
    
    So thei example would be 
    
Example 
The key for the columnar transposition cipher is a keyword e.g. GERMAN. 
The row length that is used is the same as the length of the keyword. To encrypt a piece of text, e.g.

    defend the east wall of the castle

we write it out in a special way in a number of rows (the keyword here is GERMAN):

G E R M A N
d e f e n d
t h e e a s
t w a l l o
f t h e c a
s t l e x x
In the above example, the plaintext has been padded so that it neatly fits in a rectangle. 
This is known as a regular columnar transposition. 
An irregular columnar transposition leaves these characters blank, 
though this makes decryption slightly more difficult. The columns are now reordered 
such that the letters in the key word are ordered alphabetically.

A E G M N R
n e d e d f
a h t e s e
l w t l o a
c t f e a h
x t s e x l
The ciphertext is read off along the columns:

   nalcxehwttdttfseeleedsoaxfeahl

"""


if __name__ == '__main__':
    print(__doc__)
    print("Not yet further implemented")

