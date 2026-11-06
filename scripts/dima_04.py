"""Anagram check utility."""


def is_anagram(a, b):
    return sorted(a.lower()) == sorted(b.lower())


if __name__ == "__main__":
    print(is_anagram("listen", "silent"))
    print(is_anagram("hello", "world"))
