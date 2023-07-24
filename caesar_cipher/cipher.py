import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    print(art.logo)

    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if direction == "encode":
            encrypt(text, shift)
        elif direction == "decode":
            decrypt(text, shift)
        
        restart_program = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
        
        if restart_program == "no":
            break

# Encrypt the text message by shifting each letter to the right
def encrypt(plain_text, shift_amount):
    # Default encrypted text
    encrypted_text = ""

    # Iterate through each letter of the text
    for letter in plain_text:
        # Add space when letter is blank
        if letter == " ":
            encrypted_text += " "
        else:
            # Record the index of the shifted letter
            shifted_index = alphabet.index(letter) + shift_amount
            # If the shift exceeds the last alphabet, the index will reset from the first
            if shifted_index > 25:
                shifted_index = shifted_index - 26
            # Record the shifted letter
            shifted_letter = alphabet[shifted_index]
            # Add the shifted letter to the encrypted text
            encrypted_text += shifted_letter
    
    # Display the encrypted text
    print(f"Here's the encoded result: {encrypted_text}")

# Decrypt the text message by shifting each letter to the left
def decrypt(cipher_text, shift_amount):
    # Default decrypted text
    decrypted_text = ""

    # Iterate through each letter of the text
    for letter in cipher_text:
        # Add space when letter is blank
        if letter == " ":
            decrypted_text += " "
        else:
            # Record the index of the shifted letter
            shifted_index = alphabet.index(letter) - shift_amount
            # If the shift exceeds the last alphabet, the index will reset from the last
            if shifted_index < 0:
                shifted_index = shifted_index + 26
            # Record the shifted letter
            shifted_letter = alphabet[shifted_index]
            # Add the shifted letter to the decrypted text
            decrypted_text += shifted_letter
    
    # Display the decrypted text
    print(f"Here's the decoded result: {decrypted_text}")


# When the program is played, main function is executed
if __name__=="__main__":
    main()
