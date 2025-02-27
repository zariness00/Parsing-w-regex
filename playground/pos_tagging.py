import nltk
from nltk import pos_tag, RegexpParser, Tree
from chunk_counter import np_chunk_counter, vp_chunk_counter
from word_tokenized_oz import word_sentence_tokenize

oz_text = open(r"C:\Users\exol1\Parsing-w-regex\Compiling-and-matching\Wizard_Of_Oz.txt", encoding='utf-8').read().lower()
word_tokenized_text = word_sentence_tokenize(oz_text)

witches_fate = word_tokenized_text[100] 
print(witches_fate)

# creating a list to hold part-of-speech tagged sentences here
pos_tagged_oz = []

for word in word_tokenized_text:
    pos_tagged_oz.append(pos_tag(word))

witches_fate_pos = pos_tagged_oz[100]
print(witches_fate_pos)

# defining adjective-noun chunk grammar here
chunk_grammar = "AN: {<JJ><NN>}"

#creating RegexpParser object below
chunk_parser = RegexpParser(chunk_grammar)

#chunking the pos tagged setnece at index 282 in my list before
scaredy_cat = chunk_parser.parse(pos_tagged_oz[282])
print(scaredy_cat)
# pretty_print the chunked sentence here
Tree.fromstring(str(scaredy_cat)).pretty_print()


#Noun phrase chunking 

np_chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"
vp_chunk_grammar = "VP: {<VB.*><DT>?<JJ>*<NN><RB.?>?}"

np_chunk_parser = RegexpParser(np_chunk_grammar)
vp_chunk_parser  = RegexpParser(vp_chunk_grammar)

np_chunked_oz = list()
vp_chunked_oz = list()

for pos_sentence in pos_tagged_oz:
    np_chunked_oz.append(np_chunk_parser.parse(pos_sentence))
    vp_chunked_oz.append(vp_chunk_parser.parse(pos_sentence))
most_common_np_chunks = np_chunk_counter(np_chunked_oz)
most_common_vp_chunks = vp_chunk_counter(vp_chunked_oz)
print(most_common_np_chunks)
print(most_common_vp_chunks)