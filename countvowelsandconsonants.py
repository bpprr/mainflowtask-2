s = input("Enter a string: ").lower()
vowels = 'aeiou'
vowel_count = consonant_count = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
