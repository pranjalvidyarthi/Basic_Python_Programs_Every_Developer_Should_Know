# Find the Largest Word in a Sentence
sentence = input("Enter a sentence: ").split()
largest_word = max(sentence, key=len)
print(f'Largest word: {largest_word}')