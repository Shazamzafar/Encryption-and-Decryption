# Name:      Shazam Zafar
# Date:      October 5 2018
# Program:   Python Encryption and Decryption (M3L4)

# this is my dictionary
My_Dictionary = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A', ' ': ' '}


# Main function it has all the input and other functions
def main():
    user_Line = str(input("Enter some text:")).upper()

    Encrypt_Or_Decrypt = str(input("Do you wish to (D)ecrypt or (E)ncrypt the text:")).upper()

# Function to encrypt a line and return the answer
    if Encrypt_Or_Decrypt == "E":
        encrypted_line = ENCRYPT(user_Line)
        print(encrypted_line)

# Function to decrypt a line and return the answer
    if Encrypt_Or_Decrypt == "D":
        decrypted_line = DECRYPT(user_Line)
        print(decrypted_line)

# ask user what he wants next
    run = str(input("Would you like to enter another string (y)/(n): ")).upper()

    if run == "Y":
        main()
    else:
        print("Program terminated")

# runs for statement to find value of key and put it into a string


def ENCRYPT(user_Line):
    encrypted_line = ''
    for letter in user_Line:
        encrypted_line += My_Dictionary[letter]

    return encrypted_line

# runs for statement to find value of key and put it into a string


def DECRYPT(user_Line):
    decrypted_line = ''
    for letter in user_Line:
        for key, value in My_Dictionary.items():  # gets value key and checks them with the letters
            if value == letter:
                decrypted_line += key

    return decrypted_line


# main function
main()
