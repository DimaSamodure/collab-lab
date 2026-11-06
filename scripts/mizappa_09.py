def caesar_cipher(text, shift):
    out = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            out += chr((ord(ch) - base + shift) % 26 + base)
        else:
            out += ch
    return out


if __name__ == "__main__":
    print(caesar_cipher("hello", 3))
    print(caesar_cipher("khoor", -3))
