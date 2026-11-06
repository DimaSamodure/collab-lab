def caesar_cipher(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result


if __name__ == "__main__":
    print(caesar_cipher("hello", 3))
    print(caesar_cipher("khoor", -3))
