from collections import Counter

def np_chunk_counter(chunked_sentences):

    chunks = list()

    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter = lambda t: t.label () == 'NP'):
            chunks.append(tuple(subtree))
    
    chunk_counter = Counter()

    for chunk in chunks:
        chunk_counter[chunk] += 1

    return chunk_counter.most_common(30)

def vp_chunk_counter(chunked_sentences):
    chunks = list()
    for chunked_sentence in chunked_sentences:
        for subtree in chunked_sentence.subtrees(filter = lambda t: t.label() == "VP"):
            chunks.append(tuple(subtree))
    chunk_counter = Counter()

    for chunk in chunks:
        chunk_counter[chunk] += 1

    return chunk_counter.most_common(30)

