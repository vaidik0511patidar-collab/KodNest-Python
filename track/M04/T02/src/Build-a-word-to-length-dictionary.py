def build_word_to_length_dictionary(words):
    # Write your dictionary comprehension here

    return {word : len(word) for word in words}


n = int(input())
words = input().split()

word_length = build_word_to_length_dictionary(words)

for word, length in word_length.items():
    print(word, length)