def capitalize(string):
    words = string.split()  # Split the string into words
    result = ''  # Initialize an empty string to store the result
    
    for word in words:
        # Capitalize the first letter of each word and append it to the result
        capitalized_word = word[0].upper() + word[1:]
        result += capitalized_word+' '
    
    # Remove the extra space at the end of the result
    return result


def capitalize_first_letter(string):
    return ' '.join(word.capitalize() for word in string.split())

def capital(string):
    return ' '.join(word.capitalize() for word in string.split())

input_string = input("Enter a string: ")
print(capitalize_first_letter(input_string))
print(capital(input_string))
print(capitalize(input_string))


