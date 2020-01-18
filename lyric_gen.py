import random
import wordhandling
import pathhandling
import library

def create_section(line_amount, word_amount, section, words):
    final = [section]
    all_words = wordhandling.get_all_words(pathhandling.paths)
    word = ""

    for i in range(line_amount):
        random_index = random.randint(0, len(words) - 1)
        word = words[random_index]

        first_letter = word[0].upper()
        word_rest = word[1:]
        line = first_letter + word_rest + " "

        for j in range(word_amount):
            following_words = wordhandling.words_that_follow(word, all_words)[word]
            rand_index = random.randint(0, len(following_words) - 1)
            word = following_words[rand_index]
            line+=word + " "
        final.append(line)

    return final

def print_section(section):
    for line in section:
        print(line)

def print_song(verses, chorus):
    last_index = len(verses) - 1
    for i in range(len(verses)):
        print_section(verses[i])
        print()
        if not (i == last_index):
            print_section(chorus)
            print()

words = library.words

chorus = create_section(9, 6, "[CHORUS]", words)
verses = [create_section(8, 7, "[VERSE]", words),create_section(8, 7, "[VERSE]", words),create_section(8, 7, "[VERSE]", words)]

print_song(verses, chorus)


