def ascii_count(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    ascii_count = 0
    for character in sentence:
        if character.isalpha():
            ascii_code = ord(character)
            if character in vowels:
                ascii_count -= ascii_code
            else:
                ascii_count += ascii_code
    return ascii_count
print(ascii_count("Dealing with failure is easy: Work hard to improve. Success is also easy to handle: You’ve solved the wrong problem. Work hard to improve."))
print(ascii_count("why and how"))