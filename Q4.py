
def highest_occurring_character(text):
    char_count = {}

    for ch in text:
        if ch.isalpha():
            ch = ch.lower()
            if ch in char_count:
                char_count[ch] += 1
            else:
                char_count[ch] = 1

    highest_char = ""
    highest_count = 0

    for ch in char_count:
        if char_count[ch] > highest_count:
            highest_char = ch
            highest_count = char_count[ch]

    return highest_char, highest_count

def main():
    char, count = highest_occurring_character("hippopotamus")
    print("Highest occurring character:", char, count)

main()
