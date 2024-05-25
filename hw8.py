def find_first_repeating_character(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            print("First repeating character:", char)
            print("Memory address:", id(char))
            return char, id(char)
        else:
            char_count[char] = 1
            
    return None


input_string = "abcdefgabc"
result = find_first_repeating_character(input_string)
if result is None:
    print("No repeating character found.")