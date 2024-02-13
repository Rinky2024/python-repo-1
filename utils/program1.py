from collections import Counter


def word_frequency(line):
    words = line.split()
    word_count = Counter(words)

    # Filter out words with frequency > 1
    filtered_word_count = {word: freq for word, freq in word_count.items() if freq == 1}

    # Sort the dictionary by keys
    sorted_word_count = dict(sorted(filtered_word_count.items()))

    # Print the result in the desired format
    for word, freq in sorted_word_count.items():
        print(f'("{word}", {freq})')
