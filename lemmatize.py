from nltk.corpus import wordnet as wn
from nltk.corpus import brown
from nltk import FreqDist
from nltk.stem import WordNetLemmatizer
from nltk import sent_tokenize, word_tokenize, pos_tag
from collections import Counter
import pickle

# frequency_dict = FreqDist(i.lower() for i in brown.words())
#
# with open('freqdict.pkl', 'wb') as freqdict:
#     pickle.dump(frequency_dict, freqdict)

with open('freqdict.pkl', 'rb') as freqdict:
    frequency_dict = pickle.load(freqdict)

WN_NOUN = 'n'
WN_VERB = 'v'
WN_ADJECTIVE = 'a'
WN_ADJECTIVE_SATELLITE = 's'
WN_ADVERB = 'r'
wordnet_lemmatizer = WordNetLemmatizer()

def nounify(word, from_pos, to_pos = "n"):
    """ Returns nounification """

    # convert to singular
    word = wordnet_lemmatizer.lemmatize(word)

    synsets = wn.synsets(word, pos=from_pos)

    # Word not found
    if not synsets:
        return None

    # Get all lemmas of the word (consider 'a'and 's' equivalent)
    lemmas = []
    for s in synsets:
        for l in s.lemmas():
            if s.name().split('.')[1] == from_pos or from_pos in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE) and s.name().split('.')[1] in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE):
                lemmas += [l]

    # Get related forms
    derivationally_related_forms = [(l, l.derivationally_related_forms()) for l in lemmas]

    # filter only the desired pos (consider 'a' and 's' equivalent)
    related_noun_lemmas = []

    for drf in derivationally_related_forms:
        for l in drf[1]:
            if l.synset().name().split('.')[1] == to_pos or to_pos in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE) and l.synset().name().split('.')[1] in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE):
                related_noun_lemmas += [l]

    # Extract the words from the lemmas
    words = [l.name() for l in related_noun_lemmas]

    # lowercase and remove duplicates
    filtered = list(set([x.lower() for x in words if x.lower() != word.lower()]))

    # choose the most common word for that particular relation
    words = [(x, frequency_dict[x]) for x in filtered]
    words.sort(key = lambda w: -w[1])

    if len(words) > 0 and len(words[0][0]) > 0:
        return words[0][0]
    else:
        return None

def get_wordnet_pos(treebank_tag):
    ''' returns wordnet POS tag '''
    if treebank_tag.startswith('J'):
        return wn.ADJ
    elif treebank_tag.startswith('V'):
        return wn.VERB
    elif treebank_tag.startswith('N'):
        return wn.NOUN
    elif treebank_tag.startswith('R'):
        return wn.ADV
    else:
        return None # for easy if-statement
