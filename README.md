# Prodigy_7_task1
Under the cybersecurity internship at Prodigy Infotech i am providing this code as the solution for task 1.

# Caesar Cipher Program

This Python program implements the **Caesar Cipher**, a simple substitution cipher used for encrypting and decrypting text by shifting characters within the alphabet. It features:

- **Encryption**: Shifts the characters of a plaintext message by a user-specified value to generate a ciphertext.
- **Decryption**: Reverses the process to retrieve the original message from the ciphertext.
- **Interactive CLI**: Users can choose between encryption, decryption, or exiting the program via a menu-driven interface.

## Features
- Handles both uppercase and lowercase letters.
- Preserves non-alphabetic characters (e.g., numbers, spaces, punctuation) without modification.
- Provides user-friendly input prompts for messages and shift values.

## How It Works
1. Characters in the input message are shifted based on their position in the alphabet.
2. A shift value determines how far each character moves.
3. The cipher wraps around the alphabet, ensuring continuity (e.g., shifting `Z` by 1 results in `A`).

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/AKankit47/Caeser_cipher.git
   ```
2. Navigate to the directory:
   ```bash
   cd Prodigy_7_task1
   ```
3. Run the program:
   ```bash
   python Task1.py
   ```
4. Follow the on-screen instructions to encrypt or decrypt messages.

## Example
- Input: `"HELLO"`, Shift: `3`
- Encrypted: `"KHOOR"`

## License
This project is open-source and licensed under the [MIT License](LICENSE).

---

Feel free to adjust the repository name or add additional details specific to your project!
