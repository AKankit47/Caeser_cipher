# Caesar Cipher Implementation

def caesar_cipher(text, shift, mode):
    if mode == "decrypt":
        shift = -shift

    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            new_char = chr((ord(char) - offset + shift) % 26 + offset)
            result += new_char
        else:
            result += char

    return result


def main():
    print("Caesar Cipher Program")
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher(message, shift, "encrypt")
            print("Encrypted message:", encrypted_message)

        elif choice == "2":
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher(message, shift, "decrypt")
            print("Decrypted message:", decrypted_message)

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


'''
Example:
Let’s shift the letter 'B' by 3:

1. 'B' is alphabetic, and it’s uppercase, so offset = 65.
2. ord('B') = 66. Subtract offset: 66 - 65 = 1 (normalized index).
3. Add the shift: 1 + 3 = 4.
4. Wrap around with % 26: 4 % 26 = 4.
5. Add the offset back: 4 + 65 = 69.
6. Convert back to a character: chr(69) = 'E'.
7. The letter 'B' shifts to 'E'.
'''
