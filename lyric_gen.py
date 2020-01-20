import random
import wordhandling
import pathhandling
import library

def has_context(line):
    dic = library.context
    if line in dic:
        return True
    return False

def create_line_with_context(context_line):
    dic = library.context
    if context_line in dic:
        context_len = len(dic[context_line])-1
        return dic[context_line][random.randint(0, context_len)]

def create_section_from_data(line_amount, section):
    section = [section]
    for i in range(line_amount):
        if has_context(section[len(section)-1]):
            if random.randint(0, 10) > 5:
                line = create_line_with_context(section[len(section)-1])
            else:
                line = wordhandling.get_random_line()
        else:
            line = wordhandling.get_random_line()
        section.append(line)
    return section


def create_section(line_amount, word_amount, section, words):
    
    if section == "[VERSE]":
        r = random.randint(0, 100)
        if r > 98:
            #generate whole section instantly with pre-generated data
            return create_section_from_data(line_amount, section)

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
                line = wordhandling.get_random_line()
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
                if wordhandling.is_ending_prepositions(word):
                    break

            line+=word + " "

        if wordhandling.is_bad_line(line):
            line = wordhandling.get_random_line()

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


