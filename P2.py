def encrypt(text, shift):
    """
    Encrypt text using Caesar Cipher.
    """

    encrypted_text = ""

    for character in text:

        if character.isupper():
            encrypted_text += chr(
                (ord(character) - ord('A') + shift) % 26 + ord('A')
            )

        elif character.islower():
            encrypted_text += chr(
                (ord(character) - ord('a') + shift) % 26 + ord('a')
            )

        else:
            # Keep spaces, numbers and special characters unchanged
            encrypted_text += character

    return encrypted_text


def decrypt(text, shift):
    """
    Decrypt Caesar Cipher text.
    """

    return encrypt(text, -shift)


def main():

    print("=" * 55)
    print("          BASIC ENCRYPTION & DECRYPTION")
    print("                CAESAR CIPHER")
    print("=" * 55)

    text = input("\nEnter the text: ")

    # Get valid shift key
    while True:
        try:
            shift = int(input("Enter shift key (1-25): "))

            if 1 <= shift <= 25:
                break

            print("Please enter a shift between 1 and 25.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Encryption
    encrypted_text = encrypt(text, shift)

    # Decryption
    decrypted_text = decrypt(encrypted_text, shift)

    print("\n" + "-" * 55)
    print("RESULT")
    print("-" * 55)

    print("Original Text  :", text)
    print("Shift Key      :", shift)
    print("Encrypted Text :", encrypted_text)
    print("Decrypted Text :", decrypted_text)

    print("-" * 55)

    if decrypted_text == text:
        print("Verification    : SUCCESS")
        print("The encrypted text was successfully decrypted.")

    print("=" * 55)


if __name__ == "__main__":
    main()