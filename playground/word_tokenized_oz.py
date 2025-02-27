import nltk
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize

def word_sentence_tokenize(text):
    sentence_tokenizer = PunktSentenceTokenizer()

    sentence_tokenized = sentence_tokenizer.tokenize(text)

    word_tokenized = list()

    for tokenized_sentence in sentence_tokenized:
        word_tokenized.append(word_tokenize(tokenized_sentence))
    return word_tokenized

oz_text = open(r"C:\Users\exol1\Parsing-w-regex\Compiling-and-matching\Wizard_Of_Oz.txt", encoding='utf-8').read().lower()
word_tokenized_text = word_sentence_tokenize(oz_text)
