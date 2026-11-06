"""Vowel counter utility."""


def count_vowels(text):
    vowels = set("aeiouAEIOU")
    return sum(1 for ch in text if ch in vowels)


if __name__ == "__main__":
    print(count_vowels("hello world"))
