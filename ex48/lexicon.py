
lexicon = {
    ('directions', 'north'),
    ('directions', 'south'),
    ('directions', 'east'),
    ('directions', 'west')
    }

def scan(text):

    words = text.lower().split()
    pairs = []

    for word in words:
        word_type = lexicon[word]
        tupes = (word, word_type) 
        pairs.append(tupes)

    return pairs