def get_all_words(paths):
    data = []
    all_words = []
    for path in paths:
        string = open(path, 'r').read()
        data = data + string.split()
    for word in data:
        all_words = all_words + word.split(" ")
    return remove_tags_and_symbols_from_words(all_words,["â€™", ",", "?", ";", "!", "â€˜", "â€‹"])

def remove_tags_and_symbols_from_words(all_words, symbols):
    final = []
    for word in all_words:
        if word[0] == "[" and word[len(word)-1] == "]":
            continue
        else:
            for symbol in symbols:
                if symbol in word:
                    word = word.replace(symbol,'')
            final.append(word.lower())
    return final

def words_that_follow(word, all_words):
    final_dictonary = {word : []}
    for i in range(len(all_words)):
        if word == all_words[i]:
            if not (i == len(all_words)-1): 
                final_dictonary[word].append(all_words[i+1])
    return final_dictonary


