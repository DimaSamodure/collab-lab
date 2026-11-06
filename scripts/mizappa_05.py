from collections import Counter


def word_count(text):
    words = text.lower().split()
    return dict(Counter(words))


if __name__ == "__main__":
    print(word_count("hello world hello collab lab"))
