VOWELS = ['a', 'e', 'i', 'o', 'u']

# Finds the longest consecutive string of vowels and consonants in enable1.txt
def main():
    f = open('enable1.txt')

    long_c = 0
    long_v = 0
    cons_len = 0
    vowel_len = 0
    long_cons_word = ''
    long_vowel_word = ''

    for line in f:
        cons_len = longest_consonant(line)
        vowel_len = longest_vowel(line)
        if long_c < cons_len:
            long_c = cons_len
            long_cons_word = line
        if long_v < vowel_len:
            long_v = vowel_len
            long_vowel_word = line

    print 'Longest consonant string: %d, %s' % (long_c, long_cons_word)
    print 'Longest vowel string: %d, %s' % (long_v, long_vowel_word)

# Returns the length of the longest string of consonants in the word
def longest_consonant(word):
    const = 0
    max_const = 0

    for letter in word:
        if letter not in VOWELS:
            const += 1
        else:
            if const > max_const:
                max_const = const
            const = 0

    return max_const

# Returns the length of the longest string of vowels in the word
def longest_vowel(word):
    vowel = 0
    max_vowel = 0

    for letter in word:
        if letter in VOWELS:
            vowel += 1
        else:
            if vowel > max_vowel:
                max_vowel = vowel
            vowel = 0

    return max_vowel

        

if __name__ == "__main__":
    main()
