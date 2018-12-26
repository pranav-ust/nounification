# Nounification

I could not see any similar tool on github, so here you go.
This is a handy tool which performs "nounification" or nominalization.

This is often useful in keyword extraction based algorithms.

You can use two functions in `nominalize.py`, which are:

1. **Nominalization based on the given tag**

`print(nounify_tag("elect", "VV"))` would give you `election`

2. **Nominalization based on the given context**

`print(nounify_tag("russian", "He is Russian."))` would give you `russia`
