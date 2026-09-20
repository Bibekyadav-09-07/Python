# Function to generate the ASCII hash
def generate_ascii_hash(char1, char2, char3):
    ascii1 = ord(char1)
    ascii2 = ord(char2)
    ascii3 = ord(char3)

    hash_value = ascii1 * ascii2 * ascii3

    return hash_value


# Function to check the strength of the hash
def check_strength_level(hash_value):
    if hash_value > 500000:
        return "STRONG HASH"
    else:
        return "WEAK HASH"


# Main program
char1 = input("Enter the first character: ")
char2 = input("Enter the second character: ")
char3 = input("Enter the third character: ")

# Display ASCII values
ascii1 = ord(char1)
ascii2 = ord(char2)
ascii3 = ord(char3)

# Generate hash
hash_value = generate_ascii_hash(char1, char2, char3)

# Check hash strength
strength = check_strength_level(hash_value)

# Security Readout
print("\n----- SECURITY READOUT -----")
print("Character 1:", char1)
print("ASCII Value:", ascii1)

print("Character 2:", char2)
print("ASCII Value:", ascii2)

print("Character 3:", char3)
print("ASCII Value:", ascii3)

print("Hash Value:", hash_value)
print("Hash Strength:", strength)