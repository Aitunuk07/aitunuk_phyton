words = input("Enter a word: ")  
vowels = "aeiou"  
vowel_count = 0
consonant_count = 0

for char in words:  
    if char.lower() in vowels:  
        vowel_count += 1
    elif char.isalpha():  
        consonant_count += 1

print("Vowel count:", vowel_count)
print("Consonant count:", consonant_count)