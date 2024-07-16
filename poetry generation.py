import nltk
import random
from nltk import word_tokenize
from nltk.probability import ConditionalFreqDist
from collections import defaultdict

# Load and tokenize the corpus
def load_and_tokenize(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return word_tokenize(text)

# Generate N-gram models
def generate_ngram_models(words, n):
    if n == 1:
        return ConditionalFreqDist((word,) for word in words)
    else:
        return ConditionalFreqDist(nltk.ngrams(words, n))

# Generate a verse using an N-gram model
def generate_verse(model, n, start_words, min_length=7, max_length=10):
    length = random.randint(min_length, max_length)
    if n == 1:
        verse = [random.choice(start_words)]
    else:
        verse = list(random.choice(start_words))
    
    while len(verse) < length:
        context = tuple(verse[-(n-1):])
        if context in model:
            next_word = random.choice(model[context].most_common())[0]
            verse.append(next_word)
        else:
            break
    return ' '.join(verse)

# Generate a stanza
def generate_stanza(model, n, start_words):
    stanza = []
    for _ in range(4):
        verse = generate_verse(model, n, start_words)
        stanza.append(verse)
    return '\n'.join(stanza)

# Main function to generate the poem
def generate_poem(style):
    if style == 'Shakespeare':
        words = load_and_tokenize('shakespeare.txt')
    else:
        words = load_and_tokenize('angelou.txt')
    
    start_words_unigram = [word for word in words if word.isalpha()]
    bigrams = list(nltk.bigrams(words))
    start_words_bigram = [bigram for bigram in bigrams if bigram[0].isalpha()]
    trigrams = list(nltk.trigrams(words))
    start_words_trigram = [trigram[:2] for trigram in trigrams if trigram[0].isalpha() and trigram[1].isalpha()]
    
    unigram_model = generate_ngram_models(words, 1)
    bigram_model = generate_ngram_models(words, 2)
    trigram_model = generate_ngram_models(words, 3)
    
    print("Unigram Model Stanza:\n")
    print(generate_stanza(unigram_model, 1, start_words_unigram))
    print("\n\n")
    
    print("Bigram Model Stanza:\n")
    print(generate_stanza(bigram_model, 2, start_words_bigram))
    print("\n\n")
    
    print("Trigram Model Stanza:\n")
    print(generate_stanza(trigram_model, 3, start_words_trigram))

# Ask user for the style
style = input("In which style do you want to generate the poem? (Shakespeare/Angelou): ")
generate_poem(style)
