# File: Project2.py
# Student:  Yejin Hong
# UT EID:   yh25386
# Course Name: CS303E
# 
# Date Created: 04/05/24
# Description of Program: 

import random

# A global constant defining the alphabet.
LCLETTERS = "abcdefghijklmnopqrstuvwxyz"

# You are welcome to use the following two auxiliary functions, or
# define your own. You don't need to understand this code at this
# point in the semester.

def isLegalKey(key):
    # A key is legal if it has length 26 and contains all letters
    # from LCLETTERS.
    return (len(key) == 26 and all([ch in key for ch in LCLETTERS]))

def makeRandomKey():
    # A legal random key is a permutation of LCLETTERS.
    lst = list(LCLETTERS)  # Turn string into list of letters
    random.shuffle(lst)    # Shuffle the list randomly
    return ''.join(lst)    # Assemble them back into a string

class SubstitutionCipher:
    def __init__(self, key=makeRandomKey()):
        """Create an instance of the cipher with stored key, which
        defaults to random."""
        if isLegalKey(key):
            self.key = key
        else:
            raise ValueError("Invalid key provided.")

    def getKey(self):
        """Getter for the stored key."""
        return self.key

    def setKey(self, newKey):
        """Setter for the stored key.  Check that it's a legal
        key."""
        if isLegalKey(newKey):
            self.key = newKey
        else:
            raise ValueError("Invalid key provided.")

    def encryptText(self, plaintext):
        """Return the plaintext encrypted with respect to the stored key."""
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                if char.islower():
                    index = LCLETTERS.index(char)
                    ciphertext += self.key[index]
                else:
                    index = LCLETTERS.index(char.lower())
                    ciphertext += self.key[index].upper()
            else:
                ciphertext += char
        return ciphertext

    def decryptText(self, ciphertext):
        """Return the ciphertext decrypted with respect to the stored
        key."""
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                if char.islower():
                    index = self.key.index(char)
                    plaintext += LCLETTERS[index]
                else:
                    index = self.key.index(char.lower())
                    plaintext += LCLETTERS[index].upper()
            else:
                plaintext += char
        return plaintext

def main():
    """ This implements the top level command loop.  It
    creates an instance of the SubstitutionCipher class and allows the user
    to invoke within a loop the following commands: help, getKey, changeKey,
    encrypt, decrypt, quit."""
    cipher = SubstitutionCipher()

    while True:
        command = input("Enter a command (help, getKey, changeKey, encrypt, decrypt, quit): ").lower()

        if command == "help":
            print("The following commands are available:")
            print("  help: show this message;")
            print("  getkey: display the current key;")
            print("  changekey: the user may provide a new legal key or enter ")
            print("      random to generate a key randomly, or quit to end this ")
            print("      command and leave the key unchanged;")
            print("  encrypt: receive a text from the user, encrypt it using the ")
            print("      current key, and print the result;")
            print("  decrypt: receive a text from the user, decrypt it using the ")
            print("      current key, and print the result;")
            print("  quit: exit the command loop;")
            print("  anything else is an error.")

        elif command == "getkey":
            print("  Current cipher key:", cipher.getKey())

        elif command == "changekey":
            while True:
                new_key = input("  Enter a valid cipher key, 'random' for a random key, or 'quit' to quit: ").lower()
                if new_key == "quit":
                    break
                elif new_key == "random":
                    cipher.setKey(makeRandomKey())
                    print("    New cipher key:", cipher.getKey())
                    break
                elif isLegalKey(new_key):
                    cipher.setKey(new_key)
                    print("    New cipher key:", cipher.getKey())
                    break
                else:
                    print("    Illegal key entered. Try again!")

        elif command == "encrypt":
            text = input("  Enter a text to encrypt: ")
            print("    The encrypted text is:", cipher.encryptText(text))

        elif command == "decrypt":
            text = input("  Enter a text to decrypt: ")
            print("    The decrypted text is:", cipher.decryptText(text))

        elif command == "quit":
            print("Thanks for visiting!")
            break

        else:
            print("Command not recognized. Try again!")

if __name__ == "__main__":
    main()
