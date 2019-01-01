from lemmatize import *
import re

def nounify_tag(word, tag):
    '''
    Input: Word you want to convert to noun, Tag in PTB format
    Output: Nounified noun
    '''
    return(nounify(word, get_wordnet_pos(tag)))

def nounify_context(word, sentence):
    '''
    Input: Word you want to convert to noun, Paragraph to which that word belongs
    Output: Nounified noun
    '''
    # pos_dict will have pos tags of corresponding words
    pos_dict = dict()
    # tokenize para into sentences
    sentences = sent_tokenize(sentence)
    # tokenize each word in sentence
    for sent in sentences:
        words = word_tokenize(sent)
        tags = pos_tag(words)
        for (word, type) in tags:
            tag = get_wordnet_pos(type)
            if tag == '':
                continue
            if word in pos_dict:
                pos_dict[word.lower()].append(type)
            else:
                pos_dict[word.lower()] = [type]

    # choose the most popular pos tags
    pos_filter = dict()

    for key, value in pos_dict.items():
        pos_list = pos_dict[key]
        data = Counter(pos_list)
        pos_tag_word = max(pos_list, key = data.get) # get most probable pos tag for a word in that para
        unit = re.sub(r'[^\w\s]', '', key) # minor cleaning
        if len(unit) > 1:
            pos_filter[unit] = pos_tag_word

    tag = pos_filter[word.lower()]
    return(nounify(word, get_wordnet_pos(tag)))

# print(nounify_tag("elect", "VV"))
# print(nounify_context("russian", "Nick is Russian"))
