# Function to return the highest value of a consonant
def solve(s):
    # Define vowels and assign values to consonants
    vowels = "aeiou"
    consonant_values = {char: i + 1 for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}
    
    # Function to calculate the value of a consonant substring
    def get_consonant_value(substring):
        return sum(consonant_values[char] for char in substring)

    # Initialize variables
    max_consonant_value = 0
    current_consonant = ""

    # Iterate through the characters in the input string
    for char in s:
        # Check if the character is a vowel
        if char not in vowels:
            current_consonant += char  # If it's a consonant, add it to the current consonant substring
        else:
            # If it's a vowel, calculate the value of the current consonant substring
            if current_consonant:
                value = get_consonant_value(current_consonant)
                max_consonant_value = max(max_consonant_value, value)  # Update the maximum consonant value if needed
                current_consonant = ""  # Reset the current consonant substring

    # Check the last substring if it ends with a consonant
    if current_consonant:
        value = get_consonant_value(current_consonant)
        max_consonant_value = max(max_consonant_value, value)  # Update the maximum consonant value if needed

    return max_consonant_value

print(solve("zodiacs"))    

