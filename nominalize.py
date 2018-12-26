from lemmatize import *

# text = "Nick is Russian."
# pos_dict = dict()
#
# sentences = sent_tokenize(text)
#
# for sent in sentences:
#     words = word_tokenize(sent)
#     tags = pos_tag(words)
#     for (word, type) in tags:
#         tag = get_wordnet_pos(type)
#         if tag == '':
#             continue
#         if word in pos_dict:
#             pos_dict[word.lower()].append(type)
#         else:
#             pos_dict[word.lower()] = [type]

def nounify_tag(word, tag):
    '''
    Input: Word you want to convert to noun, Tag in PTB format
    Output: Nounified noun
    '''
    return(nounify(word, get_wordnet_pos(tag)))

print(nounify_tag("elect", "VV"))
