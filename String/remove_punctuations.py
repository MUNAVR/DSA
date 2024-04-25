import string


def remove_punctuations(strings):
    l=[]
    for char in strings :
        if char not in string.punctuation:
            l.append(char)
        
    return ''.join(l)

input_string = "Hello, World! This is a test string."
cleaned_string = remove_punctuations(input_string)
print(cleaned_string)