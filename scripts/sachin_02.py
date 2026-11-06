def is_anagram(a, b):
    clean = lambda s: sorted(s.replace(" ", "").lower())
    return clean(a) == clean(b)

if __name__ == "__main__":
    print(is_anagram("listen", "silent"))
    print(is_anagram("hello", "world"))
