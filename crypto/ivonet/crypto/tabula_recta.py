from ivonet.collection.list import rotate
from ivonet.string.alphabet import alphabet, alphabet_loc

__doc__ = """
https://nl.wikipedia.org/wiki/Vigen%C3%A8recijfer
This program generates a cryptographic table in the style of a tabula recta.

Vigenère-vercijfering

"""


def default_tabula_recta():
    print("""         | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    -------------------------------------------------------------
       A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
       B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
       C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
       D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
       E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
       F | F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
       G | G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
       H | H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
       I | I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
       J | J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
       K | K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
       L | L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
       M | M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
       N | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
       O | O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
       P | P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
       Q | Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
       R | R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
       S | S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
       T | T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
       U | U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
       V | V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
       W | W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
       X | X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
       Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
       Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y""")
    print()


def tabula_recta(text, key) -> str:
    """Encodes text based on the provided key according to the Vingenere Cypher"""
    k = key.strip().upper()
    txt = text.strip().upper()
    alpha = list(alphabet(True))
    while len(k) < len(txt):
        k += key.strip().upper()
    answer = ""
    for i, x in enumerate(txt):
        cipher = rotate(alpha, alphabet_loc(x, 0))
        loc = alphabet_loc(k[i], 0)
        answer += cipher[loc]
    return answer


def vingenere_cypher(text, key) -> str:
    """Encodes text based on the provided key according to the Vingenere Cypher"""
    return tabula_recta(text, key)


def tabula_recta_decode(text, key) -> str:
    """Decodes to original text based on the provided cyphered text and the provided key"""
    k = key.strip().upper()
    txt = text.strip().upper()
    alpha = list(alphabet(True))
    while len(k) < len(txt):
        k += key.strip().upper()
    answer = ""
    for i, x in enumerate(txt):
        pos = alpha.index(k[i])
        for idx in range(0, 25):
            cypher = rotate(alpha, idx)
            if cypher[pos] == x:
                answer += alpha[idx]
                break
    return answer


def vingenere_cyper_decode(ciphered, key):
    """Decodes to original text based on the provided cyphered text and the provided key"""
    return tabula_recta_decode(ciphered, key)


if __name__ == '__main__':
    print(tabula_recta_decode("QQAMIAIII", "vingenere"))
    # default_tabula_recta()
