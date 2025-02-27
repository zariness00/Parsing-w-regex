from nltk import pos_tag, RegexpParser
from word_tokenized import word_sentence_tokenize
from chunk_counter import np_chunk_counter, vp_chunk_counter


# import text of choice here

iliad_text = open(r"C:\Users\exol1\Parsing-w-regex\the_iliad.txt", encoding='utf-8').read().lower()

# sentence and word tokenize text here
tokenized_text = word_sentence_tokenize(iliad_text)

# store and print any word tokenized sentence here
one_tokenized_sentence = tokenized_text[100]
#print(one_tokenized_sentence)

# create a list to hold part-of-speech tagged sentences here
pos_tagged_sentences = list()

# create a for loop through each word tokenized sentence here
for word in tokenized_text:
     # part-of-speech tag each sentence and append to list of pos-tagged sentences here
    pos_tagged_sentences.append(pos_tag(word))

 
  

# store and print any part-of-speech tagged sentence here
single_pos_sentence = pos_tagged_sentences[100]
#print(single_pos_sentence)


# define noun phrase chunk grammar here
np_chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"
# define verb phrase chunk grammar here
vp_chunk_grammar = "VP: {<VB.*><DT>?<JJ>*<NN><RB.?>?}"
# create noun phrase RegexpParser object here
np_chunk_parser = RegexpParser(np_chunk_grammar)
# create verb phrase RegexpParser object here
vp_chunk_parser  = RegexpParser(vp_chunk_grammar)
# create a list to hold noun phrase chunked sentences and a list to hold verb phrase chunked sentences here
np_chunked_text = list()
vp_chunked_text = list()



# create a for loop through each pos-tagged sentence here
# chunk each sentence and append to lists here
  
for pos_sentence in pos_tagged_sentences:
    np_chunked_text.append(np_chunk_parser.parse(pos_sentence))
    vp_chunked_text.append(vp_chunk_parser.parse(pos_sentence))
most_common_np_chunks = np_chunk_counter(np_chunked_text)
most_common_vp_chunks = vp_chunk_counter(vp_chunked_text)
print(most_common_np_chunks)
print(most_common_vp_chunks)











# store and print the most common NP-chunks here



# store and print the most common VP-chunks here

