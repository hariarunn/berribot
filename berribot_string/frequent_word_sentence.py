s1 = input("Enter the string: ")
words = s1.split()

freq = {}  # dictionary to count frequency

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

# find word with maximum frequency
most_frequent = max(freq, key=freq.get)
print(most_frequent)
