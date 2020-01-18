import random
import wordhandling
import pathhandling
import library

def create_section(line_amount, word_amount, section, words):
    final = [section]
    all_words = wordhandling.get_all_words(pathhandling.paths)
    word = ""

    for i in range(line_amount):
        if section == "[CHORUS]":
            most_used_words = ['you', 'to', 'in', 'i', 'my', 'the', 'and', 'a', 'it', 'im']
            random_index = random.randint(0, len(most_used_words) - 1)
            word = most_used_words[random_index]
        else:
            r = random.randint(0, 100)
            if r > 95:
                great_generated_lines = ["Im used to say it should've been", "And dont i know i am lost", "I can feel you hope mine's not", "To tell me i dont wanna stop", 
                                         "I haven't felt this in my mind", "This is up in your chameleon skin", "Your pocketbook can't hear he's handsome and unprepared", 
                                         "When i give me down and carry on", "Woman dreaming of your pen left town tonight", "All my dreams i can do nothing without", 
                                         "And even when i haven't been me", "If this is this go by my side", "A damn good job everybody likes", "You and i can't get used", 
                                         "Remember who i've already shown that i am", "Baby dont wanna get off my saving parachute", "Been lost but oh oh no longer lost"]
                line = great_generated_lines[random.randint(0, len(great_generated_lines)-1)]
                final.append(line)
                continue
            word = wordhandling.get_random_first_word()

        first_letter = word[0].upper()
        word_rest = word[1:]
        line = first_letter + word_rest + " "

        for j in range(word_amount):
            following_words = wordhandling.words_that_follow(word, all_words)[word]
            rand_index = random.randint(0, len(following_words) - 1)
            word = following_words[rand_index]

            if j == word_amount-1:
                if word == "a" or word == "i" or word == "as" or word == "if" or word == "your" or word == "to" or word == "and" or word == "let" or word == "my" or word == "just" or word == "the" or word == "til":
                    break

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


