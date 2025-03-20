import string
def find_most_frequent_word(text, illegibles):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    word_count = {}
    for word in words:
        if word not in illegibles and word not in word_count:
            word_count[word] = 1
        elif word in illegibles:
            continue
        else:
            word_count[word] += 1
    max_count = max(word_count.values())
    most_frequent = [word for word, count in word_count.items() if count == max_count]
    return most_frequent[0]

paragraph1 = "a."
illegibles1 = []
print(find_most_frequent_word(paragraph1, illegibles1)) 

paragraph2 = "Bob hit a ball, the hit BALL flew far after it was hit."
illegibles2 = ["hit"]
print(find_most_frequent_word(paragraph2, illegibles2)) 