# Count Vowels and Consonants
text = input('enter the string: ').lower()
vowels = 'aeiou'
vowel_count = sum(1 for char in text if char in vowels)
consonets_count = sum(1 for char in text if char.isalpha() and char not in vowels)

print(f'Vowels: {vowel_count}, Consonants: {consonets_count}')