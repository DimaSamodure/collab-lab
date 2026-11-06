def word_count(text):
    words = text.split()
    return len(words)


def char_count(text):
    return len(text)


if __name__ == "__main__":
    sample = "hello world from expedition"
    print(word_count(sample))
    print(char_count(sample))
