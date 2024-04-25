# def replace_alphabet(string, n):
#     result = ''  # Initialize an empty string to store the result
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'

#     # Create a dictionary to map each alphabet to its shifted alphabet
#     shifted_alphabet = {}
#     for i in range(26):
#         shifted_alphabet[alphabet[i]] = alphabet[(i + n) % 26]

#     # Iterate over each character in the input string
#     for char in string:
#         # Check if the character is an alphabet character
#         if char.lower() in alphabet:
#             # Determine the shifted character based on the dictionary
#             shifted_char = shifted_alphabet[char.lower()]
#             # Preserve the case of the original character
#             if char.isupper():
#                 shifted_char = shifted_char.upper()
#             # Append the shifted character to the result
#             result += shifted_char
#         else:
#             # If the character is not an alphabet, keep it unchanged
#             result += char

#     return result


def replace_alphabet(string, n):
    result = ''  # Initialize an empty string to store the result

    # Iterate over each character in the input string
    for char in string:
        # Check if the character is an alphabet character
        if char.isalpha():
            # Determine the position of the character in the alphabet
            if char.islower():
                position = ord(char) - ord('a')
                
            else:
                position = ord(char) - ord('A')
            # Calculate the new position after adding the offset 'n'
            new_position = (position + n) % 26
            
            # Determine the new character based on the position and case
            if char.islower():
                new_char = chr(ord('a') + new_position)
            else:
                new_char = chr(ord('A') + new_position)
            # Append the new character to the result
            result += new_char
        else:
            # If the character is not an alphabet, keep it unchanged
            result += char

    return result

# Test the function
input_string = input("Enter a string: ")
offset = int(input("Enter the offset (n): "))
print("String with each alphabet replaced:", replace_alphabet(input_string, offset))



