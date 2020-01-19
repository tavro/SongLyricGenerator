import random

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

def get_random_first_word():
    popular = ['your', 'all', 'on', 'know', 'oh', 'that', 'up', 'love', 'of', 'when']
    common = ['if', 'say', 'be', 'for', 'just', 'baby', 'this', 'down', 'will', 'what', 'can', 'but', 'are', 'been', 'is', "don't", 'we', 'am', 'she', 'dont', "i've", 'have', "it's", 'as', 'like', 'wanna', 'leaving']
    ordinary = ['let', 'night', 'so', 'really', 'right', 'no', "i'll", 'cause', "you're", 'there', 'come', 'take', 'home', 'see', 'her', 'things', 'about', 'go', 'already', 'everything', 'long', 'time', 'think', 'call', 'hold', 'do', 'never', 'heart', 'too', 'our', 'not', 'said', 'mine', 'with', 'some', 'lost', 'dead', 'better', 'its', 'at', 'little', 'skin', 'into', 'who', 'get', 'was', 'off', 'give', 'away', 'even', 'trying', 'nothing', 'wherever', 'gone', "we're", 'mind', 'by', 'used', 'wrong', 'sun', 'from', 'sound', 'why', 'back', 'inside', "should've", 'monsoon', 'rollin', 'everyday']
    some_times = ["you'd", 'man', 'one', 'these', 'fall', "that's", 'need', 'ever', 'next', "won't", 'way', 'remember', 'day', 'loved', 'youre', 'before', 'maybe', 'or', 'mean', 'stay', 'then', 'coming', 'he', 'should', 'darling', 'again', 'tell', 'words', 'truth', 'may', 'still', 'young', 'an', 'face', 'soon', 'bed', 'left', 'done', 'through', 'than', 'head', 'make', 'good', 'ooh', 'only', 'thing', 'could', 'own', 'find', 'try', 'gonna', 'beauty', 'together', 'found', 'â€‹', 'want', 'putting', 'stones', 'wings', 'name', 'game', 'feel', 'alone', 'read', 'life', "ain't", 'those', 'older', 'says', 'old', 'enough', 'lay', 'every', 'past', "can't", 'got', 'write', 'getting', "she's", 'another', 'songs', 'would', 'guess', 'lights', 'best', 'end', 'hear', 'lord', 'dress', 'chameleon', 'last', 'song', 'everybody', 'knows', 'job', 'follow', 'going', 'comes', 'oh-oh-oh-oh', 'river', 'gaze', 'ground', 'quit', 'safe', 'girl', 'falling', 'surrender', 'without', 'further']
    unpopular = ["i'd", 'arms', 'wanted', 'look', 'side', 'did', 'theres', 'stuck', 'year', 'two', 'hope', 'anna', 'water', 'wine', 'room', 'came', 'sing', 'first', 'near', 'turned', 'blind', 'fray', 'weight', 'tamed', 'catch', 'blues', 'stop', 'stick', "what's", 'figures', 'em', 'watch', 'wait', 'smile', 'worst', 'saying', "we'll", 'drive', 'heard', 'wonder', 'here', 'alive', 'costs', 'his', 'speak', 'till', 'walk', 'friend', 'early', 'low', 'smoke', 'hand', 'awake', 'word', 'warm', 'today', 'kitchen', "one's", 'wind', 'loves']
    bad = ['climb', 'walls', 'softly', 'ship', 'south', 'scared', 'laughing', 'save', 'sometime', 'pull', 'unholy', 'daylight', 'shut', "they're", 'starting', 'prompt', 'downtown', 'sticker', 'hes', 'smelled', 'running', 'clean', 'understood', 'refuse', 'care', 'mes', 'true', 'finally', 'thats', 'ok', 'whole', 'demons', 'compare', 'stories', 'trials', 'glories', "mine's", 'boring', 'youve', 'thought', 'id', 'ignore', 'la', 'become', 'saving', 'parachute', 'breath', 'youth', 'pretend', 'fool', 'foool', 'lead', 'demon', 'hides', 'sleeve', 'salty', 'memories', 'stored', 'part-by-part', 'blunder', 'farse', 'self-serving', "love's", 'forgot', 'art', 'launched', 'thousand', 'ships', 'war-torn', 'kiss', 'flower', 'created', 'unsaid', 'compared', 'bending', 'knee', 'wasnt', 'stood', 'beneath', 'burning', 'tree', 'hoped', 'rescue', 'leaves', 'figured', 'bout', 'hey', 'hearts', 'weve', 'won', 'restless', 'thieves', 'shiver', 'theyre', 'warmer', 'ones', 'bet', 'youd', 'starve', 'roll', 'arrows', 'met', 'iron', 'archers', 'kings', 'settled', 'sell', 'fell', 'risk', 'limbs', 'closer', 'break', 'neck', 'stars', 'dare', 'reckless', 'wandering', 'ours', 'feed', 'breathe', 'grieve', 'feast', 'beast', 'release', 'unprepared', 'woman', 'dreaming', 'swear', 'loving', 'making', 'wife', 'sore', "'til", 'lonely', 'ohh', 'nobody', 'birds', 'feather', 'flock', 'ya', 'weather', 'wipe', 'tears', 'dear', 'glad', 'scream', 'sane', 'throne', 'dime', 'store', 'penny', 'crying', 'calling', 'code', 'apologies', 'boarding', 'hospital', 'empty', 'wishing', 'fairytale', 'send', 'whiskey', 'gin', 'babe', 'living', 'sin', 'drinking', "cryin'", 'gamble', "loving's", 'played', 'throw', 'dice', 'someplace', 'wake', "tryin'", 'born', 'worm', 'spins', 'cocoon', 'sleep', 'wakes', 'butterfly', 'hopeless', 'notice', 'bound', 'sure', 'destruction', 'closed', 'letter', 'town', 'went', 'carried', 'weapon', 'tells', '"i\'m', 'lit', 'dynamite', 'blow', 'down."', 'clock', 'whatever', 'point', 'figure', 'trouble', 'hands', 'mr.', 'kind', 'because', 'behind', 'bars', 'tomorrow', 'harder', 'aching', 'waking', 'throwing', 'chains', 'weighed', 'erase', 'final', 'fate', 'losing', 'any', 'definition', 'submit', 'fumble', 'stumble', 'awful', 'rough', 'knocked', 'takes', 'seat', 'blowing', 'ambitions', 'thoughts', 'spending', 'scenes', 'boss', 'rolling', 'rubber', 'sleeves', 'quickly', 'lover', 'bleeds', 'knees', 'crossed', 'reason', 'tossed', 'fifty', 'statisticians', "we'd", 'perfect', 'harmony', 'no...', 'impressed', 'strong', 'set', 'shown', 'ready', 'now.', 'hell', 'out.', 'space', 'bad', 'fade', 'times', 'them', 'friends', 'unto', 'please', 'everlasting', 'grace', 'eternity', 'fathers', 'voices', 'swinging', 'holy', 'sword', 'bought', 'warned', 'tries', 'yes', 'unattainable', 'float', 'high', 'below', 'ghosts', 'seems', 'slow', 'ahead', 'abuse', 'control', 'woo-woo', '[outro', 'chorus]', 'light', 'highs', 'heavy', 'lows', 'years', 'share', 'painted', 'arched', 'ceilings', 'barroom', 'floors', 'seasons', 'begin', 'change', 'ragged', 'mile', 'crave', 'nights', 'months', 'snowy', 'denver', 'mountains', 'bedroom', "fire's", 'weakest', 'flame', 'dying', 'rest', 'calm', 'sunrise', 'pours', 'window', 'floor', 'grip', 'pistol', 'howling', 'dog', 'door', 'voice', 'missed', 'dripping', 'ink', 'pen', 'note', 'hit', 'distance', 'such', 'surprise', 'which', 'person', 'sad', 'somewhere', 'rhyme', "isn't", 'listening', 'white', 'dress.', 'quiet', 'afternoons', 'given', 'soon.', 'hair', 'curls', 'pretty', 'uptight', 'mexican', 'girl.', 'shit', 'called', "isnt'", 'me.', 'wooo', 'ooooh', 'oooohh', 'string', 'silly', 'admit', 'guess.', 'dawn', 'darkness', 'once', 'twice', 'slice', 'none', 'wrong.', 'return', 'ask', 'disappointed', 'unexpected', 'harvest', 'kentucky', 'son', 'runs', 'farthest', 'doing', 'faith', 'belief', 'except', 'teeth', 'champions', 'rust', 'rot', 'breathing', 'missing', 'passing', 'brush', 'strokes', 'sickness', 'folks', 'renewed', 'unchanging', 'pasture', 'fenced', 'edge', 'dakota', 'thunder', 'raging', 'shoes', 'grass', "we've", 'laid', 'above', 'tunnel', 'shy', 'moves', 'never-ending', 'desire', 'calcified', 'lose', 'unspeakable', 'denial', 'crimes', 'versatile', 'raining', 'sea', 'shaking', 'winter', "pourin'", 'fine', 'february', 'fiddler', 'drum', 'bleak', 'halls', "architect's", 'un-imagination', 'returning', 'venue', 'held', 'very', 'conversation', 'arrived', 'swanned', 'later', 'nod', 'order', 'double', 'mixer', 'told', "playmate's", 'successful', 'handsome', 'charming', 'damn', 'wound', 'harming', 'joking', 'rudely', 'interrupted', 'half-wit', 'boyfriend', 'beat', 'were', 'dreamed', "'93", 'over', 'picks', 'bones', 'guitar', 'louder', 'anymore', 'tired', 'ran', 'forever', 'arm', 'setting', 'higher', 'perfection', 'book', 'hid', 'page', "didn't", 'locked', 'cage', 'novel', 'likes', 'started', 'rare', 'fragile', 'bird', "couldn't", 'spell', 'table', 'sky', 'cold', 'apple', 'story', 'proper', 'hello', 'felt', 'hero', 'tale', 'truly', 'prevail', 'sequel', "part's", 'die', 'movie', 'tragic', 'grey', 'short', 'roads', 'smooth', 'wanderings', 'bring', 'wisdoms', 'gold', 'most', 'matter', 'happiness', 'lasting', 'real', 'purify', 'passions', 'wet', 'stretch', 'paws', 'along', 'shores', 'depths', 'crouch', 'spiders', 'raindrops', 'singing', 'reverie', 'cuz', 'miss', 'hollow', 'stallion', 'nightmares', 'armistice', 'stalk', 'gibberish', 'moon', 'different', 'language', 'cannot', 'after', 'june', 'pine', 'brushing', 'dew', 'unlike', 'copious', 'death', 'precipitation', 'carry', "something's", 'pending', 'curvaceously', 'sunburned', 'agree', "pleasure's", 'chin', 'mess', 'pool', 'spent', 'sunday', 'school', 'july', 'golden', 'hue', 'hung', 'drove', 'straight', 'burial', 'saw', 'loud', 'gray-blue', 'grave', 'red', 'suits', 'five', 'took', '405', 'act', 'age', 'asleep', 'choose', 'midnight', 'pocketbook', 'hate', 'anyway', 'another...', 'safety', 'pride', 'keeping', 'score', 'fear', 'downfall', 'enemy', 'blame', 'fault', 'core', 'steady', 'crash', 'nice', 'canâ€…seeâ€…right', 'theyâ€…marked', 'woodenâ€…cross', 'gal', "'sorry", "loss'", 'ended', 'saturday', 'showdown', 'fire', 'hits', 'bottle', 'sits', 'weak', 'stand', 'saint', 'paula', 'skies', 'memory', 'swimming', 'infinity', 'black', 'wire', 'sings', 'blue', 'following', 'cloud', 'hot', 'mother', 'father', 'cut', 'jesus', 'stronger', 'hopin', 'comin', 'late', 'blinded', 'relates', 'loathsome', 'sounds', 'texas', 'funerals', 'breakin', 'somehow', 'feels', 'brain', 'fried', 'griddle', 'cant', 'beggin', 'rain', 'losin', 'guts', 'split', 'howlin', 'feedin', 'petunia', 'cmon', 'prowlin', 'crawlin', 'gotta', 'lonesome', 'couldnt', 'seen', 'whisper', 'whos', 'taken', 'well-earned', 'reward', "takin'", 'shadow', 'errors', 'steal', "placin'", 'path', 'touch', 'letting', 'pleases', 'crime', 'crushed', 'bone', 'spoken', 'sweeter', 'yesterday', 'abiding', 'anything', 'claim', 'victory', 'died', 'cross', 'rose', 'yours', 'radiant', 'glorious', 'remain', 'mystery', 'mysteries', 'heaven', 'enshrined', 'nighthawk', 'diner', 'blueberries', 'cinnamon', 'cup', 'coffee', 'cream', 'fuel', 'cigarette', 'reading', 'instruction', 'manual', 'start', 'consider', 'desired', "wasn't", 'bit', 'umpire', "else's", 'sweat-faced', 'counter', 'half-regretting', 'flyer', 'watching', 'silver', 'soda', 'underneath', 'ceiling', 'fan', 'half-consumed', 'perspire', 'tendency', 'laugh', 'moments', 'silent', 'type', 'exit', 'sign', 'yellow', 'brick', 'miles', 'each', 'future', 'holds', 'surface', 'storm', 'sunset', 'hurricane', 'vincent', 'van', 'gogh', 'feeling', 'clearly', 'nearly', 'heal', 'fades', 'feelings']
    
    rand = random.randint(0, 100)
    if rand >= 0  and rand < 35:
        return popular[random.randint(0, len(popular)-1)]
    elif rand >= 35 and rand < 65:
        return common[random.randint(0, len(common)-1)]
    elif rand >= 65 and rand < 80:
        return ordinary[random.randint(0, len(ordinary)-1)]
    elif rand >= 80 and rand < 90:
        return some_times[random.randint(0, len(some_times)-1)]
    elif rand >= 90 and rand < 95:
        return unpopular[random.randint(0, len(unpopular)-1)]
    elif rand >= 95 and rand <= 100:
        return bad[random.randint(0, len(bad)-1)]

def is_ending_prepositions(word):
    return word == "a" or word == "i" or word == "as" or word == "if" or word == "your" or word == "to" or word == "and" or word == "let" or word == "my" or word == "just" or word == "the" or word == "til" or word == "of" or word == "but" or word == "when" or word == "such" or word == "in" or word == "just"


def get_random_line():
    great_generated_lines = ["Im used to say it should've been", "And dont i know i am lost", "I can feel you hope mine's not", "To tell me i dont wanna stop", 
                                         "I haven't felt this in my mind", "This is up in your chameleon skin", "Your pocketbook can't hear he's handsome and unprepared", 
                                         "When i give me down and carry on", "Woman dreaming of your pen left town tonight", "All my dreams i can do nothing without", 
                                         "And even when i haven't been me", "If this is this go by my side", "A damn good job everybody likes", "You and i can't get used", 
                                         "Remember who i've already shown that i am", "Baby dont wanna get off my saving parachute", "Been lost but oh oh no longer lost",
                                         "I know that song and i know", "My love in my hand oh", "Don't follow what i know what pleases me", "Its hot and we'll keep putting stones on", 
                                         "Wanna remember who i've been who i've lost", "I will i still got your throne", "She says that you will close down", 
                                         "We drink of all that i won't be", "My love my tries to fly away", "That said i have been a fool", "On my bed she tells him it's", 
                                         "Already done wrong and some call his name", "I haven't been me nothing without you", "Don't wanna remember who i've already past", 
                                         "And i am unchanging i'm getting further", "Your restless little boy and every morning sunrise", "Wanna heal but it should've been lonesome", 
                                         "That you used to be in your mind", "All lies crash into my chest like it", "My wings i will i know it", "Im so much older baby please", 
                                         "I haven't been me go now", "My emotions i'm waking up leaving it", "End of my love to love in reverie", "Im used to you wanna remember who", 
                                         "The floor hold you from the core", "You are warm today dont wanna heal", "When you're impressed that i know what", 
                                         "Will risk our eyes and take the life", "I know it takes a little boy", "Love oh i will close down and all", 
                                         "We are sad songs that i could blow", "This was wrong and i forget the miles", "Just like me you'd pull me she said", 
                                         "Baby dead like me i wish i watch", "On my bed she said i'm just another", "Know what you take oh oh no this", 
                                         "Know it was dead like you are radiant", "You only known love you're gonna lie", "I dont i keep trying to be", 
                                         "That showed you i don't really know oh", "You say what you oh-oh-oh-oh oh-oh-oh-oh oh-oh-oh-oh", "I show me time to be", 
                                         "It should've been me something picks me", "I already know what i will love", "You keep putting stones on the weakest", 
                                         "Try to meet somebody i will i will", "Wooo oooohh i can i love you", "As i still think i call goodbye", "Why oh oh oh lying awake", 
                                         "The fray weight of iron skin", "My eyes that's all of all", "Act my baby dont wanna hear the fuck", "I'd climb these songs are the best", 
                                         "But i pray something clearly gone baby please", "When i know i feed off the best", "All i hear he went she hides her", 
                                         "When i feel the love you have played", "Will come pourin' down it's in the darkness", "Gal 'sorry for me that i don't give", 
                                         "She said we'd live in love darling"]
    return great_generated_lines[random.randint(0, len(great_generated_lines)-1)]
