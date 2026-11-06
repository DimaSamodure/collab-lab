VOWELS = set("aeiouAEIOU")

def count_vowels(text):
    return {v: text.count(v) for v in "aeiou" if text.count(v)}

def total_vowels(text):
    return sum(1 for ch in text if ch in VOWELS)

if __name__ == "__main__":
    print(count_vowels("hello world"))
    print(total_vowels("hello world"))
