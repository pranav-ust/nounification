# Nounification

I could not see any similar tool on github, so here you go.
This is a handy tool which performs "nounification" or nominalization.

This is often useful in keyword extraction based algorithms.

## Usage

You can use two functions in `nominalize.py`, which are:

1. **Nominalization based on the given tag**

`print(nounify_tag("elect", "VV"))` would give you `election`

2. **Nominalization based on the given context**

`print(nounify_context("russian", "He is Russian."))` would give you `russia`

## Requirements

Python 3

NLTK (with WordNet)

Pickle

## Methodology

1. The word is lemmatized into its root form.
2. The synsets of the root word is obtained from the correponding POS tag.
3. The lemmas of each word in synset are collected (narrowed down to desired tag / adjective).
4. Derivationally related forms are calculated of each lemma which were obtained in step 3.
5. The given forms are filtered into the desired POS tag.
6. Filtered lemmas are converted into proper words.
7. The resulting list is lowercased and duplicates are removed.
8. Probabilistic distribution of frequency (based on Brown Corpus) is applied and the word with highest probability is returned.


