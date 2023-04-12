alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction.lower() == "decode":
        shift_amount *= -1
    for char in start_text:
        # TODO-2: If code includes number/symbol, do not have to change it

        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")



# TODO-3: Restart the program if the user wants to code/decode again

execute_program = False

while not execute_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-1: Take into account shift number of more than 26 (more than the no of alphabets)

    if shift > 26:
        shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    response = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if response.lower() == "no":
        execute_program = True

print("Goodbye")
