import string

def remove_word(text, word):
    text = text.replace(word, '')
    return text

def remove_special_characters(text):
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    return text

def remove_extra_spaces(text):
    return ' '.join(text.split())

def remove_short_words(text):
    words = text.split()
    filtered_words = [word for word in words if len(word) >= 3]
    return ' '.join(filtered_words)
